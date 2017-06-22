## 최솟값 만들기
자연수로 이루어진 길이가 같은 수열 A,B가 있습니다. 최솟값 만들기는 A, B에서 각각 한 개의 숫자를 뽑아 두 수를 곱한 값을 누적하여 더합니다. 이러한 과정을 수열의 길이만큼 반복하여 최종적으로 누적된 값이 최소가 되도록 만드는 것이 목표입니다.<br>

예를 들어 A = [1, 2] , B = [3, 4] 라면, <br>
1. A에서 1, B에서 4를 뽑아 곱하여 더합니다.
2. A에서 2, B에서 3을 뽑아 곱하여 더합니다.

수열의 길이만큼 반복하여 최솟값 10을 얻을 수 있으며, 이 10이 최솟값이 됩니다.
수열 A,B가 주어질 때, 최솟값을 반환해주는 getMinSum 함수를 완성하세요.

- 내가 푼 것

```python
def getMinSum(A,B):
    A = sorted(A)
    B = sorted(B)
    B.reverse()
    return sum([a * b for a, b in list(zip(A, B))])

print(getMinSum([1,2],[3,4]))
```

- 다른 사람 풀이

```python
def getMinSum(A,B):
    answer = 0
    A.sort()
    B.sort(reverse=True)
    for i in range(len(A)):
        answer += A[i]*B[i]

    return answer
```

## 2016년

2016년 1월 1일은 금요일입니다. 2016년 A월 B일은 무슨 요일일까요? 두 수 A,B를 입력받아 A월 B일이 무슨 요일인지 출력하는 getDayName 함수를 완성하세요. 요일의 이름은 일요일부터 토요일까지 각각 <br>

`SUN,MON,TUE,WED,THU,FRI,SAT` <br>

를 출력해주면 됩니다. 예를 들어 A=5, B=24가 입력된다면 5월 24일은 화요일이므로 `TUE`를 반환하면 됩니다.

- 내가 푼 것

```python
from datetime import date

def getDayName(a,b):
    week_list = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    week_int = date(2016, a, b).weekday()
    return week_list[week_int]
```

- 다른 사람 풀이

```python
import datetime

def getDayName(a,b):
    dayname = ['FRI','SAT','SUN', 'MON', 'TUE', 'WED', 'THU']
    a=datetime.date(2016,a,b)
    b=datetime.date(2016,1,1)
    day = (a-b).days
    answer = dayname[int(day%7)]
    return answer
```
