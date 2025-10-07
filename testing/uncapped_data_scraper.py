# UNCC Parking - Data Scraper in 10s intervals
# MAY PROVIDE TOO MANY DATAPOINTS

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
    for data in fetch_stream():
        # print(json.dumps(data, indent=2))
        for deck in data:
            print(f"{deck['name']}: \t\t\t{deck['percentAvailable']*100:.1f}% available")
        log_to_csv(data)
        print(f"\nData fetched at: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

    
    


    
        # PRINT IN PLAIN TEXT FOR DEBUGGING
        # for deck in data:
        #     print(f"{deck['name']}: {deck['percentAvailable']*100:.1f}% available")
        # print(f"\nData fetched at: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    