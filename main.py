

from bs4 import BeautifulSoup
import requests
import csv

def getArticleTitle(soup):

    headers = soup.find_all("h1")
    if len(headers)==0:
        return "Not Found"
    else:
        return headers[0].getText()

def getArticleData(soup):
    data = soup.findAll("div",{"class":"td-post-content tagdiv-type"})
    if len(data)>0:
        return data[0].getText()
    else:
        return "Article Not Found"




urlsList = []
title_article_list = []
count=1

# Loading Input URLs
with open('InputURLSheet.csv', 'r') as input_file:
    input_data = csv.reader(input_file)
    for row in input_data:
        print(row)
        url = row[1]
        urlsList.append(url)


# Removing Excel headers
urlsList.pop(0)
#

for url in urlsList:
    # Loading web-page
    webPage = requests.get(url)

    # Making SOUP of it
    soup = BeautifulSoup(webPage.content,features="html.parser")

    # Filtering title and article
    title   = getArticleTitle(soup)
    article = getArticleData(soup)

    print(count,"=> ",title)
    count+=1
    if(title=="Not Found"):
        # print(url,title)
        title = "Not Found"
        article = "Article not found for  URL : "+ url

    title_article_list.append([title,article])


# Writing result to output file
with open("output.csv",'w') as OutputFile:
    writer = csv.writer(OutputFile)
    writer.writerow(['Title','Article'])
    writer.writerows(title_article_list)
