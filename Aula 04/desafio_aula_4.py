# -*- coding: utf-8 -*-
"""Desafio Aula 4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/11QadYO8xYpsLJQk3cj3GqBIpnjAoqNIk
"""

!pip install mplfinance

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import mplfinance as mpf
import yfinance as yf
import plotly.graph_objects as go
from plotly.subplots import make_subplots

dados = yf.download("AAPL", start="2023-01-01", end="2023-12-31")
mpf.plot(dados.head(100), type="candle", figsize = (16,8), volume=True, mav=(7,14,30), style='nightclouds', title="Ações da Apple")

