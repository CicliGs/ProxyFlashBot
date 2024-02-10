

class User:
    def __init__(self, user_id, referrer_id, language):
        self.user_id = user_id
        self.referrer_id = referrer_id
        self.language = language


class Proxy:
    def __init__(self, user_id, country, proxy, start_proxy_date, end_proxy_date, time):
        self.user_id = user_id
        self.country = country
        self.proxy = proxy
        self.start_proxy_date = start_proxy_date
        self.end_proxy_date = end_proxy_date
        self.time = time

    id: str | int


class Transaction:
    def __init__(self, user_id, payment_amount, currency, transaction_date, transaction_time):
        self.user_id = user_id
        self.payment_amount = payment_amount
        self.currency = currency
        self.transaction_date = transaction_date
        self.transaction_time = transaction_time

    id: str | int

