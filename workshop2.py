import random

def Randomnumber():
    random_number = random.randint(1, 100)
    return random_number

def InputNum():
    while True:
        try:
            guess_number = int(input("ป้อนตัวเลข (1-100): "))
            if 1 <= guess_number <= 100:
             return guess_number
        except ValueError:
            print("ใส่ตัวเลขอย่าให้มีตรั้งที่ 2 ")


def CheckNum(random_number, guess_number):
    if guess_number == random_number:
        print("----------YAY----------------")
        print("-Correct, You are the winner-")
    elif guess_number < random_number:
        print("-- ไม่ถูกกกกกกก  !!!      --")
        print("--   NT มากกว่า! --")
    else:
        print("-- ไม่ถูกกกกกกก  !!!       --")
        print("--  NT น้อยกว่า!  --")

def showResult(random_number):
    print(f"เฉลย: {random_number}")

print("-----------------------------")
print("      GUESE IT IF U CAN      ")
print("-----------------------------")

random_number = Randomnumber()
guess_number = InputNum()
CheckNum(random_number, guess_number)
showResult(random_number)
