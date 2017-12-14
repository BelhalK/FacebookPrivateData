import mechanize
from BeautifulSoup import BeautifulSoup
import urllib
import requests
import html5lib
f = urllib.urlopen("https://www.facebook.com/profile.php?id=100005725576273&fref=nf")
data = f.read()

data2 = html5lib.parse(f)

print (data2)
