from bs4 import BeautifulSoup
import csv
import urllib

url = 'http://news.etnews.com/'
file = urllib.request.urlopen(url)

soup = BeautifulSoup(file, 'html.parser')

links = soup.find_all('div', attrs={'class':'grid' })
for link in links:
    #print (link.findChild('strong'))
    strongTag = link.findChild('strong')
    if strongTag is not None:
        aTag = strongTag.findChild('a')
        if aTag is not None:
            linkToVisit = aTag.get('href')

            # news title # 
            newsTitle = aTag.get_text()
            
            fileToVisit = urllib.request.urlopen(linkToVisit)
            soupToVisit = BeautifulSoup(fileToVisit, 'html.parser')

            # news content #
            contentToVisit = soupToVisit.find('section', attrs={'id':'articleBody' })
            if contentToVisit is not None:
                contentP = contentToVisit.findChildren('p')
                content = ''
                for cp in contentP:
                    content = content + cp.get_text()
                   # print(cp.get_text())
                #print(content)

            # date #
            dateToVisit = soupToVisit.find('time', attrs={'class':'date' })
            if dateToVisit is not None:
                dateP = dateToVisit.get_text()

                # date #
                date = dateP
                #print(date)

            # save into csv #
            with open('newsScrap.csv', 'a', newline='') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter=',', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
                           # quotechar=' ', quoting=csv.QUOTE_MINIMAL)

                spamwriter.writerow([ newsTitle.encode("utf-8"), content.encode("utf-8"), date.encode("utf-8") ])                 
               # spamwriter.writerow([newsTitle.encode("utf-8"), 't', 't4'])
                                
                print('scrapped')
               

            










                
#print(contentToVisit)


#print (links[3].findChild('strong'))
#print (links[3].findChild('div'))



#print (file.read())

#html_doc = open(file.read(), 'r')


# links = soup.find_all('a')

#
#soup = BeautifulSoup(html_doc, 'html.parser')

# print(soup.prettify())
# print(soup.title.string)
# print (soup.find_all('a'))
# print (soup.get_text())

# f = csv.writer(open("test.csv", "w"))

#links = soup.find_all('a')

# for link in links:
#    print (link)
#    f.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])

#with open('test.csv', 'w', newline='') as f:
#    writer = csv.writer(f)
#    writer.writerows(['Spam'])
