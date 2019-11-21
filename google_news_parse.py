import pandas as pd


def parse(json_data):
    """takes json response object from google news API and flattens into a dataframe"""
    all_parsed = []
    # for each article in request_data, normalises into dict
    for article in json_data.json()['articles']:
        parsed = {
            'source': article['source']['name'],
            'author': article['author'],
            'title': article['title'],
            'description': article['description'],
            'url': article['url'],
            'urlToImage': article['urlToImage'],
            'publishedAt': article['publishedAt'],
            'content': article['content']
        }
        # adds each dictionary into the list
        all_parsed.append(parsed)
    # converts into dataframe and returns
    return pd.DataFrame(all_parsed)


if __name__ == "__main__":
    import json

    with open('news.json', 'r') as f:
        data = json.load(f)

    print(parse(data))
