import mechanize
from BeautifulSoup import BeautifulSoup
import urllib
import requests
html_content = urllib.urlopen("https://www.facebook.com/profile.php?id=100005725576273&fref=nf")
data = html_content.read()
soup = BeautifulSoup(data)
print (soup.title)

"""
score = soup.find_all('div', attrs={'class' : '_mediaPageName'})
print(score)

print (soup)"""



"""print (data)  donne le code ok"""

print(soup.title.string)

print(soup.findAll('span'))
