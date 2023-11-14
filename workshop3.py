def menu():
    print("1. หาพื้นที่สีเหลี่ยม กด 1")
    print("2. หาพื้นที่วงกลม กด 2")
    print("3. หาปริมาตรทรงสี่เหลี่ยม กด 3")
    print("4. หาปริมาตรทรงกลม กด 4")
    print("5. ออก กด 5")

def get_choice():
    while True:
        try:
            choice = int(input("เลือก: "))
            if 1 <= choice <= 5:
                return choice
            else:
                print("ไม่มีตัวเลือกนี้ใส่ 1-5")
        except ValueError:
            print("ใส่ได้แต่ตัวเลข")

def option1():
    print("You selected 1.")
    width = float(input("ป้อนความกว้างของสี่เหลี่ยม: "))
    length = float(input("ป้อนความยาวของสี่เหลี่ยม: "))
    area = width * length
    print(f"พื้นที่สี่เหลี่ยม: {area}")
def option2():
    print("You selected 2.")
    radius = float(input("ป้อนรัศมี: "))
    calcircle = 3.14 * radius ** 2
    print(f"พื้นที่วงกบม:{calcircle}")
def option3():
    print("You selected  3.")
    width = float(input("ป้อนความกว้าง: "))
    length = float(input("ป้อนความยาว: "))
    height = float(input("ป้อนความสูง: "))
    cal = width * length * height
    print(f"ปริมาตรสี่เหลี่ยม: {cal}")
def option4():
    print("You selected  4.")
    radius = float(input("ป้อนรัศมี: "))
    calcirclearea = 4/3 * 3.14 * radius ** 3
    print(f"ปริมาตรวงกลม:{calcirclearea}")
def main():
    while True:
        menu()
        choice = get_choice()

        if choice == 1:
            option1()
        elif choice == 2:
            option2()
        elif choice == 3:
            option3()
        elif choice == 4:
            option4()
        elif choice == 5:
            print("ออกแล้ว")
            break
        else:
            print("ไม่มีตัวเลือกนี้รองใหม่")

if __name__ == "__main__":
    main()
