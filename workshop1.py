def enterKey():
    text = str(input("ใส่คำและเว้นวรรคทุกคำ: "))
    return text.split()

def convertlist(result):
    con_list = [str(element) for element in result]
    return con_list

def countSameText(afterbelist):
    list_count = {}
    for text in afterbelist:
        text_lower = text.lower()
        if text_lower in list_count:
            list_count[text_lower] += 1
        else:
            list_count[text_lower] = 1
    return list_count

def showTotalWordCount(afterbelist):
    total_word_count = len(afterbelist)
    print(f"คำทั้งหมดมี: {total_word_count} คำ")

def showResult(after_count_list):
    total_same_text_count = 0  # Initialize the total count
    for text, count in after_count_list.items():
        if count > 1:
            print(f"คำว่า: {text}, ซ้ำกัน: {count} ครั้ง")
            total_same_text_count += count  # Increment the total count
    return total_same_text_count  # Return the total count




result = enterKey()
afterbelist = convertlist(result)
after_count_list = countSameText(afterbelist)
showTotalWordCount(afterbelist)
total_same_text_count = showResult(after_count_list)
print(f"คำซ้ำทั้งหมดมี: {total_same_text_count} คำ")
