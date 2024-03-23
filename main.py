numbers = [1, 2, 67, "98348923465", 23, 2, 12, 32]
numbers.append("12")
numbers.insert(3, "12")
numbers.insert(len(numbers), "The end hahaha")
numbers += [123]
numbers.remove(2)
print(numbers)
