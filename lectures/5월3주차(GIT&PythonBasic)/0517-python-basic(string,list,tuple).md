## Python Basic ##

#### Split
`<문자열 변수>.split('구분자')`
- 문자열을 리스트 타입으로 반환한다.
- 인자를 주지 않을 경우, 공백문자를 구분자로 사용한다.

#### Join
`'구분자'.join(<문자열 변수>)`
- 리스트를 하나의 문자열로 결합한다.

#### 대소문자
`<문자열 변수>.upper()`
- 대문자로 변환
`<문자열 변수>.lower()`
- 소문자로 변환

#### List
리스트는 순차적인 데이터를 나타내는 데 유용하며, 문자여로가 달리 원소를 변경할 수 있다.

```python
# 리스트의 생성
empty_list1 = []
empty_list2 = list()
sample_list = ['a', 'b', 'c']
```

- **슬라이스 :** 리스트[start : end : step]

- **append :** 리스트에 원소 추가, 리스트로 할당된 변수에 또 다른 리스트로 할당된 변수를 'append'하면 리스트 안에 리스트가 중복 삽입된다. `<리스트1>.append(<리스트2>)`

- **extend :** 마찬가지로 리스트에 원소 추가, 하지만 리스트에 리스트를 'extend'하면 병합되어 리스트 중복을 피할 수 있다. `<리스트1>.extend(<리스트2>)`  
<!-- 즉, 내용을 ` `하면 중복된 부분은 탈락된다. -->
- **remove :** 값으로 리스트 항목 삭제, 중복되는 값이 하나의 리스트에 여러 개 존재하더라도 그 첫번째 값만 삭제한다.
`<list>.remove('value')`

- **index :** 값으로 리스트 오프셋 찾기, 마찬가지로 중복되는 값이 하나의 리스트에 여러 개 존재하더라도 그 첫번째 항목의 오프셋만 찾을 수 있다. `<리스트>.index('value')`

- **in :** 존재여부 확인, 존재하면 True, 존재하지 않으면 False를 반환한다. `'value' in <list>`

- **count :** 리스트 안의 값을 센다.

#### Tuple
리스트와 비슷하나, 내부 항목의 삭제나 수정이 불가능하다.

```python
#빈 튜플의 생성
empty_tuple = ()
# 튜플이 하나의 항목만 가질 경우, 쉼표로서 튜플임을 명시한다.
colors = 'red',
fruits = 'apple', 'banana',
```

- **튜플 언패킹 :** 튜플 항목의 값을 각 변수에 할당한다. `f1, f2 = fruits`

- **튜플을 사용하는 이유**
  - 리스트보다 적은 메모리 사용
  - 정의 후에는 변하지 않는 내부 값

### *실습*
1 . 문자열 'Fastcampus'를 리스트, 튜플 타이으로 형편환하여 새 변수에 할당한다.

```python
  fc_string = 'Fastcampus'
  # 출력 결과 : Fastcampus

  fc_tuple = tuple(fc_string) # tuple('스트링형으로^^*')
  # 출력 결과 : ('F', 'a', 's', 't', 'c', 'a', 'm', 'p', 'u', 's')

  fc_list = list(fc_tuple)
  # 출력 결과 : ['F', 'a', 's', 't', 'c', 'a', 'm', 'p', 'u', 's']
```

2 . 1번에서 할당한 리스트, 튜플 변수를 이용해 다시 문자열을 만든다.

```python
  change_fc_string = ''.join(fc_list)
  # 출력 결과 : 'Fastcampus'

  change_fc_string = ''.join(fc_tuple)
  # 출력 결과 : 'Fastcampus'
```
