###### 1. 숫자를 입력받아 해당하는 숫자 단수를 튜플 리스트로 결과를 저장하는 함수 make_gugu(num) 함수 작성
ex) make_gugu(3) -> return [(3,1,3), (3,2,6), ....(3,9,27)]

```python

# 함수를 활용한 구구단 만들기

def make_gugu(num):
    result = []
    for i in range(1, 10):
        result.append((num, i, num*i))
    return result

make_gugu(3)

''' 출력 결과 :
[(3, 1, 3),
 (3, 2, 6),
 (3, 3, 9),
 (3, 4, 12),
 (3, 5, 15),
 (3, 6, 18),
 (3, 7, 21),
 (3, 8, 24),
 (3, 9, 27)]
'''
```

###### 2. 매개변수 print_type과 gugu_list를 가지며,  print_type에 따라 gugu_list를 단순출력 또는 '{} x {} = {}'형으로 출력해주는 함수 print_gugu(print_type, gugu_list) 작성
ex) print_gugu('simple', <어떤리스트>) -> print((3,1,3),(3,2,6)...)
print_type은 'simple'과 'normal'로 나눠지며, simple은 튜플을 그냥 출력, normal은 위의 format string 형태로 출력

```python
def print_gugu(print_type, gugu_list):
    if print_type == 'simple':
        print(make_gugu(gugu_list))
    elif print_type == 'normal':
        for i in make_gugu(gugu_list):
            print('{} X {} = {}'.format(i[0], i[1], i[2]))

        '''선생님이 한 방법
        for x, y, z in make_gugu(gugu_list):
            print( '{} X {} = {}'.format(x, y, z) )
        '''

print_gugu('normal', 3)

''' 출력 결과 :
3 X 1 = 3
3 X 2 = 6
3 X 3 = 9
3 X 4 = 12
3 X 5 = 15
3 X 6 = 18
3 X 7 = 21
3 X 8 = 24
3 X 9 = 27
'''
```

###### 3. 매개변수 range, print_type, make_gugu_function, print_gugu_function을 이용하여 range에 해당하는 범위의 구구단을 생성하고 출력하는 함수 gugu작성
작성한 함수에서는 매 단마다 줄바꿈 및 이번이 몇 단인지를 알려주는 문자열을 출력 `_function`으로 끝나는 매개변수는 함수 자체를 전달

ex) gugu(range(3,7), 'normal', make_gugu, print_gugu)

```python
def decorate_gugu(ranges, print_type):
    if ranges == 0:
        return "끝~"

    print("==== " + str(ranges) + "단 ====")
    print_gugu(print_type, ranges)

    return decorate_gugu(ranges - 1, print_type)

decorate_gugu(3, "normal")

''' 출력 결과 :
==== 3단 ====
3 X 1 = 3
3 X 2 = 6
3 X 3 = 9
3 X 4 = 12
3 X 5 = 15
3 X 6 = 18
3 X 7 = 21
3 X 8 = 24
3 X 9 = 27
==== 2단 ====
2 X 1 = 2
2 X 2 = 4
2 X 3 = 6
2 X 4 = 8
2 X 5 = 10
2 X 6 = 12
2 X 7 = 14
2 X 8 = 16
2 X 9 = 18
==== 1단 ====
1 X 1 = 1
1 X 2 = 2
1 X 3 = 3
1 X 4 = 4
1 X 5 = 5
1 X 6 = 6
1 X 7 = 7
1 X 8 = 8
1 X 9 = 9

'끝~'
'''
```
