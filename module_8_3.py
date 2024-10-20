class IncorrectVinNumber(Exception):
    def __init__(self, message='Некорректный тип vin номер'):
        super().__init__(message)  # Передаем сообщение родительскому классу
        self.message = message

class IncorrectCarNumbers(Exception):
    def __init__(self, message='Некорректный тип данных для номеров'):
        super().__init__(message)  # Передаем сообщение родительскому классу
        self.message = message

class Car:
    def __init__(self, model, vin, numbers):
        self.model = model
        self.__vin = vin
        self.__numbers = numbers

        # Проверяем корректность vin и номера автомобиля
        self.__validate_vin(vin)
        self.__validate_numbers(numbers)

    def __validate_vin(self, vin_number):
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber()  # Используем сообщение по умолчанию
        if vin_number < 1000000 or vin_number > 9999999:
            raise IncorrectVinNumber('Неверный диапазон для vin номера')  # Теперь можем передать сообщение
        return True

    def __validate_numbers(self, numbers):
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers()  # Используем сообщение по умолчанию
        if len(numbers) != 6:
            raise IncorrectCarNumbers('Неверная длина номера')  # Теперь можем передать сообщение
        return True

# Пример выполнения кода
try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')