>٩(๑òωó๑)۶ 아, 아, 마이크 테스트<br>
이 마크다운은 빌루바노빅의 'Introducing Python'을 토대로 작성되었습니다.
제 기준 헷갈리는 개념을 위주로 다른 문서를 참고하여 이해하기 쉽도록 내용을 더하였습니다.

<br>
## 컴프리헨션
- 사전적 의미 : 이해력
- 컴퓨터적 의미 : 함축, 하나 이상의 이터레이터(리스트, 튜플...)로 부터 코드를 절약한 자료구조를 만드는 방법

<br>
#### 리스트 컴프리헨션
> 1부터 5까지 정수 리스트를 만드는 데에는 아래와 같은 방법들이 있다.

```python
# 1. 일반 루프 방식
>>> num_list = []
>>> for num in range(1, 6):
...   num_list.append(num)
>>> num_list
[1, 2, 3, 4, 5]

# 2. 리스트 컴프리헨션 사용
>>> num_list = list(range(1, 6))
>>> num_list
[1, 2, 3, 4, 5]
```
- 이들 접근 방식은 동일한 결과를 생성한다. 하지만 **리스트 컴프리헨션** 을 사용해서 리스트를 만드는 것이 조금 더 파이써닉한 방법이라고 할 수 있다.
<br><br>

> [표현식 for 항목 in 순회 가능한 객체]

```python
>>> num_list = [num-1 for num in range(1, 6)]
```
- 리스트에 대한 값을 생성하는 `첫 번째 num` 변수(표현식)는 루프의 결과에 주어진 연산식을 적용하여 num_list 변수에 넣어준다.
- `두 번째 num` 변수는 단순히 for문의 일부이다.
<br><br>

> [표현식 for 항목 in 순회 가능한 객체 if 조건]

```python
>>> num_list = [num for num in range(1, 6) if num % 2 == 1]
>>> num_list
[1, 3, 5]
```
- `num % 2 == 1` 은 홀수일 때 True 짝수일 때 False를 도출하여 True 값인 홀수를 생성한다.
<br><br>

> 하나 이상의 중첩 for문도 사용할 수 있다.

```python
>>> rows = range(1, 4)
>>> cols = range(1, 3)
>>> cells = [(row, col) for row in rows for col in cols]
>>> for cell in cells:
...   print(cell)
(1, 1)
(1, 2)
(2, 1)
(2, 2)
(3, 1)
(3, 2)
```

<br>
#### 딕셔너리 컴프리헨션
- 딕셔너리 형태로 값을 반환받는 것을 제외하고 리스트 컴프리헨션과 거의 흡사하다.

> {키표현식 : 값표현식 for 항목 in 순회 가능한 객체}

```python
>>> word = 'letters'
>>> letter_counts = {letter: word.count(letter) for letter in word}
>>> letter_counts
{'l': 1, 'e' : 2, 't' : 2, 'r' : 1, 's' : 1}
```
- 첫 번째 letter 변수는 Key로서 for문으로부터 순차적으로 문자열을 받는다.
- word.count(letter) 는 Value로서 첫 번째 letter 변수에서 받은 문자열을 세어 정수로 반환한다.
- 하지만 이 방식으로 문자열을 셀 경우, 'e'와 't'는 두 번씩 순회하며 세기 때문에 시간 낭비를 초래할 수 있다.
- `{letter: word.count(letter) for letter in set(word)}` 면 시간 낭비를 줄이고 조금 더 파이써닉하게 처리할 수 있다.

<br><br>
#### *결론*
- 컴프리헨션은 이전 예제보다 간단하지 않지만, 더 많은 것을 간단한 원리로 표현할 수 있도록 해준다.
