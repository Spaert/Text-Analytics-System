# Text-Analytics-System
## Flowchart
![Imgur](https://i.imgur.com/Bt9uNON.png)

## Description
* [politics.py](https://github.com/Spaert/Text-Analytics-System/blob/master/politics.py) / [entertainment.py](https://github.com/Spaert/Text-Analytics-System/blob/master/entertainment.py)  are to get the news from [Yahoo! politics](https://tw.news.yahoo.com/politics) / [Yahoo! entertainment](https://tw.news.yahoo.com/entertainment) and put the news into Kafka message queue



* [textanalytics_politics.py](https://github.com/Spaert/Text-Analytics-System/blob/master/textanalytics_politics.py) / [textanalytics_entertainment.py](https://github.com/Spaert/Text-Analytics-System/blob/master/textanalytics_entertainment.py) are to analysis the news with [Jeiba](https://github.com/fxsjy/jieba) and set up TF-IDF to compute the document similarity
* [politics.csv](https://github.com/Spaert/Text-Analytics-System/blob/master/politics.csv) / [entertainment.csv](https://github.com/Spaert/Text-Analytics-System/blob/master/entertainment.csv) are the result of the news similarity

## Result
After execute the  [politics.py](https://github.com/Spaert/Text-Analytics-System/blob/master/politics.py) / [entertainment.py](https://github.com/Spaert/Text-Analytics-System/blob/master/entertainment.py) we will get the title and the link of news like below image
![crawler result](https://github.com/Spaert/Text-Analytics-System/blob/master/result%20pic/1.PNG)

Also we put the data to Kafka message queue we can use [getpolitics.py](https://github.com/Spaert/Text-Analytics-System) / [getentertainment.py](https://github.com/Spaert/Text-Analytics-System/blob/master/getentertainment.py) to check the data which in the Kafka message queue

And then we use [Jeiba](https://github.com/fxsjy/jieba) to split the word and set up TF-IDF to compute the word similarity the result is in below image 
![word similarity result](https://github.com/Spaert/Text-Analytics-System/blob/master/result%20pic/2.PNG)

Final we use [cosine similarity from scikit-learn](http://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.cosine_similarity.html) to compare each news similarity 
![result](https://github.com/Spaert/Text-Analytics-System/blob/master/result%20pic/3.PNG)
