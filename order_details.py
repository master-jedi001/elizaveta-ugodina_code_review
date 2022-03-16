from order import *
from item import *


class OrderDetails:
    __list_order = dict()

    @staticmethod
    def add_to_cart(user_name, user_phone):
        print('___Добавьте товар в корзину___')
        Order.get_user_tittle(user_name, user_phone)
        if Order.get_user_tittle != None:
            if Order.get_user_tittle in Item.get_item_by_tittle:
                if not Order.get_user_tittle in OrderDetails.__list_order:
                    OrderDetails.__list_order[Order.get_user_tittle] = (Item.get_item_by_price(Order.get_user_tittle))


    @property
    def list_order(self):
        return self.__list_order

    @list_order.getter
    def get_order(self):
        return self.__list_order
    # далее можно реализовать оплату

    # review: @property и функцию list_order я бы убрал, так как list_order - это статическая переменная и она уже
    # является приватной. Строчку @list_order.getter тоже бы убрал, а оставил бы только метод get_order. Вместо
    # return self.__list_order лучше написать return OrderDetails.__list_order, так как list_order - статическая
    # переменная
    # Метод добавления товара в корзину в идейном плане реализован хорошо, есть только небольшие замечания по коду:
    #
    # строчка 11: я бы сделал так  _user_tittle = Order.get_user_tittle(user_name, user_phone), чтобы не вызвать каждый
    # раз метод get_user_tittle ( а то придется вводить код по нескольку раз ;) ) Везде где есть Order.get_user_tittle
    # можно просто писать _user_tittle

    # строчка 12: если я правильно понял, здесь идет проверка на то, что товар, который ввел пользователь, не является
    # пустым. Но если он введет пустую строку, то это тоже не будет равняьтся None, то есть это условие по идее всегда
    # будет выполняться. Мне кажется тогда лучше сделать так: if _user_tittle: Результат выдаст False, если _user_tittle
    # будет пустым и проверка тогда дальше не пойдет, добавления пустого товара в словарь не будет.
    #
    # строчка 13: если я правильно понял, здесь идет проверка на то, что товар, введенный пользователем, есть в базе
    # товаров. Но выражение Item.get_item_by_tittle не является списком или словарем, это объект класса Item (правда
    # чтобы это был объект, нужно еще в скобках передать название товара, так как метод get_item_by_tittle принимает
    # его на вход). Я бы здесь написал  так: if Item.get_item_by_tittle(_user_tittle): Если True, то товар есть в базе,
    # если False, то его в базе нет.

    # строчка 14: тут, как я понял, проверяется, что товара еще нет в словаре list_order, и тогда его можно туда
    # добавить. Здесь я бы только заменил Order.get_user_tittle на _user_tittle
    #
    # строчка 15: я бы так написал: OrderDetails.__list_order[_user_tittle] = Item.get_item_price_by_tittle(_user_tittle)
    # по поводу метода get_item_price_by_tittle я сделал комментарий в item.py.

    # Суммируя все, я бы вот так немного поменял метод add_to_cart:
    #
    # @staticmethod
    # def add_to_cart(user_name, user_phone):
    #     print('___Добавьте товар в корзину___')
    #     _user_tittle = Order.get_user_tittle(user_name, user_phone)
    #     if _user_tittle:
    #         if Item.get_item_by_tittle(_user_tittle):
    #             if not (_user_tittle in OrderDetails.__list_order):
    #                 OrderDetails.__list_order[_user_tittle] = Item.get_item_price_by_tittle(_user_tittle)

    # Получается, что list_order выполняет роль корзины, но поскольку это статическая переменная, то получается вроде
    # как, что у всех пользователей одна единая корзина. Наверное можно еще как-то сделать, чтобы у каждого пользователя
    # была своя корзина, и можно еще добавить методы по удалению товаров из корзины
