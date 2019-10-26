from google.cloud import language_v1
from google.cloud.language_v1 import enums
import pandas as pd
import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'credentials.json'

def sample_analyze_entity_sentiment(text_content):
    """
    Analyzing Entity Sentiment in a String

    Args:
      text_content The text content to analyze
    """

    entity_data = []

    client = language_v1.LanguageServiceClient()

    # text_content = 'Grapes are good. Bananas are bad.'

    # Available types: PLAIN_TEXT, HTML
    type_ = enums.Document.Type.PLAIN_TEXT

    # Optional. If not specified, the language is automatically detected.
    # For list of supported languages:
    # https://cloud.google.com/natural-language/docs/languages
    language = "en"
    document = {"content": text_content, "type": type_, "language": language}

    # Available values: NONE, UTF8, UTF16, UTF32
    encoding_type = enums.EncodingType.UTF8

    response = client.analyze_entity_sentiment(document, encoding_type=encoding_type)
    # Loop through entities returned from the API
    for entity in response.entities:
        current_entity = {'entity_name': entity.name, 'entity_type': enums.Entity.Type(entity.type).name,
                          'entity_salience': entity.salience, 'entity_sentiment': entity.sentiment.score}
        entity_data.append(current_entity)
    return entity_data


text_content = '''
England had stormed into a 10-0 lead, Manu Tuilagi's second-minute try and a long-range penalty from George Ford fitting reward for a blistering first half.

The 2003 winners could have been out of sight had tries for Sam Underhill and Ben Youngs not been ruled out by the video referee, but when Ardie Savea pounced on a wayward line-out throw to reduce the deficit to 13-7 the three-time world champions were on the charge.

Yet the superb Ford landed a trio of nerveless penalties and with the young dynamos Underhill and Tom Curry outstanding in the back row England held on in style to pull off one of their greatest victories.

The All Blacks had not lost a World Cup game in 12 years and had won 15 of the past 16 games between the two nations.

But four years after crashing out at the group stage England tore the crown from their head with a performance of unremitting energy and excellence on a night for the ages in Yokohama.
'''

entity_data = sample_analyze_entity_sentiment(text_content)
entity_dataframe = pd.DataFrame(entity_data)

entity_dataframe.to_csv('test_data.csv')