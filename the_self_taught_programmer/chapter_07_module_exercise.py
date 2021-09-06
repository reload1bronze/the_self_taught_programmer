import statistics
import chapter_07_module_cubed

# 1
# statistics 모듈의 함수 연습해보기
list_num = [1, 23, 185, 319, 485, 39, 40, 835, 319]

# 평균값 : 리스트 모든 숫자의 합 / 전체 개수 - arithmetic mean (average)
print(statistics.mean(list_num))
# 중간값 : 리스트 숫자를 크기 순으로 나열하였을 때 중간에 있는 값 (전체 개수가 짝수이면 중간 두 개 값의 평균값) - median (middle value)
print(statistics.median(list_num))
# 최빈값 : 가장 많이 등장하는 값 - single mode (most common value)
print(statistics.mode(list_num))
# 표준 편차 : 분산(편차들의 제곱합에서 얻어진 값의 평균치)의 제곱근 - standard deviation
print(statistics.stdev(list_num))

# 2
# 다른 모듈에서 숫자를 받고 제곱해서 반환하는 함수를 만들고, 임포트해서 그 함수를 호출
input_num = int(input("숫자를 입력하세요"))
print(chapter_07_module_cubed.cubed(input_num))
