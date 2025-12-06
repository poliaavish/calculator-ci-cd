class Calculator:
    def add(self, a, b):
        """Сложение"""
        return a + b
    
    def subtract(self, a, b):
        """Вычитание"""
        return a - b
    
    def multiply(self, a, b):
        """Умножение"""
        return a * b
    
    def divide(self, a, b):
        """Деление"""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    
    def power(self, a, b):
        """Возведение в степень"""
        return a ** b

    def modulo(self, a, b):
        """Остаток от деления"""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a % b