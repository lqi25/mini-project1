
# mini-project1   

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

# Architecture
<img src="https://github.com/lqi25/mini-project1/blob/master/Screen%20Shot%202019-09-29%20at%208.51.02%20PM.png"/> 

# Installation Instructions
1. Install Python 3.6+, corresponding pip
2. Clone this repository using:
   ```
   git clone https://github.com/lqi25/mini-project1/blob/master/README.md
   ```
   or download a zip file of the repository by clicking the download zip button at top right.
<img src="https://github.com/lqi25/mini-project1/blob/master/githubclone.png"/> 



3. Navigate to the project folder by running "
      ```
      cd WorkingTitle
      ```
      Then paste the key.json file that containing api keys in this folder and also paste the twitter api keys in the combine.py file at the appropiate places. Also need to install all the package that required.
 <img src="https://github.com/lqi25/mini-project1/blob/master/twitterkey.png"/> 
 
 
 
4. In the terminal,type 
      ```
      python combine.py
      ```
      The script will get the latest 20 users. Then users need to input a keyword that they interested in. 
      
      <img src="https://github.com/lqi25/mini-project1/blob/master/twitterouput.png"/> 
      
      Then will generate a text files called TweetOutput.txt, which containing 100 tweets that include BBC news and the keyword.
       <img src="https://github.com/lqi25/mini-project1/blob/master/txt.png"/> 
     
     
5. Next type 
      ```
      python googleAPI.py
      ```
      The script will generate the sentiment scores for the tweets in the text file TweetOutput.txt. This part contain a overall attitude and the precentage of positive & negative attitude.
      
 <img src="https://github.com/lqi25/mini-project1/blob/master/googleoutput.png"/> 
          






