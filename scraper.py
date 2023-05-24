import requests
from bs4 import BeautifulSoup
import json

# URL to be scraped
url = 'https://en.wikipedia.org/wiki/History_of_Mexico'

def get_citations_needed_count(url):
    """this count the number of citations needed in the page and return the number """
    # Get the page content
    page = requests.get(url)
    # Parse the content
    soup = BeautifulSoup(page.content, 'html.parser')
    # Find all the <sup> tags
    citations = soup.find_all('a', title="Wikipedia:Citation needed")
    # Return the length of the list
    return len(citations)

def get_citations_needed_report(url):
    """
    This function will return a string
    """
    # Get the page content
    page = requests.get(url)
    # Parse the content
    soup = BeautifulSoup(page.content, 'html.parser')
    # Find all the <sup> tags
    sup_tags = soup.find_all('p')
    # Create an empty string
    paragraph = ''
    for tag in sup_tags:
        if tag.find('a', title="Wikipedia:Citation needed"):
            paragraph += tag.text.strip() + '\n \n'
    return paragraph

if __name__ == "__main__":
    print(get_citations_needed_count(url))
    print(get_citations_needed_report(url))
    