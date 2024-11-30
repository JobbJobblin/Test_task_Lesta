# Вопрос №2
#
# На языке Python написать минимум по 2 класса реализовывающих циклический буфер FIFO. Объяснить плюсы и минусы каждой реализации.

#Класс 1. Использует список. Использует встроенные методы работы со списками.

class Pie_collector:

    def __init__(self):
        self.list = list() #Список для хранения элементов.

    def Inject(self, item):
        # Добавляем значение в конец списка (first in...).
        self.list.append(item)
        print(f"{item} добавлен к списку.")
        print(f"Теперь список выглядит так: {self.list}.")

    def Reject(self):
        # Убираем значение из конца списка (...first out).
        try:
            Rejected = self.list.pop()
            print(f"Из списка был удалён {Rejected}")
            print(f"Теперь список выглядит так: {self.list}.")
        except:
            #Обработка ошибки при вызове Reject с пустым списком.
            print("Чтобы что-то убрать, нужно что-то добавить. Список пуст.")

print("Класс 1. Который не делает ничего интересного.")
#Создаём экземпляр класса.
The_List = Pie_collector()
#Добавляем значения.
The_List.Inject(item="Absolutely random value 1")
The_List.Inject("Absolutely random value 2")
The_List.Inject("Пенкин")
The_List.Inject("Absolutely random value 4")
#Убираем значения.
The_List.Reject()
The_List.Reject()
The_List.Reject()
The_List.Reject()
#Ловим ошибку.
The_List.Reject()



