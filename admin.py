from user import*
from item import *


class Administrator(User):
    __last_id = 0
    # review: переменную __last_id я бы убрал, потому что при создании администратора происходит обращение к
    # суперклассу, в котором есть свой счетчик айди. Если вывести в main.py айди админа, то его айди будет равняться 6,
    # а не 1

    def __init__(self, name, surname):
        Administrator.__last_id += 1
        super().__init__(self, name, surname)
        # review: здесь я бы написал так super().__init__(name, surname, phone=None) например, так как суперкласс - это
        # User, а конструктор у User следующий: def __init__(self, name, surname, phone):
        # То есть при вызове суперкласса надо передать три параметра: имя, фамилию и телефон. И если написать так:
        # super().__init__(self, name, surname), то в имя админа вместо name попадет self (сам админ), в фамилию вместо
        # surname попадет name, а в телефон попадет фамилия админа.

    def add_item(self, item_category, item_name, item_price):
        Item(item_category, item_name, item_price)

    def __str__(self):
        return str(self.id) + ' ' + self.name + ' ' + self.surname

    # review: еще наверное можно было бы реализовать удаление товара админом, а может и не надо
