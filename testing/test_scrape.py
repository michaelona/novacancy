import requests

url = "https://parkingavailability.charlotte.edu/decks/stream"
with requests.get(url, stream=True) as r:
    for line in r.iter_lines():
        if line:
            print(line.decode("utf-8"))
