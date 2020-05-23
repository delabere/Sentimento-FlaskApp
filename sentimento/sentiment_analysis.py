from google.cloud import language_v1
from google.cloud.language_v1 import enums
import pandas as pd
import os


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'credentials.json'

client = language_v1.LanguageServiceClient()
# Available types: PLAIN_TEXT, HTML
type_ = enums.Document.Type.PLAIN_TEXT
language = "en"
encoding_type = enums.EncodingType.UTF8


def sample_analyze_entity_sentiment(text_content, unique_id):
    """
    Analyzing Entity Sentiment in a String

    Args:
      text_content The text content to analyze
      id The unique id to tie back to the source data
    """

    entity_data = []
    document = {"content": text_content, "type": type_, "language": language}
    response = client.analyze_entity_sentiment(document, encoding_type=encoding_type)

    # Loop through entities returned from the API
    for entity in response.entities:
        current_entity = {'id': unique_id, 'entity_name': entity.name, 'entity_type': enums.Entity.Type(entity.type).name,
                          'entity_salience': entity.salience, 'entity_sentiment': entity.sentiment.score}
        entity_data.append(current_entity)

    return entity_data


# read source data and create list of tuples to pass into sentiment function
source_data = pd.read_csv(r'data/rugby_data.csv')
zipped_data = zip(source_data['url'], source_data['description'])

# loop through each url/description and append results to csv
index = 0
for unique_id, description in zipped_data:
    index += 1
    try:
        entity_data =  pd.DataFrame(sample_analyze_entity_sentiment(description, unique_id))
        print(f'{index} / {len(source_data)}')
        if not os.path.exists(r'data/rugby_sentiment_data.csv'):
            entity_data.to_csv(r'data/rugby_sentiment_data.csv', index=False)

        entity_data.to_csv(r'data/rugby_sentiment_data.csv', mode='a', header=False ,index=False)
    except:
        pass