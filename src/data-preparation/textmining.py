import pandas as pd
from textblob import TextBlob
import os

data = pd.read_csv('../../gen/data-preparation/temp/parsed-data-event.csv', sep = '\t')
data_2 = pd.read_csv('../../gen/data-preparation/temp/parsed-data-eventbef.csv', sep = '\t')
data_3 = pd.read_csv('../../gen/data-preparation/temp/parsed-data-eventaf.csv', sep = '\t')
data.head()


for i, j in data.iterrows():
    print(i)
    try:
        blob = TextBlob(j['text'])
        data.loc[i, 'polarity'] = blob.sentiment.polarity
        data.loc[i, 'subjectivity'] = blob.sentiment.subjectivity
    except:
        data.loc[i, 'polarity'] = ''
        data.loc[i, 'subjectivity'] = ''

data.head()

data_2.head()


for i, j in data_2.iterrows():
    print(i)
    try:
        blob = TextBlob(j['text'])
        data_2.loc[i, 'polarity'] = blob.sentiment.polarity
        data_2.loc[i, 'subjectivity'] = blob.sentiment.subjectivity
    except:
        data_2.loc[i, 'polarity'] = ''
        data_2.loc[i, 'subjectivity'] = ''

data_2.head()

data_3.head()


for i, j in data_3.iterrows():
    print(i)
    try:
        blob = TextBlob(j['text'])
        data_3.loc[i, 'polarity'] = blob.sentiment.polarity
        data_3.loc[i, 'subjectivity'] = blob.sentiment.subjectivity
    except:
        data_3.loc[i, 'polarity'] = ''
        data_3.loc[i, 'subjectivity'] = ''

data_3.head()

os.makedirs('../../gen/data-preparation/output/', exist_ok=True)

data.to_csv('../../gen/data-preparation/output/dataset-event.csv', index = False)
data_2.to_csv('../../gen/data-preparation/output/dataset-bef.csv', index = False)
data_3.to_csv('../../gen/data-preparation/output/dataset-after.csv', index = False)

print('done.')
