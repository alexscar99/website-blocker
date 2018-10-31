import time
from datetime import datetime as dt

hosts_path = "/etc/hosts"
redirect = "127.0.0.1"

# websites to block (using social sites as examples)
website_list = [
    "www.youtube.com", "youtube.com", "www.reddit.com", "reddit.com",
    "www.facebook.com", "facebook.com", "www.twitter.com", "twitter.com",
    "www.instagram.com", "instagram.com"
]

# infinite loop checking if the current time is within the work day (9am-5pm)
while True:
    if dt(dt.now().year,
          dt.now().month,
          dt.now().day, 9) < dt.now() < dt(dt.now().year,
                                           dt.now().month,
                                           dt.now().day, 17):
        print("Working hours...go be productive!")
    else:
        print("Free time...visit any site you'd like!")

    # set interval between running above conditional to check time
    time.sleep(5)
