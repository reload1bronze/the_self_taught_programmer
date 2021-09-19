import csv

st = open("st.txt", "w")
st.write("Hi from Python!!!")
st.close()

with open("stt.txt", "w") as f:
    f.write("Hello from Python!")

with open("st.csv", "w", newline='') as f:
    write = csv.writer(f, delimiter=",")
    write.writerow(["one", "two", "three"])
    write.writerow(["four", "five", "six"])

with open("st.csv", "r") as f:
    read = csv.reader(f, delimiter=",")
    for row in read:
        print(",".join(row))

# 1
# 다른 폴더의 파일을 찾아 내용을 출력
with open("C:/Program Files/Android/Android Studio/NOTICE.txt") as f:
    print(f.read())

# 2
# 사용자에게 질문하고, 응답을 파일에 저장하는 프로그램 작성
with open("favorite_food.csv", "w") as f:
    write = csv.writer(f, delimiter=",")
    while True:
        answer = input("좋아하는 음식은? (\"q\"입력시 종료됩니다)")
        if answer == "q":
            break
        else:
            write.writerow(answer)

# 3
# 중첩된 리스트의 요소를 CSV 파일에 저장
with open("movie_list", "w") as f:
    write = csv.writer(f, delimiter=",")
    original_lists = [["Top Gun", "Risky Business", "Minority Report"], ["Titanic", "The Revenant", "Inception"],
                      ["Training Day", "Man on Fire", "Flight"]]
    for nested_list in original_lists:
        write.writerow(nested_list)
