import requests


def fetch_fno():
    headers = {"User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0"}
    session = requests.Session()
    url = "https://www.nseindia.com/api/equity-stockIndices?index=SECURITIES%20IN%20F%26O"
    session.get("https://www.nseindia.com/", headers=headers)
    data = session.get(url, headers=headers).json()["data"]
    symbols = []
    for row in data:
        symbols.append(row['symbol'])
    symbols.sort()
    return symbols
