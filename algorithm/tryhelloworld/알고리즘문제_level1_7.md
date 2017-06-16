## 피보나치 수
피보나치 수는 F(0) = 0, F(1) = 1일 때, 2 이상의 n에 대하여 F(n) = F(n-1) + F(n-2) 가 적용되는 점화식입니다.
2 이상의 n이 입력되었을 때, fibonacci 함수를 제작하여 n번째 피보나치 수를 반환해 주세요.
예를 들어 n = 3이라면 2를 반환해주면 됩니다.

### 내 풀이
```python
def fibonacci(num):
    a, b = 0, 1
    i = 0
    while True:
        result = b-a
        if(i > num):
            return result
        a, b = b, a+b
        i += 1

print(fibonacci(5))
```

### 다른 사람 풀이
```python
def fibonacci(num):
    a, b = 0, 1
    for i in range(num):
        a, b = b, a+b
    return a
```
## 약수의 합
어떤 수를 입력받아 그 수의 약수를 모두 더한 수 sumDivisor 함수를 완성해 보세요.
예를 들어 12가 입력된다면 12의 약수는 [1, 2, 3, 4, 6, 12]가 되고, 총 합은 28이 되므로 28을 반환해 주면 됩니다.

### 내 풀이
```python
from functools import reduce

def sumDivisor(num):
    divisor = []
    for i in range(num):
        if num % (i+1) == 0:
            divisor.append(i+1)
    return reduce(lambda x, y: x + y, divisor)
```

### 다른 사람 풀이
```python
def sumDivisor(num):
    return sum([ i for i in range(1,num+1) if num%i==0])
```
