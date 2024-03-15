
class Calculator:

    def addnumbers(self, num1, num2):
        try:
            res = num1 + num2
            return res
        except Exception as e:
            print(f"Помилка {e}")

    def substructnumbers(self, num1, num2):
        try:
            res = num1 - num2
            return res
        except Exception as e:
            print(f"Помилка {e}")

    def multiplynumbers(self, num1, num2):
        try:
            res = num1 * num2
            return res
        except Exception as e:
            print(f"Помилка {e}")

    def devidenumbers(self, num1, num2):
        try:
            res = num1 / num2
            return res
        except ZeroDivisionError:
            print("На нуль ділити не можна")

    def squareroot(self, x):
        try:
            if x < 0:
                raise ValueError("Неможливо обчислити квадратний корінь від від'ємного числа.")
            res = x ** 0.5
            return res
        except ValueError as e:
            print("помилка", e)

    def exponumbers(self, num1, num2):
        try:
            if num2 < 0:
                raise NegativeExpoError()
            res = num1 ** num2
            return res
        except NegativeExpoError as e:
            print("помилка", e)





class NegativeExpoError(Exception):
    def __init__(self, message='число не має бути негативним'):
        super().__init__(message)




calc = Calculator()
print(calc.addnumbers(5, 3))
print(calc.substructnumbers(5, 3))
print(calc.multiplynumbers(5, 3))
print(calc.devidenumbers(5, 0))
print(calc.devidenumbers(5, 2))
print(calc.exponumbers(2, -3))
print(calc.exponumbers(2, 3))
print(calc.squareroot(-9))
print(calc.squareroot(9))