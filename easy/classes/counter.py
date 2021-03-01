"""
Описать класс Counter, реализующий целочисленный счетчик.
который может увеличивать или уменьшать свое значение (атрибут value)
на единицу в заданном диапазоне.

Предусмотреть инициализацию счетчика значениями по умолчанию и произвольными значениями.

Определить атрибуты:

- value - текущее значение счетчика

Определить методы:

- инициализатор __init__, который устанавливает значение счетчика или 0 по умолчанию
- increase(num=1), увеличивает счетчик на заданную величину или 1 по умолчанию
- decrease(num=1), уменьшает счетчик на заданную величину или 1 по умолчанию
- метод __iter__
- метод __next__
"""


class Counter:
    def __init__(self, value=0, inc=1, dec=1, min_count=-10, max_count=10):
        self.value = value
        self._increase = inc
        self._decrease = dec
        self.min_count = min_count
        self.max_count = max_count

    def increase(self):
        if self.value + self._increase >= self.max_count:
            raise StopIteration
        self.value += self._increase

    def decrease(self):
        if self.value - self._decrease <= self.min_count:
            raise StopIteration
        self.value -= self._decrease

    def __iter__(self):
        return self

    def __next__(self):
        self.increase()
        return self.value
