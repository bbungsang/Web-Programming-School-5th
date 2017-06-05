## 문자열 다루기 기본
alpha_string46함수는 문자열 s를 매개변수로 입력받습니다.<br>
s의 길이가 4혹은 6이고, 숫자로만 구성되있는지 확인해주는 함수를 완성하세요.<br>
예를들어 s가 "a234"이면 False를 리턴하고 "1234"라면 True를 리턴하면 됩니다<br>

- 내가 푼 것 ^0^/

```python
def alpha_string46(s):
    num_list = []
    for i in range(0, 10):
        num_list.append(str(i))

    if len(s) != 4 and len(s) != 6:
        return False

    for j in range(len(s)):
        if s[j] not in num_list:
            return False
    return True

print( alpha_string46("a23415") )
print( alpha_string46("031779") )
```

- 다른 사람 풀이

```python
def alpha_string46(s):
    return s.isdigit() and len(s) in [4, 6]
```
<br><br>
## 문자열 내 p와 y의 개수
numPY함수는 대문자와 소문자가 섞여있는 문자열 s를 매개변수로 입력받습니다.<br>
s에 'p'의 개수와 'y'의 개수를 비교해 같으면 True, 다르면 False를 리턴하도록 함수를 완성하세요. 'p', 'y' 모두 하나도 없는 경우는 항상 True를 리턴합니다.<br>
예를들어 s가 "pPoooyY"면 True를 리턴하고 "Pyy"라면 False를 리턴합니다.<br>

- 내가 푼 것 ^0^/

```python
def numPY(s):
	p_count = 0
	y_count = 0

	for i in s:
		if i == "p" or i == "P":
			p_count += 1
		elif i == "y" or i == "Y":
			y_count += 1
	print(p_count, y_count)

	if p_count == y_count:
		return True
	return False

print( numPY("YbYYYpppEPRm") )
print( numPY("Pyy") )
```

- 다른 사람 풀이

```python
def numPY(s):
    return s.lower().count('p') == s.lower().count('y')
```
<br><br>
#### *소감*
- 이번 알고리즘은 내 기준에서 매우 어려웠다. 코드 엄청 긴 것 보소>.0 그에 비해 다른 사람이 한 줄로 풀어낸 것을 보노라면 어김없이 현타가 찾아온다. 
