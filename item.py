import datetime


class Item:
    __last_id = 0
    __list_item = dict()
    # review: идея хранить список товаров в виде словаря очень хорошая

    def __init__(self, category, tittle, price):
        Item.__last_id += 1
        self.id = Item.__last_id
        self.tittle = tittle
        self.price = price
        self.created = datetime.datetime.now()
        self.updated = None
        self.category = category
        Item.__list_item[Item.__last_id] = self

    # review: поля id, created и updated я бы сделал приватными, чтобы к ним не было доступа извне без специалных
    # методов
    # review: для полей title и category я бы дополнительно сделал property и setter, чтобы валидировать значения,
    # которые будут туда приходить (момжно различные регулярные выражения добавить)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price
    # review: здесь мне кажется нужна проверка, например на то, что цена не будет отрицательной и будет целым
    # или вещественным числом

    @staticmethod
    def get_item_by_id(id):
        for item in Item.__list_item:
            if item.id == id:
                return item
        raise ValueError('Товар не найден')
    # review: по этому методу есть небольшое замечание: Item.__list_item - это словарь, ключи которого - айдишники
    # (числа), а значения - объекты класса Item. Поскольу item в цикле будет ключом, то item.id не спработает, так как
    # это число, а не объект. Мне кажется правильнее будет так:

    # @staticmethod
    # def get_item_by_id(id):
    #     for item in Item.__list_item:
    #         if item == id:
    #             return Item.__list_item[item]
    #     raise ValueError('Товар не найден')

    @staticmethod
    def get_item_by_price(price):
        for product in Item.__list_item:
            if product.price == price:
                return price
        raise ValueError('Товар не найден')
    # review: Аналогичная ситуация с методом get_item_by_price. В дальнейшем в классе OrderDetails этот метод будет
    # вызываться, но только для получения цены товара по его названию, а не для получения товара по его цене.
    # Поэтому я бы назвал этот метод как get_item_price_by_tittle.
    # @staticmethod
    # def get_item_price_by_tittle(tittle):
    #     for product in Item.__list_item:
    #         if Item.__list_item[product].tittle == tittle:
    #             return Item.__list_item[product].price
    #     raise ValueError('Товар не найден')

    # review: Аналогично и с методом get_item_by_title

    @staticmethod
    def get_item_by_tittle(tittle):
        for item in Item.__list_item:
            if item.tittle == tittle:
                return item
        raise ValueError('Товар не найден')
    # @staticmethod
    # def get_item_by_tittle(tittle):
    #     for item in Item.__list_item:
    #         if Item.__list_item[item].tittle == tittle:
    #             return Item.__list_item[item]
    #     raise ValueError('Товар не найден')

    def __str__(self):
        return str(self.id) + ' ' + self.category + ' ' + self.tittle + ' ' + str(self.price)

    # review: На мой взгляд класс Item реализован очень хорошо. Наверное еще можно подумать, как задействовать поле
    # updated.
    # review: Можно, например, обновлять его каждый раз, когда у товара будет меняться цена или сделать это поле
    # списком и хранить в нем историю изменений, произошедших с товаром
