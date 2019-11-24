from flask import Flask, Markup, render_template
import pandas as pd
import numpy as np
import cufflinks as cf
from plotly.offline import download_plotlyjs, init_notebook_mode, plot,  iplot

app = Flask(__name__)

cf.go_offline()

@app.route('/')
def index():
    data = pd.read_csv(r'data/rugby_sentiment_data.csv')

    figure_1 = data[['entity_sentiment','entity_name','entity_salience']]\
        .sort_values('entity_sentiment').iplot(kind='bar',
                                                barmode='overlay',
                                                x='entity_name',
                                                xTitle='entity_sentiment',
                                                yTitle='score',
                                                title='Sentiment & Salience Distribution',
                                                asFigure=True).to_html()

    figure_2 = data.iplot(
                            x='entity_sentiment',
                            y='entity_salience',
                            categories='entity_type',
                            xTitle='entity_sentiment',
                            yTitle='entity_salience',
                            title='Salience Vs Sentiment by Entity Type',
                            asFigure=True
                        ).to_html()

    charts = [figure_1, figure_2]
    return render_template('index.html', charts=charts)

if __name__ == '__main__':
    app.run()
