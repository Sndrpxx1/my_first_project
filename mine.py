import telebot
from pas import gen_pass  # Импортируем функцию из bot_logic

# Замени 'TOKEN' на токен твоего бота
# Этот токен ты получаешь от BotFather, чтобы бот мог работать
bot = telebot.TeleBot("8112631224:AAHM_tmE_GB0hLGK-4RpGYgRLDR4mwffRgc")

# Эта функция запускается, когда кто-то отправляет команду /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Бот отвечает пользователю приветственным сообщениемtelebot
    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши что-нибудь!")

# Эта функция запускается, когда кто-то отправляет команду /hello
@bot.message_handler(commands=['hello'])
def send_hello(message):
    # Бот отвечает, спрашивая, как дела
    bot.reply_to(message, "Привет! Как дела?")

@bot.message_handler(commands=['mem'])
def send_mem(message):
    with open('images/kodland.jpeg', 'rb') as f:
        bot.send_photo(message.chat.id, f)


# Эта функция запускается, когда кто-то отправляет команду /bye
@bot.message_handler(commands=['bye'])
def send_bye(message):
    # Бот прощается с пользователем
    bot.reply_to(message, "Пока! Удачи!")


@bot.message_handler(commands=['pass'])
def send_password(message):

    password = gen_pass(10)  # Устанавливаем длину пароля, например, 10 символов
    bot.reply_to(message, f"Вот твой сгенерированный пароль: {password}")

@bot.message_handler(commands=['echo'])
def send_echo(message):
    # Бот отвечает, спрашивая, как дела
    bot.reply_to(message, "Загрязнение водных ресурсов стало причиной потери многих видов флоры и фауны Земли. Это произошло из-за того, что промышленные отходы, сбрасываемые в реки и другие водные объекты, вызывают дисбаланс в водной среде, что приводит к серьезному загрязнению и смерти водных животных и растений!")

# Эта функция запускается для всех остальных сообщений
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    # Бот повторяет текст, который ему отправил пользователь
    bot.reply_to(message, message.text)

bot.delete_my_commands(scope=None, language_code=None)



bot.set_my_commands(
    commands=[
        telebot.types.BotCommand("start", "Запуск бота"),
        telebot.types.BotCommand("hello", "description"),
        telebot.types.BotCommand("hello", "description"),
        telebot.types.BotCommand("pass", "description")
    # scope=telebot.types.BotCommandScopeChat(12345678)  # use for personal command for users
    # scope=telebot.types.BotCommandScopeAllPrivateChats()  # use for all private chats
])


# check command
cmd = bot.get_my_commands(scope=None, language_code=None)
print([c.to_json() for c in cmd])




bot.polling()
