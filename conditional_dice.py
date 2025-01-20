'''
a,b = map(int,input().split())

if a>b :
    print(">")
elif a==b :
    print("==")
else :
    print("<")
'''
import random

dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)
dice3 = random.randint(1, 6)

#dice1, dice2, dice3 = map(int, input().split())

reward = 0

print(dice1, dice2, dice3)

if dice1 == dice2 == dice3:
  reward = 10000 + dice1*1000
  print("reward : ", reward)

#같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)×100원
elif dice1 == dice2 or dice1 == dice3:
  reward = 1000 + dice1*100
  print("reward : ", reward)

elif dice2 == dice3:
  reward = 1000 + dice2*100
  print("reward : ", reward)
else :
  reward = max(dice1, dice2, dice3)*100
  print("reward : ", reward)