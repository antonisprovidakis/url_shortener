import sys, requests, json
from requests.exceptions import ConnectionError

# replace with your Google URL Shortener API_KEY
API_KEY = "some_API_Key"

class URLShortener:
    def __init__(self, api_key):
        self.API_KEY = api_key
        self.api_url = 'https://www.googleapis.com/urlshortener/v1/url'
        self.payload = {'key': self.API_KEY}
        self.headers = {'Content-Type': 'application/json'}

    def shorten(self, url):
        data = {'longUrl': url}
        short_url = ''

        try:
            r = requests.post(self.api_url, params = self.payload, headers = self.headers, data = json.dumps(data))
            short_url = r.json()['id'] + '\n'
        except ConnectionError as e:
            short_url = url
        
        return short_url

def main():
    url_shortener = URLShortener(API_KEY)

    # get filename from command line
    file_urls_name = sys.argv[1]
    short_file_urls_name = 'short_' + file_urls_name

    with open(file_urls_name, 'r') as infile, open(short_file_urls_name, 'w') as outfile:
        long_urls = infile.readlines()

        for line in long_urls:
            if line.strip(): # line is not empty
                outfile.write(url_shortener.shorten(line))            
            else: # line is empty
                outfile.write(line)
        
if __name__ == "__main__":
    sys.exit(int(main() or 0))