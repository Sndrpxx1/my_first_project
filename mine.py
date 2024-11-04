import random
hobby = ["Jantemir","13","cyprus","Cat"]
print(random.choice(hobby))

print("HelloWorld")

import telebot


API_TOKEN = '8112631224:AAHM_tmE_GB0hLGK-4RpGYgRLDR4mwffRgc'
bot = telebot.TeleBot(API_TOKEN)

# use in for delete with the necessary scope and language_code if necessary
bot.delete_my_commands(scope=None, language_code=None)

bot.set_my_commands(
    commands=[
        telebot.types.BotCommand("start", "Запуск бота"),
        telebot.types.BotCommand("hello", "Приветствие"),
        telebot.types.BotCommand("bye", "Прощаемся")
    ],

    # scope=telebot.types.BotCommandScopeChat(12345678)  # use for personal command for users
    # scope=telebot.types.BotCommandScopeAllPrivateChats()  # use for all private chats
)

# check command
cmd = bot.get_my_commands(scope=None, language_code=None)
print([c.to_json() for c in cmd])

bot.polling()
