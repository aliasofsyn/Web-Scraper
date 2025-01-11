from bs4 import BeautifulSoup
import requests
from lxml import etree

def getCompanies(): 
    url = requests.get("https://www.ycombinator.com/companies/industry/ai")
    scraper = BeautifulSoup(url.text, "lxml")

    dom = etree.HTML(str(scraper))

    links = dom.xpath("//ul[@class = 'space-y-2 overflow-hidden']/a/@href")
    
    with open('output/companies.csv', 'w') as file:
        for link in links:
                file.write("https://www.ycombinator.com" + link + "\n")


def isAquired(scraper):
        text = scraper.get_text(separator=" ", strip=True)
        acquiredCount = text.lower().count("acquired")
        return True if acquiredCount != 0 else False
            

def getInfo():
    file = open('output/companies.csv', 'r')
    for line in file:
        url = requests.get(line.removesuffix("\n")).text
        scraper = BeautifulSoup(url, 'html.parser')    

        #if(not isAquired(scraper)):
            
                    


if __name__ == '__main__':
    getInfo() 