import urllib.request
import re
import sys

print("Starting...")
fnamebackup = "urls.txt"
fname = "urls.txt"
print("Opening" + fname + "...")
with open(fname) as f:
   urls = f.readlines()
with open(fnamebackup) as products:
   listProducts = products.readlines()
print(fname + " file successful opened.")

if not urls:
    sys.exit("Empty url text file provided!")

i=0;
intArticleCounter = 0
intUrlCounter = 0

strArticlePatern = re.compile(b'<a class="productLink" href="(.+?)">')
strUrlsPatern = re.compile(b'<a href="(.+?)" target="_self">')

print("Searching for <a class=productLink")
while i< len(urls):
    print("\n \nGetting data from urls in text file...")
    htmlfile = urllib.request.urlopen(urls[i])
    htmltext = htmlfile.read()
    #print(htmltext)
    ListArticleLinks = re.findall(strArticlePatern, htmltext)
    ListUrls = re.findall(strUrlsPatern, htmltext)

    i += 1
    intCurrentProductCounter = 0
    intCurrentUrlCounter = 0

    f = open("articles.txt", "a")
    for strArticleUrl in ListArticleLinks:
        strArticleUrl = strArticleUrl.decode("utf-8")
        strArticleUrl = "http://www.alternate.nl/html/product" + strArticleUrl
        if strArticleUrl not in listProducts:

            #print(strArticleUrl)

            f.write("%s\n" % strArticleUrl)
            intArticleCounter = intArticleCounter + 1
    print("Amount of products found on url: ")
    print(intCurrentProductCounter)

    print("Finished collecting articles from site")

    #TODO fix ' displaying as ?

    print("Starting to collect urls...")

    FileUrls = open("urls.txt", "a")
    for item in ListUrls:
        item = item.decode("utf-8")
        item = "http://www.alternate.nl" + item
        if item not in urls:
            intCurrentUrlCounter += 1

            #print(item)
            FileUrls.write("%s\n" % item)
            intUrlCounter = intUrlCounter + 1
    print("Amount of urls found on url: ")
    print(intCurrentUrlCounter)

    print("Finished collecting urls")
    print("Page number:")
    print(i)
    print("Total amount of pages:")
    print(len(urls))

print("Amount of pages crawled:")
print(i)

print("Amount of articles found:")
print(intArticleCounter)

print("Amount of urls found:")
print(intUrlCounter)