
import webbrowser

import requests
from bs4 import BeautifulSoup

input_func = None
try:
    input_func = input('Enter the song to be played: ')
except NameError:
    input_func = input('Enter the song to be played: ')

query = input_func.replace(' ', '+')

# search for the best similar matching video
url = 'https://www.youtube.com/results?search_query=' + query
source_code = requests.get(url, timeout=15)
plain_text = source_code.text
soup = BeautifulSoup(plain_text, "html.parser")

# fetches the url of the video
songs = soup.findAll('div', {'class': 'yt-lockup-video'})
song = songs[0].contents[0].contents[0].contents[0]
# link = song['href']
# webbrowser.open('https://www.youtube.com' + link)

try:
    link = song['href']
    webbrowser.open('https://www.youtube.com' + link)
except KeyError:
    print("Can't find any song,check your network or try a new word")

