import requests
import datetime
import config
from twilio.rest import Client

# CONSTANT
STOCK_API = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY"
KEY_STOCKS = "IFEB19AS7U9G3J8L"
KEY_NEWS = "31d30ece64ca4756b3185d09723c3529"
company_name = "Microsoft"
stock = "MSFT"
stock_params = {
    'symbol': stock,
    'apikey': KEY_STOCKS
}
time_yesterday = datetime.datetime.today()-datetime.timedelta(days=1)
time_before_yesterday = datetime.datetime.today()-datetime.timedelta(days=7)
time_yesterday = time_yesterday.strftime("%Y-%m-%d")
time_before_yesterday = time_before_yesterday.strftime("%Y-%m-%d")


# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
response = requests.get(STOCK_API, params=stock_params)
data = response.json()
stock_before_yesterday = data["Time Series (Daily)"][time_before_yesterday]
stock_yesterday = data["Time Series (Daily)"][time_yesterday]
percentage = round((float(stock_yesterday['4. close'])-float(
    stock_before_yesterday['4. close']))/float(stock_before_yesterday['4. close']), 2)
percentage = percentage*100
# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
print(percentage)
if percentage >= 5 or percentage <= -5:
    reponse_news = requests.get(
        f'https://newsapi.org/v2/everything?q={company_name}&apiKey={KEY_NEWS}')
    data_news = reponse_news.json()
    news = data_news["articles"]

    account_sid = config.TWILIO_ACCOUNT_SID
    auth_token = config.TWILIO_AUTH_TOKEN
    for new_information in range(3):
        client = Client(account_sid, auth_token)
        if percentage > 5:
            message = client.messages \
                            .create(
                                body=f"{stock}:🔺{percentage}%\n{news[new_information]['title']}\n{news[new_information]['description']}",
                                from_='+15344003793',
                                to='+51977115116'
                            )
        else:
            message = client.messages \
                            .create(
                                body=f"{stock}:🔻{percentage}%\n{news[new_information]['title']}\n{news[new_information]['description']}",
                                from_='+15344003793',
                                to='+51977115116'
                            )
# STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
