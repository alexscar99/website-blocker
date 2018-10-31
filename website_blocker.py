import time
from datetime import datetime as dt

hosts_path = '/etc/hosts'
redirect = '127.0.0.1'

# websites to block (using social sites as examples)
website_list = [
    'www.youtube.com', 'youtube.com', 'www.reddit.com', 'reddit.com',
    'www.facebook.com', 'facebook.com', 'www.twitter.com', 'twitter.com',
    'www.instagram.com', 'instagram.com'
]

# loop running every 5 sec to check if current time is during the work day (9am-5pm)
while True:
    if dt(dt.now().year,
          dt.now().month,
          dt.now().day, 9) < dt.now() < dt(dt.now().year,
                                           dt.now().month,
                                           dt.now().day, 17):
        # open hosts file, append redirect and website URL if not already there
        with open(hosts_path, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + ' ' + website + '\n')
        print('Working hours...go be productive!')
    else:
        # open hosts file, store list of each line, move pointer to beginning
        with open(hosts_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            # write each line only if it doesn't contain any of the website URLs
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            # remove everything after pointer's location to avoid duplication
            file.truncate()
        print('Free time...visit any site you would like!')

    time.sleep(5)
