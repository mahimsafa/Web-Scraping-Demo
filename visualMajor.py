from bs4 import BeautifulSoup
import csv
from selenium import webdriver
import visualMinor
from visualMinor import postWriter, postLink

driver = webdriver.Chrome('/opt/google/chrome/chromedriver')


with open('result.csv', 'w', newline='') as f:
        thewriter = csv.writer(f)
        thewriter.writerow(['Title', 'Date', 'Author', 'Link'])

def resultWriter(title=None, date=None, author=None, link=None):
    with open('result.csv', 'a', newline='') as f:
        fieldnames = ['Title', 'Date', 'Author', 'Link']
        thewriter = csv.DictWriter(f, fieldnames=fieldnames)
        thewriter.writerow({'Title' : title, 'Date' : date, 'Author' : author, 'Link' : link})


def baseData(url):
    driver.get(url)
    r = driver.page_source
    soup = BeautifulSoup(r, 'html.parser')
    for post_header in soup.find_all("div", class_="post-header"):
        title = post_header.a.string
        link = post_header.a['href']
        date = post_header.div.span.a.string
        post_author = post_header.div
        author = post_author.find('span', class_='author').a.string
        print("Title    : " + title)
        print("Posted on: " + date)
        print("Posted by: " + author)
        print("Post Link: " + link)
        print("\n----------------------------------------------------\n")
        resultWriter(title, date, author, link)
    

def nextPageCheck(url):
    driver.get(url)
    r = driver.page_source
    soup = BeautifulSoup(r, 'html.parser')
    if "OLDER POST" in str(soup):
        older_post = soup.find('a', class_='next-posts-link')['href']
        return older_post, True
    else:
        return False



def visual():
    url = 'https://blog.scrapinghub.com/'
    while True:
        if nextPageCheck(url):
            url = nextPageCheck(url)[0]
            print("+---------------------------------------------------------------+")
            print("|                                                               |")
            print(f"   Going to next page: {url}           ")
            print("|                                                               |")
            print("+---------------------------------------------------------------+")
            baseData(url)
        else:
            print("+---------------------------------------------------------------+")
            print("|                                                               |")
            print("|           No more page left. Collecting post data             |")
            print("|                                                               |")
            print("+---------------------------------------------------------------+")
            driver.quit()
            visualMinor.postWriter()
            break