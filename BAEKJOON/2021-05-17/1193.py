n = int(input())

crossNum = 0
counter = 0
# 같은 대각선에 있는 값들은 분모 + 분자 값이 동일하다
# 대각선의 순서는 (분모 + 분자) - 1
# 대각선의 분모 + 분자가 짝수이면 우측으로 진행
# 대각선의 분모 + 분자가 홀수이면 좌측으로 진행

# 몇번째 대각선인지 알아야 됨..
#1, 3, 6, 10, 15
for i in range(n):
    curNum = i+1
    if curNum > counter:
        crossNum += 1
        counter = (crossNum+1)
        print("counter==", counter)

print("crossNum", crossNum)
