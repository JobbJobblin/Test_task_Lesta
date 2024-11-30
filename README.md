# Test_task_Lesta
Тестовое задание для вакансии Стажер-программист игровой логики (Intern Game Logic Programmer)

# Вопрос 1.

На языке Python написать алгоритм (функцию) определения четности целого числа, который будет аналогичен нижеприведенному по функциональности, но отличен по своей сути. Объяснить плюсы и минусы обеих реализаций. 

Задание выполнено [тут](https://github.com/JobbJobblin/Test_task_Lesta/blob/31aa02cf911e9589036edae8e00eb919bb4c8e4c/1st%20task/pie.py).
В комментариях описано решение, а также плюсы и минусы вариантов.

# Вопрос 2.

На языке Python написать минимум по 2 класса реализовывающих циклический буфер FIFO. Объяснить плюсы и минусы каждой реализации.

1 класс [тут](https://github.com/JobbJobblin/Test_task_Lesta/blob/31aa02cf911e9589036edae8e00eb919bb4c8e4c/2nd%20task/1class.py).

1 класс написан на основе списка с использованием базовых методов списка Python:
+ Список является довольно лёгкой коллекцией, что делает работу кода быстрее.
+ Базовые методы делают код поддерживаемым и читаемым.
- Базовые методы могут быть не всегда лучшим решением проблемы.
- Список ограничен в своей фукнциональной эксплуатации. Дальнейшее использование класса маловероятно.

2 класс [тут](https://github.com/JobbJobblin/Test_task_Lesta/blob/31aa02cf911e9589036edae8e00eb919bb4c8e4c/2nd%20task/2class.py).

2 класс написан на основе словаря с использованием базовых команд Python.
+ Использование словаря позволяет создавать более детальные версии буфера благодаря ключам.
+ Отсутствие базовых методов делает переработку/доработку класса более простой. 
- Код чуть менее читаем для стороннего пользователя, чем первый класс, т.к. не использует общепринятых методов для работы со словарями.
- Словарь - коллекция более тяжёлая, чем список, что потенциально может замедлить исполнение кода. 

# Вопрос 3. 

На языке Python предложить алгоритм, который быстрее всего (по процессорным тикам) отсортирует данный ей массив чисел. Массив может быть любого размера со случайным порядком чисел (в том числе и отсортированным). Объяснить, почему вы считаете, что функция соответствует заданным критериям.

Решение написано [тут](https://github.com/JobbJobblin/Test_task_Lesta/blob/31aa02cf911e9589036edae8e00eb919bb4c8e4c/3d%20task/pie.py).

К сожалению, нового алгоритма сортировки я не придумал. Был использован метод сортировки слиянием. 
К реализации рассматривалось три варианта:
1) Timsort
2) Сортировка слиянием (merge sort)
3) Сортировка пирамидой/кучей (heap sort)

1 вариант был наиболее эффективным во всех возможных смыслах. Разработчики Python, как оказалось, согласны с этим мнением.
Решив не реализовывать стандартную функцию sort, я выбрал вариант merge sort.
Несмотря на одинаковое расчётное время исполнения, merge sort сугубо эмпирически демонстрирует более быстрые результаты сортировки, чем heap sort. 
Ключевым недостатком, который реально может повлиять на выбор в сторону другого метода сортировки, было использование памяти. 
В связи с рекурсивным созданием дополнительных списков Merge sort использует для решения задачи дополнительную память. 
Если её достаточно в рамках поставленной задачи, то merge sort действительно будет лучше выполнять задачу. 
Если нет, то heap sort - верный ответ. 
