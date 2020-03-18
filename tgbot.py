import telebot
import anime as t


TOKEN = '1049227502:AAG_iRRkXhONas_6JuaYryZJQ_SVPLT_Cfw'

tb = telebot.TeleBot(TOKEN)
# tb.send_message(chatid, message)
news = None

@tb.message_handler(commands=["help"])
def help(message):
    tb.send_message(message.chat.id, "Привет, у меня есть следующие команды:\n/start - пока хз зачем она мне.\n/tengri - просмотр новостей")
@tb.message_handler(commands=['start'])
def start_message(message):
    tb.send_message(message.chat.id, 'Привет, для начала давай выберем с какого источника ты хочешь получать информацию\nНа данный момент это только Tenginews, так что пиши - /tengri')
    print("lol")
    

@tb.message_handler(commands=['tengri'])
def choice_news(message):
    global news
    news = t.Tengrinews(t.main_link)
    send_news(message)
def send_news(message):
    print("Выбрали: ", news.title)
    tb.send_message(message.chat.id, ("Вы выбрали " + news.title))
    tb.send_message(message.chat.id, "Теперь давай посмотрим, что ты можешь сделать:\n/find - поиск по ключевому слову\nПока только пункт сверху!")

@tb.message_handler(commands=['find'])
def word(message):
    tb.send_message(message.chat.id, "Введи ключевое слово для поиска!")
    @tb.message_handler(content_types=['text'])
    def test(message):
        a = str(message.text)
        print(a, type(a))
        tb.send_message(message.chat.id, "Поиск...")
        news.find_word(a)
        # print("TEST", t.b)
        for i in range(len(t.b)-1):
            title = str(t.b[i][0][0] + t.b[i][0][1])
            link = str(t.b[i][1][0] + t.b[i][1][1])
            time = str(t.b[i][2][0] + t.b[i][2][1])
            tb.send_message(message.chat.id, "----------------------------------")
            tb.send_message(message.chat.id, title)
            tb.send_message(message.chat.id, link)
            tb.send_message(message.chat.id, time)
            tb.send_message(message.chat.id, "----------------------------------")

tb.polling(none_stop=True, interval=0)