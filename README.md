# Тестовые задания
Вопрос №1:
  isEven.py - пример с целочисленным делением.
  isEven_AND.py - решение с бинарным оператором "И".

Разницы по времени выполнения операторов не заметил (прим.: time_Even.py и     time_Even_AND.py). Однако в сети наткнулся на указание, что выполнение с целочисленным делением быстрее. Переведя программы в байт-код получил подтверждение: 308 байт против 312 байт.

Вопрос №3:
  Реализован алгоритм сортировки слиянием (Merge sort) для массива случайных чисел. В отличии от быстрой сортировки средняя скорость выполнения алгоритма остается постоянной при любых наборах данных. Так как по условию задачи основной критерий - скорость, то Merge sort очевидный выбор. Если на первом месте стояло бы экономное использование памяти, то лучшим решением была бы быстрая сортировка. У сортировки слиянием есть улучшение по скорости - Timsort. Собственно функция sort() в Python вызывает алгоритм Timsort. Но улучшение по скорости будет лишь в том случае, если в исследуемом массиве найдутся уже упорядоченные подмассивы.
