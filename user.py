import datetime


class User:
    __last_id = 0
    __list_user = dict()
    # review: идея хранить список пользователей в виде словаря очень хорошая

    def __init__(self, name, surname, phone):
        User.__last_id += 1
        self.id = User.__last_id
        self.name = name
        self.surname = surname
        self.phone = phone
        self.created = datetime.datetime.now()
        self.updated = None
        self.last_visit = self.created
        User.__list_user[User.__last_id] = self

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, phone):
        self.__phone = phone

    @staticmethod
    def get_user_by_id(id):
        for user in User.__list_user:
            if user.id == id:
                return user
        raise ValueError('Пользователь не найден')
    # @staticmethod
    # def get_user_by_id(id):
    #     for user in User.__list_user:
    #         if User.__list_user[user].id == id:
    #             return User.__list_user[user]
    #     raise ValueError('Пользователь не найден')

    @staticmethod
    def get_user_by_phone(phone):
        for user in User.__list_user:
            if user.phone == phone:
                return user
        raise ValueError('Пользователь не найден')
    # @staticmethod
    # def get_user_by_phone(phone):
    #     for user in User.__list_user:
    #         if User.__list_user[user].phone == phone:
    #             return User.__list_user[user]
    #     raise ValueError('Пользователь не найден')

    def __str__(self):
        return str(self.id) + ' ' + self.name + ' ' + self.surname

    # review: В идейном плане класс реализован очень хорошо. В плане каких-то технических деталей,
    # то замечания примерно такие же, как и для класса Item: поля id, created, updated, last_visit я бы сделал
    # приватными и добавил бы методы по доступу к этим полям, если потребуется. Добавил бы дополнительно property и
    # setter с проверками для полей имя и фамилия и к полю phone тоже бы добавил проверку по какому-нибудь регулярному
    # выражению например. Просто сейчас получается, что можно создавать кучу пользователей с одинаковыми именами,
    # фамилиями и телефонами (дубликаты одного и того же пользователя). В методах поиска пользователя по айди и телефону
    # ситуация такая же, как с методами поиска в классе Item (здесь User.__list_user - это словарь, а не список). А в
    # остальном все очень логично.
