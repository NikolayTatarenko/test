class String(str):
    def __add__(self, other):
        return String(str(self) + str(other))

    def __sub__(self, other):
        if isinstance(other, str):
            return String(str(self).replace(other, '', 1))
        elif isinstance(other, int):
            return String(str(self).replace(str(other), '', 1))
        else:
            return String(str(self))

print(String('New') + String(890))
print(String(1234) + 5678)
print(String('New') + 'castle')
print(String('New') + 77)
print(String('New') + True)
print(String('New') + ['s', ' ', 23])
print(String('New') + None)