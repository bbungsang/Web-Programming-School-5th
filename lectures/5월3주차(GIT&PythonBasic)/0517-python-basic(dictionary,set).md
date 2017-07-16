## Python Basic

### 딕셔너리(Dictionary)
Key : Value 형태로 항목을 가지는 자료구조

```python
# 딕셔너리 생성
empty_dict1 = {}
empty_dict2 = dict()
teletubbies = {
  '보라돌이' : 'purple',
  '뚜비' : 'green',
  '나나' : 'yellow',
  '뽀' : 'red',
}

teletubbies['보라돌이']
# result : 'purple'

teletubbies['웨딩피치'] = 'pink'
# result : {'나나': 'yellow', '뚜비': 'green', '보라돌이': 'purple', '뽀': 'red', '웨딩피치': 'pink'}

teletubbies['보라돌이'] = 'violet'
# result : {'나나': 'yellow', '뚜비': 'green', '보라돌이': 'violet', '뽀': 'red', '웨딩피치': 'pink'}
```
중복을 허용하지 않음을 알 수 있다. key가 중복될 경우, 본래 key의 value가 바뀐다.

#### 결합(Update)
```python
new_dict = {
  '명탐정' : '코난',
  '피구왕' : '통키',
  '요리왕' : '비룡',
}  

teletubbies.update(new_dict)
# rusult :
{'나나': 'yellow',
'뚜비': 'green',
'명탐정': '코난',
'보라돌이': 'violet',
'뽀': 'red',
'요리왕': '비룡',
'웨딩피치': 'pink',
'피구왕': '통키'}

```
순서가 없음을 알 수 있다.

- **in :** key 검색, key가 있으면 True, 없으면 False를 반환한다.

`'나나' in teletubbies`

result : True

- **keys() :** 모든 key를 리스트 형태로 얻을 수 있다.

`teletubbies.keys()`

result : ['요리왕', '피구왕', '나나', '웨딩피치', '보라돌이', '뚜비', '명탐정', '뽀']

- **values() :** 모든 value를 리스트 형태로 얻을 수 있다.

`teletubbies.values()`

result : ['비룡', '통키', 'yellow', 'pink', 'violet', 'green', '코난', 'red']

- **items() :** 모든 key와 value를 튜플을 한 항목으로 하여 리스트 형태로 얻을 수 있다.

result : [('요리왕', '비룡'), ('피구왕', '통키'), ('나나', 'yellow'), ('웨딩피치', 'pink'), ('보라돌이', 'violet'), ('뚜비', 'green'), ('명탐정', '코난'), ('뽀', 'red')]

### 집합 자료형
딕셔너리의 key만 있는 형태, *순서가 없고 중복을 허용하지 않는다*

```python
## 집합 선언
set_exam = set([1, 2, 3])

## 값 하나 추가
set_exam.add(4)
# result : {1, 2, 3, 4}

## 값 여러개 추가
set_exam.update([5, 6, 7])
# result : {1, 2, 3, 4, 5, 6, 7}
```

집합은 **순서** 가 없어 인덱스를 이용해서 값을 참조할 수 없다. **리스트** 나 **튜플** 로 변환해야 인덱스를 이용한 참조를 할 수 있게된다.

```python
change_list = list(set_exam)

change_list[2]
# result : 3
```

## 집합 연산 (교집합, 합집합, 차집합)

```python
## 집합 선언
set1 = set([1,2,3])
set2 = set([2,4,5,6])
set3 = set() # 공집합

## set1과 set2의 교집합
set1 & set2
set1.intersection(set2)
# result : set([2])

## set1과 set2의 합집합
set1 | set2
set1.union(set2)
# result : set([1, 2, 3, 4, 5, 6])

## set1과 set2의 차집합
set1 - set2
set1.difference(set2)
# result : set([1, 3])
set2.difference(set1)
# result : set([4, 5, 6])

## set1과 set2의 합집합에서 교집합을 뺀 차집합
set1 ^ set2
# result : set([1, 3, 4, 5, 6])
```

### *정리*
- 집합은 순서가 없고 중복을 허용하지 않는다.
- 이 특징을 이용해서 리스트나 튜플의 중복을 제거할 수 있다.
- 순서가 없기 때문에 인덱스를 이용한 데이터를 참조하기위해서는 리스트나 튜플로 변환 후 사용해야 한다.
