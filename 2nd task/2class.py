# Вопрос №2
#
# На языке Python написать минимум по 2 класса реализовывающих циклический буфер FIFO. Объяснить плюсы и минусы каждой реализации.

#Класс 2. Использует словарь. Вместо использования стандартных методов (вроде update и pop), усложняет себе жизнь.

class Pie_collector_but_cooler:

    def __init__(self):
        self.data = {} # Словарь для хранения элементов.
        self.id = 0 #Переменная-счётчик. Присваивает уникальный id.

    def Inject(self, item):
        #Увеличиваем счётчик на 1. Добавляем значение с номером в счётчике => Добавляем значение в конец списка (first in...).
        self.id += 1
        self.data[self.id] = item
        print(f"{item} добавлен к словарю.")
        print(f"Теперь словарь выглядит так: {self.data}.")

    def Reject(self):
        # Убираем значение из конца списка (...first out).
        if self.data.keys():
            for key in self.data.keys():
                #Ищем максимальное значение ключа.
                max_id = max(self.data.keys())
                #Удаляем пару с максимальным значением ключа.
                del self.data[max_id]
                print(f"Из словаря был удалён {max_id}")
                print(f"Теперь словарь выглядит так: {self.data}.")
                return
        else:
            #Обработка запроса при вызове Reject с пустым списком.
            print("Чтобы что-то убрать, нужно что-то добавить. Словарь пуст.")

print("Класс 2. Который проснулся и выбрал боль.")
#Создаём экземпляр класса.
The_List = Pie_collector_but_cooler()
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
The_List.Reject()



