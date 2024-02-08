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

welcome_message_1 = {
    "ru": "Proxy Flash это:\n\n🔥поддержка клиентов 24/7, мы всегда на связи, без исключений;\n🔥прокси будут только в вашем личном пользовании;\n🔥стабильное соединение.",
    "en": "Proxy Flash is:\n\n🔥 customer support 24/7, we are always on the phone, no exceptions;\n🔥 proxies will be only for your personal use;\n🔥 stable connection."
}

welcome_message_2 = {
    "ru": "Чтобы купить прокси, введите команду /proxy. Купленные прокси будут отображаться во вкладке /my_proxy.\nВы можете посмотреть все функции бота, открыв меню",
    "en": "To buy a proxy, enter the command /proxy. Purchased proxies will be displayed in the /my_proxy tab. You can view all the bot's functions by opening the menu"
}

payment_method_selection = {
    "ru": "Выберите способ оплаты:",
    "en": "Select a payment method:"
}

proxy_duration_selection = {
    "ru": "Выберите длительность работы прокси:",
    "en": "Select the duration of the proxy operation:"
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


def available_language(language: str):
    if language != 'ru' and language != 'en':
        return 'en'
    else:
        return language


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