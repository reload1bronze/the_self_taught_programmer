# 1
# 리스트의 각 요소 출력하기
list_words = ["The Walking Dead", "Entourage", "The Sopranos", "The Vampire Diaries"]
for word in list_words:
    print(word)

# 2
# 25 부터 50 까지 숫자 출력
for i in range(25, 51):
    print(i)

# 3
# 1번 문제의 인덱스와 요소 모두 출력
for i, word in enumerate(list_words):
    print("{} 번째 단어는 {}".format(i, word))

# 4
# 무한 루프가 생기는 프로그램
list_number = ["3"]
result = True
while result:
    answer = input("한 자리 숫자를 입력해주세요 ('q' 입력시 종료됩니다)")
    # 주의: input 으로 들어온 값은 '숫자'가 아니라 '문자'임
    if answer in list_number:
        result = False
    if answer == "q":
        result = False

# 5
# 두 개의 리스트 각 요소를 곱한 결과로 리스트 만들기
list_one = [8, 19, 148, 4]
list_two = [9, 1, 33, 83]
result = []
for num in list_one:
    index = list_one.index(num)
    result.append(num * list_two[index])
print(result)
