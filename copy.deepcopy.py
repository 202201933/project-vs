import copy

original = [[1,2],3,4]

shallow = copy.copy(original)
deep = copy.deepcopy(original)

original[0].append(99)

print('original:', original) #바뀐 결과
print('shallow', shallow) #바꾼 결과 호출
print('deep', deep) #원본 유지

