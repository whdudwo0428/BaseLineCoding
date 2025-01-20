print("별 찍기")
print("1.☆")
print("2.★")
print("3.#")
print("4.○")
print("5.●")

mode = int(input("모드를 선택하시오 :"))
len = int(input("길이를 입력하시오 :"))

if mode == 1:
    shape = "☆"  # mode = "★"
elif mode == 2:
    shape = "★"  # mode = "★"
elif mode == 3:
    shape = "#"

if mode == 1 or mode == 2:
    #위
    for i in range(len):
        if i == 0:
            print(" "*(len*3-1) + shape)
        else :
            print(" "*(len*3-(i+1)) + shape*(i+1))
        if i+1 == len:
            print(shape*(len*3+1))
    #중간
    for j in range(len//2):
        print(" "*((j+1)*2) + shape*(len*3-2*(j+1)))
    #아래
    for k in range(len,0,-1):
        print(" "*(k-1) + shape*k + " "*(5*(len-k)) + shape*k)

if mode == 3:
    hole = len // 3
    for i in range(0,5):
        hole = len//3

        if i % 2 == 0:
            print(" " * ((hole * 2)-i) + shape + " "*(hole * 2) + shape)
        else:
            print(shape*len*2)
