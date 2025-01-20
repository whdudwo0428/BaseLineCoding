list_a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
list_b = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
list_c = []

index_a, index_b = 0, 0
n = 1  # 처음에는 1개씩 추가

while index_a < len(list_a) or index_b < len(list_b):
    # list_a에서 n개의 값을 추가 (리스트의 범위를 넘지 않도록 처리)
    for i in range(n):
        if index_a < len(list_a):
            list_c.append(list_a[index_a])
            index_a += 1

    # list_b에서 n개의 값을 추가 (리스트의 범위를 넘지 않도록 처리)
    for i in range(n):
        if index_b < len(list_b):
            list_c.append(list_b[index_b])
            index_b += 1

    n += 1  # 추가할 개수를 1씩 증가시킴

print(list_c)
