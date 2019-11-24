from flask import Flask, Markup
import pandas as pd
import numpy as np
import cufflinks as cf
from plotly.offline import download_plotlyjs, init_notebook_mode, plot,  iplot

app = Flask(__name__)

cf.go_offline()

@app.route('/')
def hello():
    # bar graph to show the entities from low to high sentiment (coloured by salience?)
# saved into a figure object using asFigure=True
    data = pd.read_csv(r'data/test_data.csv')

    figure = data[['entity_sentiment','entity_name','entity_salience']]\
        .sort_values('entity_sentiment').iplot(kind='bar',
                                                barmode='overlay',
                                                x='entity_name',
                                                xTitle='entity_sentiment',
                                                yTitle='score',
                                                title='Sentiment & Salience Distribution',
                                                asFigure=True)

    html = figure.to_html()
    return Markup(html)

if __name__ == '__main__':
    app.run()
