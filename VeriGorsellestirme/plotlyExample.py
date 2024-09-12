# -*- coding: utf-8 -*-
"""
Plotly Library ->https://plotly.com/python/
"""
#python cheat example ->python get started 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import chart_studio.plotly as py
from plotly.offline import init_notebook_mode,iplot
import plotly.graph_objs as go

from wordcloud import wordCloud

times_data=pd.read_csv("timesData.csv")

#prepare dataFrame
df=times_data.iloc[:100,:]
trace1=go.Scatter(
    x=df.word_rank,
    y=df.citations,
    mode="lines",#type of plot like marker,line or line+marker
    name="citiation",#name of the plot
    marker=dict(color='rgba(16,112,2,0.8)'),#renk belirlemek için 0.8 de alpha değeri
    text=df.university_name#graph üzerine gelince yazılacak yazı
    )
#creating trace2
trace2=go.Scatter(
    x=df.word_rank,
    y=df.teaching,
    mode="lines+markers",#type of plot like marker,line or line+marker
    name="teaching",#name of the plot
    marker=dict(color='rgba(80,26,80,0.8)'),#renk belirlemek için 0.8 de alpha değeri
    text=df.university_name#graph üzerine gelince yazılacak yazı
    )
data=[trace1,trace2]
layout=dict(title='Citation and teaching vs world rank of top 100 universities',
            xaxis=dict(title='world rank ',ticklen=5,zeroline=False))
fig=dict(data=data,layout=layout)
iplot(fig)


