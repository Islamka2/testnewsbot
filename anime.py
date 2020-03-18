
import requests
import telebot
from bs4 import BeautifulSoup as BS 

main_link = 'https://tengrinews.kz/'

r = requests.get(main_link)
tengri_html = BS(r.content, 'html.parser')
a = 0
b = []
def lol():
    print("LOL")
    
class Tengrinews:
    def __init__(self, link):
        self.title = tengri_html.title.string
    
    def find_word(self, word):
        print("Ищу...")
        try:
            for el in tengri_html.select('.tn-main-news-item'):
                if word in el.span.string.lower():
                    global b
                    text = [["Заголовок: ", el.span.string],["Ссылка на полную статью: ",main_link + el.a['href']], ["Дата и время публикации: ", el.ul.time.string]]
                    b.append(text)
                    print("-------------------------")
                    print("Заголовок: ",el.span.string)
                    print("Ссылка на полную статью: ",main_link + el.a['href'])
                    print("Дата и время публикации: ",el.ul.time.string)
                    print("-------------------------")
                else:
                    pass
        except AttributeError:
            print("Error")


    
# tengri = Tengrinews(main_link)
# print(tengri.title)
# a = str(input("Что ищем бро?"))
# tengri.find_word(a)

# for el in tengri_html.select('.tn-main-news-item'):
#     try:
#         if "коронавирус" in el.span.string.lower():
#             print(el.span.string)
#             print(main_link + el.a['href'])
#             print(el.ul)
#             print(el.ul.time)
#     except AttributeError:
#         print("Не имеет описания")