from urllib.request import urlopen, Request
from json import loads

input_url = input('Starting URL: ')

last_slash_character = len(input_url) - input_url.rfind('/')

start_url = input_url[:-last_slash_character] + '.json'

print('Using URL:', start_url)

recieved_page = urlopen(Request(start_url, headers={'User-Agent': 'Mozilla'})).read().decode("utf-8")

page_object = loads(recieved_page)
