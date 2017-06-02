## 짝수와 홀수
evenOrOdd 메소드는 int형 num을 매개변수로 받습니다.<br>
num이 짝수일 경우 "Even"을 반환하고 홀수인 경우 "Odd"를 반환하도록 evenOrOdd에 코드를 작성해 보세요.<br>
num은 0이상의 정수이며, num이 음수인 경우는 없습니다.

- 내가 푼 것 ^0^/

```python
def evenOrOdd(num):
  return "Even" if num % 2 == 0 else "Odd"

print("결과 : " + evenOrOdd(3))
print("결과 : " + evenOrOdd(2))
```

- 다른 사람 풀이

```python
def evenOrOdd(num):
    return num % 2 and "Odd" or "Even"
```
<br><br>

## 제일 작은 수 제거하기
rm_small함수는 list타입 변수 mylist을 매개변수로 입력받습니다.<br>
mylist 에서 가장 작은 수를 제거한 리스트를 리턴하고, mylist의 원소가 1개 이하인 경우는 []를 리턴하는 함수를 완성하세요.<br>
예를들어 mylist가 [4,3,2,1]인 경우는 [4,3,2]를 리턴 하고, [10, 8, 22]면 [10, 22]를 리턴 합니다.

- 내가 푼 것 ^0^/

```python
def rm_small(mylist):
    min = 0
    if len(mylist) <= 1:
    	mylist = []
    else:
        min = mylist[0]

        for i in range(len(mylist)):
            if min > mylist[i]:
                min = mylist[i]

        mylist.remove(min)

    return mylist

my_list = [1, 2, 3, 4]
print("결과 {} ".format(rm_small(my_list)))
```

- 다른 사람 풀이

```python
def rm_small(mylist):
    return [i for i in mylist if i > min(mylist)]
```

```python
def rm_small(mylist):
    del(mylist[mylist.index(min(mylist))])
    return mylist
```


## 정수제곱근 판별하기
nextSqaure함수는 정수 n을 매개변수로 입력받습니다.<br>
n이 임의의 정수 x의 제곱이라면 x+1의 제곱을 리턴하고, n이 임의의 정수 x의 제곱이 아니라면 'no'을 리턴하는 함수를 완성하세요.<br>
예를들어 n이 121이라면 이는 정수 11의 제곱이므로 (11+1)의 제곱인 144를 리턴하고, 3이라면 'no'을 리턴하면 됩니다.

- 내가 푼 것 ^0^/

```python
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
    for x in range(1,n) :
        if x ** 2 == n :
            return (x+1) ** 2
    return "no"
```
