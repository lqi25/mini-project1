# mini-project1-Xiaoyu An
## twitter API
### Introduction
Use twitter api to use the Search API to find historical Tweets,and get only the Tweets that need by using advanced filtering tools with the realtime streaming API.
### Design Process
- Create a Twitter developer account and create an app.
- Get Twitter API and secret keys
- Get all tweets of @BBCWorld and store the info in JSON file.
- Use search function to get the latest 20 Twitter users who mentioned BBC NewS.
- Import package TwitterSearch and request user input a keyword.
- Using TwitterSearch package function to get 100 tweets which included BBC News and the keyword.
- Storing those 100 tweets in a txt file.   
### Testing 
Here is the result of performing the process that writing tweets to json file, get latest 20 user who mentioned BBC. And after input a keyword "Trump", save 100 tweets (BBC + Trump) to a txt file.
<img src="https://github.com/lqi25/mini-project1/blob/Xiaoyu_An/Screen%20Shot%202019-09-29%20at%209.06.11%20PM.png"/>   
Here is the txt file
<img src="https://github.com/lqi25/mini-project1/blob/Xiaoyu_An/Screen%20Shot%202019-09-29%20at%209.04.24%20PM.png"/>  


## Google API

### Design Process
- Setting the Google NLP API path
- Open the TwitterSearchOutput file(txt)
- Take advantage of the API's sentiment function to analyze the sentiment score and magnitude of each tweet line
- Using some math formula and calculation to get the average score toward the keyword in BBC news
- Calculate the precentage of people who has positive and negative attitude.


### Testing
Here is the sample output of sentiment anlaysis (keyword: 'Happy')
<img src="https://github.com/lqi25/mini-project1/blob/Xiaoyu_An/Screen%20Shot%202019-09-29%20at%209.09.15%20PM.png"/>  



