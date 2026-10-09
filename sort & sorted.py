numbers = [3,1,4,1,5,9]

new_list = sorted(numbers) #새 리스트 만듦
print(new_list) #새 리스트에서 정렬된 값을 호출함
print(numbers) #원본 유지

numbers.sort() #직접 정렬
print(numbers)

def square(x):
    return x * x

square_lambda = lambda x: x * x

print(square(5))
print(square_lambda(5))

text = "apple, banana, cherry"
words = text.split(",")
print(words)

words = ['apple', 'banana', 'cherry']
result = "-".join(words)
print(result)





