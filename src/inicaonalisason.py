# def __init__(self, <аргументы>):
#     <тело метода>

class Employee:
    """Класс для представления сотрудника."""
    name = str
    surname = str
    email = str
    pay = int

    def __init__(self, first, last, pay):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        self.first = first  # эквивалентно emp_1.first = 'Ivan'
        self.last = last    # эквивалентно emp_1.last = 'Ivanov'
        self.pay = pay      # эквивалентно emp_1.pay = 50000
        self.email = f'{first}.{last}@email.com'  # эквивалентно emp_1.email = 'Ivan.Ivanov@email.com'