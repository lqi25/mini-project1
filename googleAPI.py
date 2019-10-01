from google.cloud import language_v1
from google.cloud.language_v1 import enums
import six

client = language_v1.LanguageServiceClient()
sum = 0
pos = 0
neg = 0
num = 0

with open('../api/TweetOutput.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:

        content = line

        if isinstance(content, six.binary_type):
            content = content.decode('utf-8')

        type_ = enums.Document.Type.PLAIN_TEXT
        document = {'type': type_, 'content': content}

        response = client.analyze_sentiment(document)
        sentiment = response.document_sentiment
        #print('Score: {}'.format(sentiment.score))
        #print('Magnitude: {}'.format(sentiment.magnitude))

        sum = sum + sentiment.score

        #print(sum)
        num += 1
        if sentiment.score >= 0.25:
            pos += 1
            #print (pos)
        if sentiment.score < 0.25:
            neg += 1
            #print (neg)

print ("the average attitude toward bbc and happy is ", sum/num)
print ("the people have positive attitude of BBC and Happy at the percent of ",100 * pos/num,"%")
print ("the people have negative attitude of BBC and Happy at the percent of ",100 * neg/num,"%")
