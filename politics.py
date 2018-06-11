import requests 
from bs4 import BeautifulSoup
import sys
from pykafka import KafkaClient
import time

client = KafkaClient(hosts="127.0.0.1:9092") 
topic = client.topics[b'politics']
host = "https://tw.news.yahoo.com/politics"
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0'
headers = { 'User-Agent' : user_agent }
   
def getNews(link):
    response = requests.get(link,headers=headers)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text,"html.parser")
    content = ''
    for i in soup.select('article'):
        content+=i.get_text()
    return content

response = requests.get(host,headers=headers)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text,"html.parser")
while True:
    for i in soup.select('div[id="YDC-Stream"] > ul > li'):    
        if(i.find_next('div').get('class')[0]!='controller'):
            data = {}
            title = i.find('div').find('div').find('h3').find('a').get_text()
            link = 'https://tw.news.yahoo.com/'+i.find('div').find('div').find('h3').find('a').get('href')
            news = getNews(link).strip()    
            print(title,link)        
            if(news!=''):
                with topic.get_sync_producer() as producer:                
                    producer.produce(bytes(news,'utf-8')) 
    time.sleep(108000A)

               
