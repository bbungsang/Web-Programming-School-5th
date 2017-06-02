## **x만큼 간격이 있는 n개의 숫자**

number_generator함수는 x와 n을 입력 받습니다.
2와 5를 입력 받으면 2부터 시작해서 2씩 증가하는 숫자를 5개 가지는 리스트를 만들어서 리턴합니다.
[2,4,6,8,10]

4와 3을 입력 받으면 4부터 시작해서 4씩 증가하는 숫자를 3개 가지는 리스트를 만들어서 리턴합니다.
[4,8,12]

이를 일반화 하면 x부터 시작해서 x씩 증가하는 숫자를 n개 가지는 리스트를 리턴하도록 함수 number_generator를 완성하면 됩니다.

- 내가 푼 것^0^;

```python
def number_generator(x, n):
    list = []
    for i in range(n):
        data = x * (i + 1)
        list.append(data)
    return list

print(number_generator(3,5))
```

- 다른 사람 풀이

```python
def number_generator(x, n):
    return [i * x + x for i in range(n)]

print(number_generator(2, 5))
```



## **핸드폰 번호 가리기**

별이는 헬로월드텔레콤에서 고지서를 보내는 일을 하고 있습니다. 개인정보 보호를 위해 고객들의 전화번호는 맨 뒷자리 4자리를 제외한 나머지를 ` * ` 으로 바꿔야 합니다.
전화번호를 문자열 s로 입력받는 hide_numbers함수를 완성해 별이를 도와주세요
예를들어 s가 " 01033334444 " 면 ` *******4444 `를 리턴하고, " 027778888 "인 경우는 ` *****8888 `을 리턴하면 됩니다

- 내가 푼 것^0^;

```python
def hide_numbers(s):
    hide = len(s) - 4
    change = '*' * hide
    return s.replace(s[0:hide], change)

print("결과 : " + hide_numbers('01033334444'));
```



## **평균 구하기**

def average(list):
함수를 완성해서 매개변수 list의 평균값을 return하도록 만들어 보세요.
어떠한 크기의 list가 와도 평균값을 구할 수 있어야 합니다.

```python
def average(list):
    avg = 0
    sum = 0

    for i in list:
    	sum += i

    avg = sum / len(list)
    return avg

list = [5,3,4]
print("평균값 : {}".format(average(list)));
```

### 자릿수 더하기
sum_digit함수는 자연수를 전달 받아서 숫자의 각 자릿수의 합을 구해서 return합니다.
예를들어 number = 123이면 1 + 2 + 3 = 6을 return하면 됩니다.
sum_digit함수를 완성해보세요.

- 내가 푼 것^0^;

```python
def sum_digit(number):
    str_num = str(number)
    # bowl = ""
    sum = 0
    for i in range(len(str_num)):
        sum += int(str_num[i-1])
        # if i == len(str_num) - 1:
        #     bowl += str_num[i] + "="
        # else:
        #     bowl += str_num[i] + "+"

    return sum

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : {}".format(sum_digit(123)));
```

- 다른 사람 풀이

```python
def sum_digit(number):
    if number < 10:
        return number;
    return (number % 10) + sum_digit(number // 10)
```

```python
def average(list):
    avg = 0
    sum = 0

    for i in list:
    	sum += i

    avg = sum / len(list)
    return avg

list = [5,3,4]
print("평균값 : {}".format(average(list)));
```



## **정수 제곱근 판별하기**

nextSqaure함수는 정수 n을 매개변수로 입력받습니다.
n이 임의의 정수 x의 제곱이라면 x+1의 제곱을 리턴하고, n이 임의의 정수 x의 제곱이 아니라면 'no'을 리턴하는 함수를 완성하세요.
예를들어 n이 121이라면 이는 정수 11의 제곱이므로 (11+1)의 제곱인 144를 리턴하고, 3이라면 'no'을 리턴하면 됩니다.

- 내가 푼 것^0^;

```python
import math

def nextSqure(n):

    sqrt = n ** (1/2)
    if (sqrt % 1) == 0:
        return (sqrt + 1) ** 2
    return "no"

print("결과 : {}".format(nextSqure(169)));
```

- 다른 사람 풀이

```python
def nextSqure(n):
    from math import sqrt
    return "no" if sqrt(n) % 1 else (sqrt(n)+1)**2
```
