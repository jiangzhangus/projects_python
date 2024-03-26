import requests

cached = {}

def get_from_web(url):
    response = requests.get(url)
    return response.text

def get_content(url):
    if url not in cached:
        print("saving url into cache")
        cached[url] = get_from_web(url)
    return cached[url]

if __name__ == "__main__":
    url = "https://www.google.com"
    print(get_content(url))
