from aiogram.types import BotCommand

translations = {
    'en': {
        'Выберите регион:': 'Select a region:',
        'Выберите необходимый вариант:': 'Select the desired option:',
        'Данная функция пока в разработке...': 'This feature is still in development...',
        'Выберите длительность работы прокси:': 'Select the duration of the proxy operation:',
        'Выберите способ оплаты:': 'Select a payment method:'
    }
}

bot_commands = {
    'ru': [
        BotCommand(command="/proxy", description="Купить прокси"),
        BotCommand(command="/help", description="Помощь"),
        BotCommand(command="/affiliate", description="Партнёрская программа"),
        BotCommand(command="/my_proxy", description="Мои прокси")
    ],
    'en': [
        BotCommand(command="/proxy", description="Buy proxy"),
        BotCommand(command="/help", description="Help"),
        BotCommand(command="/affiliate", description="Affiliate program"),
        BotCommand(command="/my_proxy", description="My proxy")
    ]
}


def choose_language(text, lang='ru'):
    if lang == 'ru':
        return text
    else:
        global translations
        try:
            return translations[lang][text]
        except:
            return text


class lang_:
    language = 'ru'
    @classmethod
    def setLanguage(cls, language):
        cls.language = language

    @classmethod
    def getLanguage(cls):
        return cls.language