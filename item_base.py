from item import *


class Item_Database:
    def __init__(self):
        self._items = [
            {
                'category': 'одежда',
                'tittle': 'футболка',
                'price': 800
            },
            {
                'category': 'одежда',
                'tittle': 'джинсы',
                'price': 1800
            },
            {
                'category': 'одежда',
                'tittle': 'куртка',
                'price': 30000

            },
            {
                'category': 'одежда',
                'tittle': 'майка',
                'price': 900

            },
            {
                'category': 'одежда',
                'tittle': 'пальто',
                'price': 20000

            },
            {
                'category': 'одежда',
                'tittle': 'носки',
                'price': 350
            }
        ]

    @property
    def baza_items(self):
        return self._items
    # review: здесь мне кажется лучше вообще убрать property и def baza_items. Просто если есть property, то обычно
    # тогда реализуют и setter. Потом property возвращает поле items защищенным, но оно и так защищенное

    @baza_items.getter
    def distribution_of_items(self):
        for i in range(len(self._items)):
            Item(self._items[i].get('Catecory'), self._items[i].get('Tittle'), self._items[i].get('price'))
    # review: @baza_items.getter я бы убрал, функция будет работать и без этого
    # review: небольшие опечатки: 'Catecory' нужно заменить на 'category', 'Tittle' нужно заменить на 'tittle'

    # review: Идея сделать базу данных товаров и реализовать метод по превращению словарей в списке items в объекты
    # Item мне нравится
