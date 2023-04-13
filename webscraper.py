import requests
from bs4 import BeautifulSoup
import pprint

website = requests.get('https://news.ycombinator.com/jobs', timeout=10)
soup = BeautifulSoup(website.text, 'html.parser')
links = soup.select('.titleline > a')
subtext = soup.select('.subtext')

def sort_jobs_by_age(jobslist):
    return sorted(jobslist, key=lambda k: k['age'], reverse=True)

def create_custom_joblist(links, subtext):
    joblist = []
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        post = subtext[idx].select('.age')
        if len(post):
            points = str(post[0].getText())
            joblist.append({'title': title, 'link': href, 'post': points})
    return joblist


pprint.pprint(create_custom_joblist(links, subtext))

