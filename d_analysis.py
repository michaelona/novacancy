# d_analysis.py
# Show CSV data as graph for selected / all decks


import pandas as pd
import matplotlib.pyplot as plt



# Load CSV
def load_data(filename = "parking_data.csv"):
    """
    Reads the CSV into a pandas DataFrame 
    and converts the timestamp col to datetime obj.
    """
    df = pd.read_csv(filename,names=["timestamp", "lotCode","name","percentAvailable"]) # Assign col names
    df["timestamp"] = pd.to_datetime(df["timestamp"]) # Convert TIMESTAMP col to datetime pandas object
    return df

# 3 Filter specific deck
def filter_deck(df, lot_code):
    """
    Filters DataFrame to only include rows for the given deck code.
    """
    return df[df["lotCode"] == lot_code]


# 4 Normalize time series
def resample_deck(df, interval="5min"):
    """
    Resamples the deck DataFrame into regular time intervals.
    '5min' = 5 minutes. This averages multiple samples in the same interval.
    """
    df = df.set_index("timestamp")
    df_resampled = df.resample(interval).mean(numeric_only=True)
    return df_resampled



# 5 Plot selected decks (all if empty)
def plot_sel_decks(df, interval="5min", show_full=False, lot_codes=None):
    """
    Plots all decks or only the specified ones on the same chart.
    lot_codes: list of deck codes (e.g. ["CD FS", "ED2/3"])
    """
    plt.figure(figsize=(14,7))
    
    groups = df.groupby("lotCode")
    for lot_code, deck_group in groups:
        if lot_codes is not None and lot_code not in lot_codes:
            continue  # skip decks not in the list
        deck_name = deck_group["name"].iloc[0]
        deck_resampled = deck_group.set_index("timestamp").resample(interval).mean(numeric_only=True)
        if show_full:
            y = 100 - deck_resampled["percentAvailable"]
        else:
            y = deck_resampled["percentAvailable"]
        plt.plot(deck_resampled.index, y, marker="o", label=deck_name)
    
    plt.title("Parking Decks Availability Over Time" if not show_full else "Parking Decks Occupancy Over Time")
    plt.xlabel("Time")
    plt.ylabel("Percent Full" if show_full else "Percent Available")
    plt.ylim(0,100)
    plt.grid(True)
    plt.legend()
    plt.show()


# Runner
if __name__ == "__main__":
    df = load_data()
    
    deck_code = "ED2/3"     # Example: pick one deck to explore (works with plot_deck)
    deck_df = filter_deck(df, deck_code)
    
    deck_resampled = resample_deck(deck_df)
    
    # plot_deck(deck_resampled, deck_name=deck_df["name"].iloc[0], show_full=True)

    plot_sel_decks(df, interval = "5min",show_full=True, lot_codes=["WEST", "ED2/3", "UDL"])  # Show selected 5 min int
    plot_sel_decks(df, show_full=True, lot_codes=["WEST", "ED2/3", "UDL"])  # Show selected 3 min int
    plot_sel_decks(df, show_full=True)                                      # Show all
