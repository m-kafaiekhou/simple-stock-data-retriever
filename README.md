# Simple stock data retriever

## Description
This project is a simple implementation of Pandas data analysis with yfinance. The project uses the yfinance package to retrieve historical data for a given stock symbol and time period. The retrieved data is then analyzed using Pandas to add a new column called "Candle" that indicates whether the candle is bullish or bearish.


## Installation
To run this project, just simply clone the repo and run the following command:

```bash
pip install -r requirements.txt
```
## Usage
To use this project, simply create an instance of the Analyzer class with the symbol you want to analyze, and call the execute() method on it. The execute() method will set the dates, retrieve the data, and add the "Candle" column
all the data will be stored in the data attribute of the Analyzer class.

```python
analyzer = Analyzer("AAPL") # you can also give the dates manually
analyzer.execute()
print(analyzer.data)
```
