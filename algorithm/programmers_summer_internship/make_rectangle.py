'''
직사각형을 만드는 데 필요한 4개의 점 중 3개의 좌표가 주어질 때, 나머지 한 점의 좌표를 반환하는 solution 함수를 완성해 주세요.
단, 직사각형의 각 변은 x축, 혹은 y축에 평행하며, 반드시 직사각형을 만들 수 있는 경우만 입력으로 주어집니다.
입출력 예)

입력 : [[1, 4], [3, 4], [3, 10]]
출력 : [1, 10]

입력 : [[1, 1], [2, 2], [1, 2]]
출력 : [2, 1]
'''

def make_rectangle(q_list=[]):
    bowl = []
    for i in range(len(q_list)):
        for j in range(len(q_list)-1):
            bowl.append(q_list[i][j])

    x_value = bowl[0::2]
    y_value = bowl[1::2]

    for k in range(3):
        if x_value.count(x_value[k]) != 2:
            result_x = x_value[k]
        elif y_value.count(y_value[k]) != 2:
            result_y = y_value[k]

    result = [result_x, result_y]

    return result

input_list = [1, 4], [3, 4], [3, 10]
make_rectangle(input_list)  
