# **** represents YOUR OWN API code, key ...etc

### Market News and Stock Price Difference Checker

This Python script utilizes the News API and Alpha Vantage to fetch recent news and analyze stock price changes for a specified company.

#### Features:

- **Company**: Tesla Inc (TSLA)
- **Date**: Previous Trading Day
- **Functionality**:
  - Retrieves latest news related to Tesla Inc from the News API.
  - Calculates the percentage change in Tesla's stock price between the previous two trading days using Alpha Vantage.
  - Displays the stock symbol, company name, date of analysis, and the percentage change in stock price with a directional emoji (🔺 or 🔻).
  - Outputs the latest headline, description, source, author, and published date of the top news article.

#### How It Works:

1. **News API Integration**: Fetches news articles related to "Tesla Inc" from the day before yesterday to yesterday.
2. **Alpha Vantage Integration**: Retrieves daily stock data for "TSLA" and calculates the percentage change in closing prices between the two most recent trading days.
3. **Display**: Prints out a formatted summary including the stock symbol, company name, date, stock price difference with a percentage change, and details of the latest news article.

#### Example Output:


Certainly! Here's a fancy explanation of the provided code snippet for your readme.md file in a notepad format:

markdown
Copy code
# **** represents YOUR OWN API code, key ...etc

### Market News and Stock Price Difference Checker

This Python script utilizes the News API and Alpha Vantage to fetch recent news and analyze stock price changes for a specified company.

#### Features:

- **Company**: Tesla Inc (TSLA)
- **Date**: Previous Trading Day
- **Functionality**:
  - Retrieves latest news related to Tesla Inc from the News API.
  - Calculates the percentage change in Tesla's stock price between the previous two trading days using Alpha Vantage.
  - Displays the stock symbol, company name, date of analysis, and the percentage change in stock price with a directional emoji (🔺 or 🔻).
  - Outputs the latest headline, description, source, author, and published date of the top news article.

#### How It Works:

1. **News API Integration**: Fetches news articles related to "Tesla Inc" from the day before yesterday to yesterday.
2. **Alpha Vantage Integration**: Retrieves daily stock data for "TSLA" and calculates the percentage change in closing prices between the two most recent trading days.
3. **Display**: Prints out a formatted summary including the stock symbol, company name, date, stock price difference with a percentage change, and details of the latest news article.

#### Example Output:

STOCK: TSLA
COMPANY: Tesla Inc
DATE: 2023-06-12
STOCK PRICE DIFFERENCE: 🔺 1.5%
Title: Tesla's New Innovation Boosts Stock Market
Description: Tesla's latest product launch has stirred positive market sentiment.
From: Financial Times --uploaded by--> John Doe -at-> 2023-06-12T10:30:00Z


#### Requirements:

- **Python Libraries**: `requests`, `datetime`, `newsapi`
- **API Keys**: Replace `"****"` with your own News API and Alpha Vantage API keys.

#### Usage:

- Ensure Python is installed.
- Replace `"****"` in the code with your valid API keys.
- Run the script to get the latest stock price change and news for Tesla Inc.

This script is designed to provide quick insights into recent developments affecting Tesla's stock performance, ideal for financial analysis or news monitoring applications.

