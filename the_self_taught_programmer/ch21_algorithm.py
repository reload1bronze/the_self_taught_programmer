# 피즈버즈
def fizz_buzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


fizz_buzz()


# 순차 검색 (sequential search)
def ss(number_list, n):
    found = False
    for i in number_list:
        if i == n:
            found = True
            break
    return found


numbers = range(0, 100)
s1 = ss(numbers, 2)
print(s1)
s2 = ss(numbers, 202)
print(s2)


# 회문 (palindrome)
def is_palindrome(word):
    word = word.lower()
    return word[::-1] == word


print(is_palindrome("Nature"))
print(is_palindrome("Pop"))


# 애너그램 (anagram)
def is_anagram(word1, word2):
    word1 = word1.lower()
    word2 = word2.lower()
    print(sorted(word1))
    return sorted(word1) == sorted(word2)


print(is_anagram("iceman", "cinema"))
print(is_anagram("leaf", "tree"))


# 글자 세기
def count_characters(string):
    count_dict = {}
    for c in string:
        if c in count_dict:
            count_dict[c] += 1
        else:
            count_dict[c] = 1
    print(count_dict)


count_characters("apeach")


# 재귀 (recursion)
def bottles_of_beer(bob):
    """ 99 Bottle of Beer on the Wall의 가사를 출력합니다.
        매개변수 bob는 반드시 양의 정수여야 합니다
    """
    if bob < 1:
        print("""No more bottles of beer on the wall. No more bottles of beer.
        """)
        return
    tmp = bob
    bob -= 1
    print("""{} bottles of beer on the wall. {} bottles of beer.
Take one down, pass it aroundk, {} bottles of beer on the wall.
    """.format(tmp, tmp, bob))
    bottles_of_beer(bob)


bottles_of_beer(99)
