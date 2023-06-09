import requests
from bs4 import BeautifulSoup
import pprint

# look up regular expressions

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
        # return a list
        post = subtext[idx].select('.age')
        # return the string such as "5 days ago"
        post_age = post[0].get_text()
        # return an int of how many days such as 5
        post_age_i = int(post_age[0:post_age.find(' ')])

        if len(post) and post_age_i <= 4:
            joblist.append(
                {'title': title, 'link': href, 'post_age': post_age})

    return joblist


job_list = create_custom_joblist(links, subtext)
pprint.pprint(job_list)
