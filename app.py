def add(a, b):
    """Додає два числа"""
    return a + b


def subtract(a, b):
    """Віднімає два числа"""
    return a - b


def multiply(a, b):
    """Множить два числа"""
    return a * b


def divide(a, b):
    """Ділить два числа"""
    if b == 0:
        raise ValueError("Ділення на нуль неможливе")
    return a / b


def greet(name):
    """Вітає користувача"""
    return f"Привіт, {name}!"
