from readline import insert_text


class Binary:

    def __init__(self, number):
        self.number = number
        self._binnumber = bin(number)

    def __repr__(self):
        return f'<Binary number={self.number} bin={self._binnumber}>'

    def __and__(self, other):
        return Binary(self.number & other.number)

    def __or__(self, other):
        return Binary(self.number | other.number)

    def __xor__(self, other):
        return Binary(self.number ^ other.number)

    def __rand__(self, other):
        if isinstance(other, int):
            return Binary(self.number & other)
        return Binary(self.number & other.number)

    def __ror__(self, other):
        if isinstance(other, int):
            return Binary(self.number | other)
        return Binary(self.number | other.number)

    def __rxor__(self, other):
        if isinstance(other, int):
            return Binary(self.number ^ other)
        return Binary(self.number ^ other.number)

    def __iand__(self, other):
        print('iand')
        temp = self.__and__(other)
        self.number = temp.number
        self._binnumber = other._binnumber
        return self

    def __ior__(self, other):
        print('ior')
        temp = self.__or__(other)
        self.number = temp.number
        self._binnumber = other._binnumber
        return self

    def __ixor__(self, other):
        print('ixor')
        temp = self.__xor__(other)
        self.number = temp.number
        self._binnumber = temp._binnumber
        return self

b = Binary(5)
b1 = Binary(7)