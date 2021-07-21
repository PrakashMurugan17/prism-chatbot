import find
from find import NewsFeed

for i in range(len(NewsFeed.entries)):
        entry = NewsFeed.entries[i]
        msg = entry.title
        if i == len(NewsFeed.entries) - 1:
            msg = "Do you want to know more?"
        else:
            msg = "Do you want to know more or go to the next topic or stop?"
            
        command_news = give_sec_command()
        if "more" in command_news:
            if re.sub('<[^>]*>', '', entry.summary)!="":
                msg = (re.sub('<[^>]*>', '', entry.summary)) 
                msg = ("Next in line, ")        
            else:
                msg = ("Could't find sumamry.")
        elif "next" in command_news:
            continue
        elif "stop" or "no" in command_news:
            msg = ("Okay!")
            break