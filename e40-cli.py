import pandas as pd

csv_path = "e40-lyrics.csv"

def find_item(item, df):
    relevant_rows = df[df['food'].str.startswith(item)]

    for index, entry in relevant_rows.iterrows():
    # for entry in relevant_rows.rows:
        song_title = entry["song"]
        album = entry["album"]
        bar = entry["lyric"]
        print(f"From {song_title} on album {album}:")
        print(f"\t{bar}\n")

    # for row in df[df['food'].str.contains(item)]:
    #     print(row)

def parse_csv(filepath):
    df = pd.read_csv(filepath)
    lyrics_data = df[df.columns[0:6]]
    print(lyrics_data.head())
    print("\n")
    return lyrics_data

def main(search_term):
    print(f"Searching for lyrics with \"{search_term}\"...\n")
    lyrics_data = parse_csv(csv_path)
    find_item(search_term, lyrics_data)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser("searches for terms in e40 lyrics")
    parser.add_argument("--item", help="item to search for", type=str, default="tomato")
    args = parser.parse_args()

    main(args.item)
