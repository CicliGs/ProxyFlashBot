translations = {
    'en': {
        'Выберите регион:': 'Select a region:',
        'Выберите необходимый вариант:': 'Select the desired option:',
        'Данная функция пока в разработке...': 'This feature is still in development...',
        'Нужна другая локация': 'We need another location',
        'Назад': 'Back',
        'Польша': 'Poland',
        'Связаться с нами': 'Contact us',
        'Криптовалюта 💲': 'Cryptocurrency 💲',
        'Карточка 💳': 'Debit card 💳',
        '1 день (5$)': '1 day (5$)',
        '1 неделя (15$)': '1 week (15$)',
        '1 месяц (40$)': '1 month (40$)',
        '1 год (??$)': '1 year (??$)',
        'FAQ': 'FAQ',
    }
}


def choose_language(text, lang='ru'):
    #print(lan.getLanguage())
    if lang == 'ru':
        return text
    else:
        global translations
        try:
            return translations[lan.getLanguage()][text]
        except:
            return text


class lan:
    language = 'ru'
    @classmethod
    def setLanguage(cls, language):
        cls.language = language

    @classmethod
    def getLanguage(cls):
        return cls.language