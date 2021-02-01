# Web-Scraping-Demo
This is just a demo of "Web Scraping" with Python. 

# Usage

  `python3 scrapper.py visual` - To scrape visually with selenium <br>
  `python3 scrapper.py headless` - To scrape in shell/commandline only with requests

# How The Script Works

* This script with will scrape https://blog.scrapinghub.com/ recursively. 
* First the script will scrape home page for every blog "Post Title", "Post Date", "Post Author", "Post Link".
* After successfully scrape the first/home page it will check if there is any second page, if any it will go further and do the same thing.
* It will keep dooing the same thing until it reaches the last page of the blog.
* After collecting all data it will store those data locally in a CSV file called `result.csv`.
* Then it will create a directory named `data/` under the current directory.
* Then it will take all the links for the blog posts from `result.csv` file and scrape for the actual "Blog Article" and save it <br> 
  in `data/` directory with a name `"ACTUAL-POST-TITLE".txt`

# Module used
* Requests
  * `pip3 install requests`
* BeautifulSoup
  * `pip3 install bs4`
* Selenium
  * `pip3 install selenium`
* CSV
  * `pip3 install csv`



# POC-Proof-of-concept

[Visual Scraping](https://youtu.be/bJ00wuIBiWs).
[headless Scraping](https://youtu.be/yTSb74DRxVY).
