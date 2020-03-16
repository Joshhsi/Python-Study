import random
rang1 = int(input("請設定本局遊戲的最小值:"))
rang2 = int(input("請設定本局遊戲的最大值:"))
num = random.randint(rang1,rang2)
guess = "guess"
print("數字猜謎遊戲！")
i = 0
while guess != num:
    i += 1
    guess = int(input("請輸入你猜的數字："))

    if guess == num:
        print("恭喜，你猜對了！")
    elif guess < num:
        print("你猜的數小了...")
    else:
        print("你猜的數大了...")

print("你總共猜了%d" %i + "次",end = '')
print(",快和你朋友較量一下...")