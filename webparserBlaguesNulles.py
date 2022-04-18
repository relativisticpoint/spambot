from bs4 import BeautifulSoup
import requests
import sys
from collections import OrderedDict
'''
-----------------------------------------------------------------------------------------------------------------------
-------------    Web Scrapper using the specific content of Blagues Nulles website to parse jokes       ---------------
-------------                  Beautiful Soup as a module for parsing                                   ---------------
-------------           Usage : python3 webparser.py <URL of the page with jokes>                       ---------------
-------------     Works with the specific html layout of the website but could be adapted to other ones ---------------
-----------------------------------------------------------------------------------------------------------------------
'''
def scrapping(url):
    #Connecting to the url 
    r = requests.get(url)   
    #Creating the Beautiful Soup parser on the html content 
    soup = BeautifulSoup(r.content,'html5lib')
    quote = []
    quote2 = []
    print(type(quote))
    table = soup.find('div',attrs={'class':'the_content'})
    h3 = table.find_all('h3')
    p = table.find_all('p')
    for i in h3:
        quote.append(i.text)
    for x in p:        
        quote2.append(x.text)
    print(quote)
    print (len(quote))
    print(len(quote2))
    list = []
    quote2.pop()
    quote2.remove('Dans cette sélection, retrouvez les pires blagues de tous les temps ! Certaines ne sont même pas humoristiques !')
    for i in range(0,2):
        quote2.pop(i)
    print(quote2[0])
    for i in range(0,42):
        list.append(quote2.pop())
    print(list)
    list.reverse()
    print(len(list))
    print(list)
    filename = 'sentences.txt'
    with open(filename,'w',newline='') as f:
          for i in range(0,42,1):
              f.write(quote[i])
              f.write("\n")
              f.write(list[i])
              f.write("\n")
            
if __name__=="__main__":
    if (len(sys.argv) != 0 ):
        print("URL : "+sys.argv[1]+"\n")
        scrapping(sys.argv[1])
    else: 
        print("Usage : python3 webparser.py <URL of blagues nulles the website>")
        sys.exit(1)
    
