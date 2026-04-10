# /stock/market-status?exchange=US
import requests
import json
import pandas as pd
from datetime import datetime, timezone
from finhub_api_key import api_key
from datetime import datetime
from term_image.image import from_url

companies = ['AAPL', 'XOM', 'TSLA', 'WMT', 'PFE', 'NFLX', 'JPM', 'CAT']


def get_news(ticker, dfrom, to):

    params = {
        'token': api_key,
        'symbol': ticker,
        'from': dfrom,
        'to': to
    }

    response = requests.get(
        url='https://finnhub.io/api/v1/company-news', params=params)

    return response.json()


def analyze_news(ticker):
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    news = get_news(ticker, now, now)

    # Предсказания

    return news


def get_ticker(inp):

    params = {
        'token': api_key,
        'q': inp,
        'exchange': 'US'
    }

    response = requests.get(
        url='https://finnhub.io/api/v1/search', params=params)

    return response.json()['result'][0]['symbol']


def display_image(url):

    image = from_url(url)

    return image


def get_info_by_ticker(ticker):
    params = {
        'token': api_key,
        'symbol': ticker
    }

    response = requests.get(
        url='https://finnhub.io/api/v1/stock/profile2', params=params)

    return response.json()['logo']


def main():
    ticker = get_ticker(
        input('Введите примерное название компание для получения анализа новостей: '))

    logo = get_info_by_ticker(ticker=ticker)

    image = display_image(logo)

    image.draw()

    news = analyze_news(ticker)

    print(news)


if __name__ == '__main__':
    main()
