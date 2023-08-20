import http.client, urllib.parse
import json
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from textblob import TextBlob


conn = http.client.HTTPSConnection('api.thenewsapi.com')

params = urllib.parse.urlencode({
    'api_token': 'nTC9M0SEjJHgmD091x4ShQmE0Ij5mKiCIVYc1sET',
    'categories': 'business,tech',
    'limit': 3,
    'language': 'en',
    })

conn.request('GET', '/v1/news/all?{}'.format(params))

res = conn.getresponse()
data = res.read()
data_json = json.loads(data.decode('utf-8'))


titles = [article['title'] for article in data_json['data']]

print(titles) 

positive_titles = [title for title in titles if TextBlob(title).sentiment.polarity > 0]

print(positive_titles) 
