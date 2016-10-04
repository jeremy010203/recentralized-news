import requests

def get_random_page():
    try:
        url = 'http://en.wikipedia.org/wiki/Special:Random'
        req = requests.get(url)
        return req.text
    except:
        msg = "Failed to get page"
        print(msg)
        return msg
