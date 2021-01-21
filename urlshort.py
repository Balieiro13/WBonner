import bitly_api

TOKEN = ''

access = bitly_api.Connection(access_token = TOKEN)

def shorturl(url):
    return access.shorten(url)

a = shorturl('https://www.google.com')
print(a)
