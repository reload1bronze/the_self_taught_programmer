# 1
# 문자열 "Adventurer"의 문자를 모두 출력하기
name = "Adventurer"
for i in range(0, len(name)):
    print(name[i])
# 잘한 부분: for 문을 활용하여 일일이 하드코딩 하지 않음

# 2
# 문자열 2개를 입력받아서 기존 문자열에 추가하여 출력하기
input_one = input("어제 무엇을 작성하셨나요?")
input_two = input("누구에게 보내셨나요?")
input_result = "Yesterday I wrote a {}. I sent it to {}".format(input_one, input_two)
print(input_result)

# 3
# 첫글자만 대문자로 변경하기
result_cap = "aldous Huxley was born in 1894".capitalize()
print(result_cap)

# 4
# 문자열을 리스트로 변환
split_list = "Where now? Who now? When now?".split("? ")
split_list[0] = split_list[0] + "?"
split_list[1] = split_list[1] + "?"
print(split_list)
# 미흡한 부분: 물음표를 하드코딩해서 넣어줘야 함

# 5
# 단어 리스트 하나로 조인하기
word_list = ["The", "fox", "jumped", "over", "the", "fence", "."]
process_sentence = " ".join(word_list)
result_sentence = process_sentence.replace(" .", ".")
print(result_sentence)
# 미흡한 부분: 마지막 쉼표 앞 띄어쓰기를 없애는 코드가 한 줄 들어감

# 6
# 문자열 내 특정 문자 치환
result_change = "A screaming comes across the sky.".replace("s", "$")
print(result_change)

# 7
result_index = "Hemingway".index("m")
print(result_index)

# 9
list_test = ["three", "three", "three"]
result_list = " ".join(list_test)
print(result_list)

result_three = "three " * 3
print(result_three)
# 미흡한 부분: 마지막에 띄어쓰기가 들어감

# 10
# 쉼표 앞에 있는 문자들만 남기기
sentence = "It was a bright cold day in April, and the clocks were striking thirteen."
find_index = sentence.index(",")
result_slice = sentence[:find_index]
print(result_slice)
