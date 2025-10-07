# UNCC Parking - Data Scraper in 3m intervals

import requests, json, csv, datetime, pandas, os

def fetch_stream():
    url = "https://parkingavailability.charlotte.edu/decks/stream"
    with requests.get(url, stream=True) as r:
        for line in r.iter_lines():
            if line:
                line = line.decode("utf-8")
                if line.startswith("data:"):
                    yield json.loads(line[len("data:"):])

def log_to_csv(data, filename="parking_data.csv"):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(filename, "a", newline="") as f:
        writer = csv.writer(f)
        for deck in data:
            writer.writerow([timestamp, deck["lotCode"], deck["name"], deck["percentAvailable"] * 100])

#MAIN METHOD
if __name__ == "__main__":
    last_logged = None
    for data in fetch_stream():
        now = datetime.datetime.now()
        if last_logged is None or (now - last_logged).total_seconds() >= 180:  #Time int in seconds (180 = 3 minutes)
            for deck in data:
                print(f"{deck['name']}: \t\t\t{deck['percentAvailable']*100:.1f}% available")
            log_to_csv(data)
            print(f"\nData fetched at: {now.strftime('%Y-%m-%d %H:%M:%S')}\n")
            last_logged = now