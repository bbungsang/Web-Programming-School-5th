>٩(๑òωó๑)۶ 아, 아, 마이크 테스트<br>
이 마크다운은 빌루바노빅의 'Introducing Python'을 토대로 작성되었습니다.
제 기준 헷갈리는 개념을 위주로 다른 문서를 참고하여 이해하기 쉽도록 내용을 더하였습니다.

<br>
## 제너레이터
- 파이썬의 `iterator`를 생성하는 객체로, 전체 시퀀스를 한 번에 메모리에 저장하고 정렬할 필요 없이 잠재적으로 아주 큰 시퀀스를 순회할 수 있다.
- `iterator`는 next()를 이용해 데이터에 순차적으로 접근이 가능한 객체이다.
- 대표적인 제너레이터 중 하나로 `range()` 가 있다.

```python
>>> sum(range(1, 10))
5050
```
- 순회할 때마다 호출된 항목을 기억하고 다음 값을 반환한다. 즉 제너레이터는 이전 호출에 대한 메모리가 없는 일반 함수와 달리 이전 호출에 대해 기억하고 이전 값을 적용하여 반환한다.
- 제너레이터 컴프리헨션에 대한 코드가 긴 경우에는 제너레이터 함수를 사용하면 된다. 제너레이터 함수는 일반 함수지만 return 으로 값을 반환하지 않고, yield 로 값을 반환한다.

```python
>>> def my_range(first=0, last=10, step=1):
...   number = first
...   while number < last:
...     yield number
...     number += step
>>> my_range
<function my_range at 0x10193e268>

>>> ranger = my_range(1, 5)
>>> ranger
<generator object my_range at 0x101a0a168>

>>> for x in ranger:
...   print(x)
1
2
3
4
```

<br><br>
#### 제너레이터 컴프리헨션
- 제너레이터 함수를 더 쉽게 사용할 수 있도록 한다. 리스트 컴프리헨션과 비슷하지만 [] 대신 () 를 사용한다.

```python
>>> [ i for i in xrange(10) if i % 2 ]
[1, 3, 5, 7, 9]

>>> ( i for i in xrange(10) if i % 2 )
<generator object <genexpr> at 0x7f6105d90960>
```

<br><br>
#### 왜 제너레이터를 사용하는가?
\# 출처: http://bluese05.tistory.com/56
###### 1. 메모리를 효율적으로 사용할 수 있다.

```python
>>> sys.getsizeof( [i for i in xrange(100) if i % 2] )    # list
536
>>> sys.getsizeof( [i for i in xrange(1000) if i % 2] )
4280
>>> sys.getsizeof( (i for i in xrange(100) if i % 2) )    # generator
80
>>> sys.getsizeof( (i for i in xrange(1000) if i % 2) )
80
```
- 리스트의 경우 사이즈가 커질수록 메모리 사용량이 늘어난다. 하지만 제너레이터의 경우 사이즈가 커져도 메모리 사용량이 동일하다.
- 리스트는 안에 속한 모든 데이터를 메모리에 적재하기 때문에 리스트의 크기 만큼 메모리 사이즈가 늘어나게 되고, 제너레이터는 데이터를 next()를 통해 차례로 값에 접근할 때마다 메모리에 적재하기 때문에 메모리 사이즈가 일정한 것이다.

###### 2. **Lazy evaluation 계산 결과가 필요할 때까지 계산을 늦추는 효과를 볼 수 있다.**

```python
### 1초간 sleep을 수행한 후 x 값을 return ###
def sleep_func(x):
  print "sleep..."
  time.sleep(1)
  return x

### list 생성 ###
list = [sleep_func(x) for x in xrange(3)]
for i in list:
  print i
## result : ##
# sleep...
# sleep...
# sleep...
# 0
# 1
# 2

### generator 생성 ###
generator = (sleep_function(x) for x in xrange(3))
for i in generator:
  print i
## result : ##
# sleep...
# 0
# sleep...
# 1
# sleep...
# 2
```
- 리스트 컴프리헨션은 리스트의 모든 값을 먼저 수행하기 떄문에 리스트 값이 매우 큰 경우 그 만큼 부담으로 작용된다.
- 하지만 제너레이터 컴프리헨션은 실제 값을 로딩하지 않고 반복문이 수행 될 때마다 하나씩 sleep_func()을 수행하며 값을 불러온다. 즉, **수행 시간이 긴 연산을 필요한 순간까지 늦출 수 있다** 는 점이 있다.

###### 이러한 특징을 이용하면 피보나치 수열을 간결한 문법과 더불어 효율적으로 작성할 수 있다.
```python
def fibonacci(n):
    a, b = 0, 1
    i = 0
    while True:
        if(i > n):
            break
        yield a
        a, b = b, a+b
        i += 1

fib = fibonacci(10)
for x in fib:
    print(x)
```
