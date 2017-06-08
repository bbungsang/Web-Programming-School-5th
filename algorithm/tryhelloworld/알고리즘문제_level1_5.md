## 딕셔너리 정렬
딕셔너리는 들어있는 값에 순서가 없지만, 키를 기준으로 정렬하고 싶습니다. 그래서 키와 값을 튜플로 구성하고, 이를 순서대로 리스트에 넣으려고 합니다.<br>
예를들어 {"김철수":78, "이하나":97, "정진원":88}이 있다면 각각의 키와 값을
- ("김철수", 78)
- ("이하나", 97)
- ("정진원", 88)

과 같이 튜플로 분리하고 키를 기준으로 정렬해서 다음과 같은 리스트를 만들면 됩니다.<br>
[ ("김철수", 78), ("이하나", 97), ("정진원", 88) ]<br>

다음 sort_dictionary 함수를 완성해 보세요.

- 내가 푼 것 ^0^/

```python
def sort_dictionary(dic):
    re_arrange = []
    sort_name = sorted(tuple(dic))
    for i in range(len(sort_name)):
    	re_arrange.append((sort_name[i], dic[sort_name[i]]))
    return re_arrange

print( sort_dictionary( {"김철수":78, "이하나":97, "정진원":88} ))
```

- 다른 사람 풀이

```python
def sort_dictionary(dic):
    return sorted(dic.items(), key=lambda x: x[0])
```
<br><br>
## 같은 숫자는 싫어
no_continuous함수는 스트링 s를 매개변수로 입력받습니다.<br>

s의 글자들의 순서를 유지하면서, 글자들 중 연속적으로 나타나는 아이템은 제거된 배열(파이썬은 list)을 리턴하도록 함수를 완성하세요.<br>
예를들어 다음과 같이 동작하면 됩니다.<br>

s가 '133303'이라면 ['1', '3', '0', '3']를 리턴<br>
s가 '47330'이라면 [4, 7, 3, 0]을 리턴<br>

- 내가 푼 것 ^0^/

```python
def no_continuous(s):
    bowl = [s[0]]
    num_value = s[0]
    for i in range(1, len(s)):
        if num_value != s[i]:
            num_value = s[i]
            bowl.append(num_value)

    return bowl

print( no_continuous( "133303" ))
```

- 다른 사람 풀이

```python
def no_continuous(s):
    # 함수를 완성하세요
    return [s[i] for i in range(len(s)) if s[i] != s[i+1:i+2]]
```
