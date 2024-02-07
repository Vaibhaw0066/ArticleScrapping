

from bs4 import BeautifulSoup
import requests
import csv

def getArticleTitle(soup):
    headers = soup.find_all("h1")
    if len(headers)>0:
        return soup.find_all("h1")[0].getText()
    else:
        return "Article Not Found"

def getArticleData(soup):
    data = soup.findAll("div",{"class":"td-post-content tagdiv-type"})
    if len(data)>=0:
        return data[0].getText()
    else:
        return "NOT Found"


urlsList = []
title_article_list = []
count=1

# Loading Input URLs
with open('InputURLSheet.csv', 'r') as input_file:
    input_data = csv.reader(input_file)
    for line in input_data:
        urlsList.append(line[1])

# Removing Excel headers
urlsList.pop(0)


for url in urlsList[14:17]:
    # Loading web-page
    webPage=requests.get(url)

    # Making SOUP of it
    soup = BeautifulSoup(webPage.content,features="html.parser")

    # Filtering title and article
    title   = getArticleTitle(soup)
    article = getArticleData(soup)

    print(count,"=> ",title)
    if(title=="Not Found"):
        print(url,title)
    else:
        title_article_list.append([title,article])


# Writing result to output file
with open("output.csv",'w') as OutputFile:
    writer = csv.writer(OutputFile)
    writer.writerow(['Title','Article'])
    writer.writerows(title_article_list)
