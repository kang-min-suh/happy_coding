# 함수를 명확하게 사용하기 
import math
def circle_area(radius): 
    result = round(radius**2*math.pi,2)
    # float는 안쓰고 round() 함수만으로 소수점 둘째자리까지 쓰는 거 표현됨. 
    return result

# 함수밖에서 입력변수 설정 
radius = float(input("반지름 값을 입력하세요: "))
# 소수값도 받으려면 int형이 아니라 float형으로 받아야 한다. 
# int()는 input()나온 문자열 중에서 정수형태만 받을 수 있다!!! 
print(circle_area(radius))
