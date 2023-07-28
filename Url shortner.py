import pyshorteners

# Initialize the shortener
shortener = pyshorteners.Shortener()

# Shorten a URL
url = 'https://www.instagram.com/inbox'
short_url = shortener.tinyurl.short(url)

# Print the shortened URL
print(short_url)
