# GoogleAPI
## Introduction
Use google natural api to perform sentiment analysis on news obtained from Twitter, knowing the sentiment score of the news and whether people's attitude towards it is positive or negative. In addition, the input news can be classified and entity sentiment analysis.   
## Design Process
- Greate a project in GCP Console and enable the google natural language api.
- Create a service account and download the file of key.
- Set the GOOGLE_APPLICATION_CREDENTIALS in cmd using service account key.
- Upload news content from Twitter to Google Cloud.
- Use client.analyze_sentiment to analyze the sentiment of the news file.
- Classified according to the content of the news.
- Analyze the entity sentiment of the news.   
## Testing 
Here is the result of performing sentiment analysis on the twitter news file located in google cloud.We can see the sentiment score of each news and people's attitude towards it is positive, negative or neutral.
<img src="https://github.com/lqi25/mini-project1/blob/lqi/img/img1.jpg"/>   
Here is the result of analyzing the input news using google natural language api.We can see the category of the news, its sentiment score,people's attitude towards it and entity sentiment analysis.   
<img src="https://github.com/lqi25/mini-project1/blob/lqi/img/img2.jpg"/>   
