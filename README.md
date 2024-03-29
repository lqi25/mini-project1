
# mini-project1   

Hello, this is miniproject1 of EC 601. In this project, we use Twitter API and Google natural language API to access Tweets related to BBC new and analyze the attitude toward it.

Authors
- Xiaoyu An
- Luxuan Qi

## Product Mission:
Twitter has a variety of news accounts, such as People's Daily, China, BBC News (World), and The New York Times. In these news accounts, we can easily get information from business, politics, sports and other fields around the world. The target users of our API is news readers and editors.Through our API, they can get the news recently,and readers'attitudes towards them. They can also classify and get keywords of the news.   

### User Stories:  
- I,a news reader,should be able to get news instantly.
- I,a news reader,should be able to store news from twitter in a file.
- I,a news reader,should know the category and keywords of the news.
- I,a news reader,should be able to input a news item and analyze it.
- I,a news editor,need to know whether people's attitudes towards a news item are positive or negative.
- I,a news editor,need to know people's overall attitude towards all the news obtained from twitter.   

### MVP
The minimum viable product of our project is to get the latest news from Twitter and analyze whether people’s attitudes toward these news are positive or negative.

### User Interface Design
We use twitter api to gain the news from twitter news account,for example,the BBC News account.Then, we use google natural language api to analyze the sentiment score of each and overall news, and get people's attitude towards them.

## Architecture
<img src="https://github.com/lqi25/mini-project1/blob/master/img/Screen%20Shot%202019-09-29%20at%208.51.02%20PM.png"/> 

## Design Progress
### Xiaoyu's part
1. Install Python 3.6+, corresponding pip
2. Clone this repository using:
   ```
   git clone https://github.com/lqi25/mini-project1/blob/master/README.md
   ```
   or download a zip file of the repository by clicking the download zip button at top right.
<img src="https://github.com/lqi25/mini-project1/blob/master/img/githubclone.png"/> 



3. Navigate to the project folder by running "
      ```
      cd WorkingTitle
      ```
      Then paste the key.json file that containing api keys in this folder and also paste the twitter api keys in the combine.py file at the appropiate places. Also need to install all the package that required.
 <img src="https://github.com/lqi25/mini-project1/blob/master/img/twitterkey1.png"/> 
 
 
 
4. In the terminal,type 
      ```
      python combine.py
      ```
      The script will get the latest 20 users. Then users need to input a keyword that they interested in. 
      
      <img src="https://github.com/lqi25/mini-project1/blob/master/img/twitterouput.png"/> 
      
      Then will generate a text files called TweetOutput.txt, which containing 100 tweets that include BBC news and the keyword.
      
     <img src="https://github.com/lqi25/mini-project1/blob/master/img/txt.png"/> 
     
     
5. Next type 
      ```
      python googleAPI.py
      ```
      The script will generate the sentiment scores for the tweets in the text file TweetOutput.txt. This part contain a overall attitude and the precentage of positive & negative attitude.
      
 <img src="https://github.com/lqi25/mini-project1/blob/master/img/googleoutput.png"/> 
 
### Luxuan Qi's part
Use google natural api to perform sentiment analysis on news obtained from Twitter, knowing the sentiment score of the news and whether people's attitude towards it is positive or negative. In addition, the input news can be classified and entity sentiment analysis.  
     
     
1.How it works   
- Greate a project in GCP Console and enable the google natural language api.
- Create a service account and download the file of key.
- Set the GOOGLE_APPLICATION_CREDENTIALS in cmd using service account key.
- Upload news content from Twitter to Google Cloud.
- Use client.analyze_sentiment to analyze the sentiment of the news file.
- Classified according to the content of the news.
- Analyze the entity sentiment of the news.   
 
    
2.Testing      
Here is the result of performing sentiment analysis on the twitter news file located in google cloud.We can see the sentiment score of each news and people's attitude towards it is positive, negative or neutral.
<img src="https://github.com/lqi25/mini-project1/blob/lqi/img/img1.jpg"/>
   
Here is the result of analyzing the input news using google natural language api.We can see the category of the news, its sentiment score,people's attitude towards it and entity sentiment analysis.   
<img src="https://github.com/lqi25/mini-project1/blob/lqi/img/img2.jpg"/>  

## Personal learning

### Xiaoyu's part

- Building software is not easy. I always run into errors. Usually write code only require a few minutes but debug need a few hours :) so consistance is really necessary. 
- For the twitter part, there are many libraries which Twitter provided that support the standard Twitter API. I prefer TwitterSearch for its multifunction and convenience. But my filtering process of twitter messages is too simple. There is an large amount of spam and useless data, so having a more in depth filtering process would be better. 
- For the google part, the guidances and documents is more, and easy to follow. I would like to continue learning more about NLP. 
- In this project I used PYCHARM and it sometimes got stuck. Next time I may use a better compiler. And also allocated more time to realize some other goals, e.g. develop a user interface and build a database integration to store historical data. This is my first time to do API programming. Next time I will aviod coding directly without learn more about API and relative knowledge. 

### Luxuan Qi's part
- I like the process of learning new things. Following the tutorial on google natural language api, I successfully analyzed the sentiment score of twitter news and people's attitude towards news, which made me very excited.   
- I think I should look at the tutorial better and try to implement more features in my project.   
- When setting the environment variable, I set the environment variable in the google shell cloud, which is actually not working, so I have been unable to successfully call google natural language api. When configuring the environment of the project, I should study the tutorial and ask for help from others when there is a problem, so that I can configure the environment as soon as possible.Therefore I can learn and design the next step.



