# modules used :
     # pip install requests 
     # pip install bs4 
     # pip install html5lib 

     
import requests
from bs4 import BeautifulSoup


url = "https://mohammadabdullah.netlify.app/"


# step no 1 : get the HTML
req = requests.get(url)
HTMLContent = req.content
# print(HTMLContent)


# step no 2 : parse the HTML
soup = BeautifulSoup(HTMLContent, 'html.parser')
# print(soup.find('p').get_text())
# print(soup.prettify)


# step no 3 : HTML  tree traversal


# === WORKING WITH A-TAGS ====
Atag = soup.find_all('a')
# print(Atag)
# print(Atag[0].get_text())
# print(Atag[0].get('href'))



# === WORKING WITH h-TAGS ====
H1 = soup.find('h1')
# ------------printing the text of h1 tag------------
# print(H1.get_text())


# === WORKING WITH IMG-TAGS ====
ImageTags = soup.find('img')
# ------- the get method always returns a string ----------
# print(type(ImageTags.get('src')))

# === WORKING WITH script-TAGS ====
JSCode = soup.find_all('script')
# --------- get the JS code written inside the html ------
print(JSCode[2].get_text())