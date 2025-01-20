a = int(input("과제 :"))
b = int(input("중간 :"))
c = int(input("기말 :"))
mean = (a+b+c) / 3

print("평균 :", {mean})
if 90 <= mean:
    print("A학점 입니다")
elif 80 <= mean:
    print("B학점 입니다")
elif 70 <= mean:
    print("C학점 입니다")
elif 60 <= mean:
    print("D학점 입니다")
