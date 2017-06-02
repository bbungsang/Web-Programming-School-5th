## **자릿수더하기**
sum_digit함수는 자연수를 전달 받아서 숫자의 각 자릿수의 합을 구해서 return합니다.<br>
예를들어 number = 123이면 1 + 2 + 3 = 6을 return하면 됩니다.<br>
sum_digit함수를 완성해보세요.

- 내가 푼 것 ^0^/

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

print("결과 : {}".format(sum_digit(6783)));   
```

- 다른 사람 풀이

```python
def sum_digit(number):
    if number < 10:
        return number;
    return (number % 10) + sum_digit(number // 10)
```
> 얼.. 재귀함수..0V0b

## **스트링을 숫자로 바꾸기**
strToInt 메소드는 String형 str을 매개변수로 받습니다.<br>
str을 숫자로 변환한 결과를 반환하도록 strToInt를 완성하세요.<br>
예를들어 str이 "1234"이면 1234를 반환하고, "-1234"이면 -1234를 반환하면 됩니다.<br>
str은 부호(+,-)와 숫자로만 구성되어 있고, 잘못된 값이 입력되는 경우는 없습니다.

- 내가 푼 것 ^0^/

```python
def strToInt(String str):
    if type(str) == str:
    	return int(str)
    else:
        return str(str)

print(strToInt(-25));
```

## **수박수박수박수박수박수?**

water_melon함수는 정수 n을 매개변수로 입력받습니다.<br>
길이가 n이고, 수박수박수...와 같은 패턴을 유지하는 문자열을 리턴하도록 함수를 완성하세요.<br>
예를들어 n이 4이면 '수박수박'을 리턴하고 3이라면 '수박수'를 리턴하면 됩니다.

- 내가 푼 것 ^0^/

```python
def water_melon(n):
    bowl = []
    su = "수"
    bak = "박"

    for i in range(1, n+1):
        if i % 2 == 0:
            bowl.append(bak)
        else:
            bowl.append(su)

    result = ''.join(bowl)

    return result

print("n이 3인 경우: " + water_melon(3));
print("n이 4인 경우: " + water_melon(4));
```

- 다른 사람 풀이

```python
def water_melon(n):
    s = "수박" * n
    return s[:n]
```

> 허무하게도 저렇게 간단한 방법이 있었다니... 분발해야겠다.



## 서울에서 김서방 찾기
findKim 함수는 String형 배열 seoul을 매개변수로 받습니다.<br>
seoul의 element중 "Kim"의 위치 x를 찾아, "김서방은 x에 있다"는 String을 반환하세요.<br>
seoul에 "Kim"은 오직 한 번만 나타나며 잘못된 값이 입력되는 경우는 없습니다.

- 내가 푼 것 ^0^/

```python
def findKim(seoul):
    kimIdx = 0
    for i in range(len(seoul)):
        if seoul[i] == "Kim":
            kimIdx = i

    return "김서방은 {}에 있다".format(kimIdx)

print(findKim(["Queen", "Tod", "Kim"]))

```

- 다른 사람 풀이

```python
def findKim(seoul):
    return "김서방은 {}에 있다".format(seoul.index('Kim'))
```


## 삼각형 출력하기
printTriangle 메소드는 양의 정수 num을 매개변수로 입력받습니다.<br>
다음을 참고해 `*(별)`로 높이가 num인 삼각형을 문자열로 리턴하는 printTriangle 메소드를 완성하세요.<br>
printTriangle이 return하는 String은 개행문자('\n')로 끝나야 합니다.

- 내가 푼 것 ^0^/

```python
def printTriangle(num):
	star_list = []
	for i in range(1, num + 1):
            star_list.append("*" * i + "\n")

	return ''.join(star_list)

print( printTriangle(5) )
```

- 다른 사람 풀이

```python
def printTriangle(num):
    return ''.join(['*'*i + '\n' for i in range(1,num+1)])
```

> 내가 푸는 방식은 아무래도 파이써닉함에서 한참 벗어나는 것 같다. 알고리즘을 단계별로 차차 풀어나가고 다른 사람 풀이도 열심히 참고하여 문법을 익히는 게 우선인 듯 하다.
