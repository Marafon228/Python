numbers = [5, 7, 9]
#numbers[3] = 100
numbers.append(100)
numbers.append(222)
numbers.insert(1, True)
b = [5, 6, 0]
numbers.extend(b)
#numbers.reverse() в обратном порядке
numbers.sort()

numbers.pop() #последний элемент удаляется, иначе удаляется по индексу

numbers.pop(-2)

numbers.remove(6) #Удаляет по определенному значению

#numbers.clear()  Удаляет весь список

print(numbers.count(5)) # Кол-во совпадений

print(len(numbers)) # длинна списка

print(numbers)