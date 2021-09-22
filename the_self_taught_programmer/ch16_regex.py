import re

zen = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

# 단순 일치
m1 = re.findall("simple", zen, re.IGNORECASE)
print(m1)

# 처음과 끝에 일치 - ^, $
m2 = re.findall("^if", zen, re.MULTILINE)
print(m2)

m2 = re.findall("idea.$", zen, re.MULTILINE)
print(m2)

# 여러 문자에 일치 - []
string = "Two too."
m3 = re.findall("t[ow]o", string, re.IGNORECASE)
print(m3)

# 숫자 찾기 - \d
line = "123?34 hell?"
m4 = re.findall("\d", line)
print(m4)

# 반복 - *
line = "two twoo not too."
m5 = re.findall("two*", line)
print(m5)

# 적극적, 탐욕적(greedy)
line = "__hello__there"
m6 = re.findall("__.*__", line)
print(m6)

# 소극적, 게으른(non-greedy)
line = "__one__ __two__ __three__"
results = re.findall("__.*?__", line)
for match in results:
    print(match)

# 이스케이프
line = "I love $"
m7 = re.findall("\\$", line, re.IGNORECASE)
print(m7)
