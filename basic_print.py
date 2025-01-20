#print문
print("1. Hello World!")
print("2. Hello", "World!") # 쉼표추가하면 하나 띄어쓰기
print("3. Hello", end = " ") # end는 프린트를 한 후에 어떤 행위를 할건지...
print("World!")

for c in [0b1001000, 0b1100101, 0b1101100, 0b1101100, 0b1101111,
          0b0100000, 0b1010111, 0b1101111, 0b1110010, 0b1101100, 0b1100100,
          0b0100001, 0b0001010]:
    print(chr(c), end= " ")  # 0b는 이진수로 표현

print("학번 : 2020112466")
print("이름 : 조영재")
