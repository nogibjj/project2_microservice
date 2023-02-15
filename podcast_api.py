import requests

# Define the search query (podcast channel name)

def search(query):
    # Send a request to the iTunes API to search for podcasts
    response = requests.get(f"https://itunes.apple.com/search?entity=podcast&term={query}")

    # Check if the request was successful
    if response.status_code != 200:
        print("Error: Request failed")
        exit()

    # Parse the JSON response and extract podcast data
    results = response.json()["results"]
    for result in results:
        print(f"Podcast Name: {result['collectionName']}")
        print(f"Podcast Author: {result['artistName']}")
        print(f"Podcast URL: {result['collectionViewUrl']}")
        print()


    # Download the podcast episode from the channel based on date in mp4 format
    response = requests.get(f"https://podcasts.apple.com/us/podcast/morning-taiwan-glocal-news/id1530000000?i=1000500000000", stream=True)
    with open("episode.mp4", "wb") as file:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                file.write(chunk.content)

if __name__ == "__main__":
    search(query = "morning-taiwan-glocal-news")