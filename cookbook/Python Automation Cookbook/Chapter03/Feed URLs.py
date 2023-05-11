import feedparser
import datetime
import delorean
import requests

rss = feedparser.parse('http://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml')
time_limit = delorean.parse(rss.feed.updated)-datetime.timedelta(hours=6)
entries = [entry for entry in rss.entries if delorean.parse(entry.published) > time_limit]
print(rss.feed.updated)
print(len(entries))
print(len(rss.entries))
print((entries[5]['title']))

print((entries[5]['link']))
print(requests.get(entries[5].link))
print(entries[6].keys())

