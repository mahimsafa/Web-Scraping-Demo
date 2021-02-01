import csv
import requests
from bs4 import BeautifulSoup


def writeData(data, filename):
    filename = filename[29:-1]
    filename =filename.replace('/', '_')
    with open("data/"+ filename + ".txt", 'w') as f:
        f.write(data)
def postLink():
    with open('result.csv', newline='') as f:
        reader = csv.DictReader(f)
        data = list(reader)
        # data = reader[3]
        return data

def postWriter():
    rule = postLink()
    for url in rule:
        link = url["Link"]
        print("\n------------------------------------------\n")
        print(link)
        r = requests.get(link).text
        soup = BeautifulSoup(r, 'html.parser')

        posttext = soup.find('span', id='hs_cos_wrapper_post_body')
        data = posttext.text
        writeData(data=data, filename=link)
        print(data)