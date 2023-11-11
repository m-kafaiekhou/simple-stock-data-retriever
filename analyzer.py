import yfinance as yf
import datetime


class Analyzer:
    def __init__(self, symbol, start_date=None, end_date=None):
        self.symbol = symbol
        self.start_date = start_date
        self.end_date = end_date
        self.data = None

    def set_dates(self):
        if self.start_date is None and self.end_date is None:
            today = datetime.date.today()
            one_year_ago = today - datetime.timedelta(days=365)
            self.start_date = one_year_ago.strftime('%Y-%m-%d')
            self.end_date = today.strftime('%Y-%m-%d')

        elif self.start_date is None:
            self.start_date = self.end_date - datetime.timedelta(days=365)

        elif self.end_date is None:
            self.end_date = datetime.date.today().strftime('%Y-%m-%d')

    def retrieve_data(self):
        self.data = yf.download(self.symbol, start=self.start_date, end=self.end_date)

    def add_candle_column(self):
        self.data["Candle"] = "Bullish"
        self.data.loc[self.data["Close"] < self.data["Open"], "Candle"] = "Bearish"

    def execute(self):
        self.set_dates()
        self.retrieve_data()
        self.add_candle_column()


if __name__ == "__main__":
    analyzer = Analyzer("AAPL")
    analyzer.execute()
    print(analyzer.data)
    