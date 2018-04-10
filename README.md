# Text-Analytics-System
## Flowchart
![Imgur](https://i.imgur.com/Bt9uNON.png)

## Description
* [politics.py](https://github.com/Spaert/Text-Analytics-System/blob/master/politics.py) / [entertainment.py](https://github.com/Spaert/Text-Analytics-System/blob/master/entertainment.py)  are to get the news from [Yahoo! politics](https://tw.news.yahoo.com/politics)/[Yahoo! entertainment](https://tw.news.yahoo.com/entertainment) and put the news into Kafka message queue



* [textanalytics_politics.py](https://github.com/Spaert/Text-Analytics-System/blob/master/textanalytics_politics.py) / [textanalytics_entertainment.py](https://github.com/Spaert/Text-Analytics-System/blob/master/textanalytics_entertainment.py) are to analysis the news with [Jeiba](https://github.com/fxsjy/jieba) and set up TF-IDF to compute the document similarity
* [politics.csv](https://github.com/Spaert/Text-Analytics-System/blob/master/politics.csv) / [entertainment.csv](https://github.com/Spaert/Text-Analytics-System/blob/master/entertainment.csv) are the result of the news similarity
