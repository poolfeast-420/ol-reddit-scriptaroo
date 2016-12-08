from requests import get

start_page_address = input('Address of start page:')

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

page = get(start_page_address.split(";")[0]
, headers=headers)
search_string = page.text.lower()

search_phrases = ["the ol' reddit","the ol reddit"]

print(page.text)

for phrase in search_phrases:
    if phrase in search_string:
        # this part is confusing because -1 is what find returns when it fails and also the last element of a list
        result_characters = []
        result_characters.append(search_string.find(phrase))
        while result_characters[-1] is not -1:
            result_characters.append(search_string.find(phrase, result_characters[-1] + 1))
        del result_characters[-1]

for result_character in result_characters:
    start_character = search_string.rfind('<p>', 0, result_character) + 3
    end_character = search_string.find('</p>', result_character)
    print(search_string[start_character:end_character])
