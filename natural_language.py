from google.cloud import language_v1
from google.cloud.language_v1 import enums
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
import six

def analyze_sentiment(gcs_content_uri):
    """
    Analyzing Sentiment in text file stored in Cloud Storage

    Args:
      gcs_content_uri Google Cloud Storage URI where the file content is located.
      e.g. gs://[Your Bucket]/[Path to File]
    """

    client = language_v1.LanguageServiceClient()

    # Available types: PLAIN_TEXT, HTML
    type_ = enums.Document.Type.PLAIN_TEXT

    language = "en"
    document = {"gcs_content_uri": gcs_content_uri, "type": type_, "language": language}

    encoding_type = enums.EncodingType.UTF8

    response = client.analyze_sentiment(document, encoding_type=encoding_type)

    # Get sentiment for all sentences in the document
    print(u"Get the sentiment score of each news:")
    for sentence in response.sentences:

        if sentence.sentiment.score > 0.25:
              print(u"Sentence text: {}".format(sentence.text.content))
              print(u"The attitude of this news is positive.")
              print(u"Sentence sentiment score: {}".format(sentence.sentiment.score))
              print(u"Sentence sentiment magnitude: {}".format(sentence.sentiment.magnitude))

        if sentence.sentiment.score <- 0.25:
              print(u"Sentence text: {}".format(sentence.text.content))
              print(u"The attitude of this news is negative.")
              print(u"Sentence sentiment score: {}".format(sentence.sentiment.score))
              print(u"Sentence sentiment magnitude: {}".format(sentence.sentiment.magnitude))

        if -0.25 <= sentence.sentiment.score <= 0.25:
              print(u"Sentence text: {}".format(sentence.text.content))
              print(u"The attitude of this news is neutral.")
              print(u"Sentence sentiment score: {}".format(sentence.sentiment.score))
              print(u"Sentence sentiment magnitude: {}".format(sentence.sentiment.magnitude))

def GoogleAPIResult(content):

    client = language.LanguageServiceClient()

    document = types.Document(
        content=content,
        type=enums.Document.Type.PLAIN_TEXT    )

    sentiment = client.analyze_sentiment(document=document).document_sentiment
    categories = client.classify_text(document).categories


    print('Content:{}'.format(content))

    for category in categories:
        print(u"The category of this news is:")
        print(u'{:<16}: {}'.format('name', category.name))
        print(u'{:<16}: {}'.format('confidence', category.confidence))

    if sentiment.score > 0.25:
        print('The attitude is positive and the score is :{}'.format(sentiment.score))
        print("")
    if sentiment.score < -0.25:
        print('The attitude is negative and the score is :{}'.format(sentiment.score))
        print("")
    if -0.25 <= sentiment.score <= 0.25:
        print('The attitude is neutral and the score is :{}'.format(sentiment.score))
        print("")
    
    encoding = enums.EncodingType.UTF32
    result = client.analyze_entity_sentiment(document, encoding)

    for entity in result.entities:
        print('Mentions: ')
        print(u'Name: "{}"'.format(entity.name))
        for mention in entity.mentions:
             print(u'Begin Offset : {}'.format(mention.text.begin_offset))
             print(u'Content : {}'.format(mention.text.content))
             print(u'Magnitude : {}'.format(mention.sentiment.magnitude))
             print(u'Sentiment : {}'.format(mention.sentiment.score))
             print(u'Type : {}'.format(mention.type))
        print(u'Salience: {}'.format(entity.salience))
        print("")


gcs_content_uri = 'gs://lqi25/SearchTweetOutput.txt'
analyze_sentiment(gcs_content_uri)
input_news = input("Please input the news:")
GoogleAPIResult(input_news)
