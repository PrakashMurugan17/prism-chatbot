import feedparser
import json
import re
with open('toi_feed_links.json', 'r') as myfile:
        data = myfile.read()
feed_links = json.loads(data)


def news(command):
   
    for a in feed_links.keys():
        if a in command:
            type = a      
    NewsFeed = feedparser.parse(feed_links[type])
    if len(NewsFeed.entries)==0:
        msg = "Sorry, couldn't find any entries."
        return msg 
        
        
    else:
        found =  "Found " + str(len(NewsFeed.entries)) + " entries\n"
        return found
            
    