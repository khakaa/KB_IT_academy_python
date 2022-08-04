
def start_game():
    import random

    fields = list()
    for i in range(10):
        fields.append([0]*10)

    nums = list(range(100))

    for i in random.sample(nums, 10):
        row = i // 10 # 행 위치
        col = i % 10 # 열 위치
        fields[row][col] = 9 # 지뢰 위치

        # 지뢰의 대각선, 상하좌우 + 1씩 해줌     
        if row < len(fields) - 1:
            fields[row+1][col] += 1 # 남

        if row < (len(fields) - 1) and col < (len(fields) - 1):
            fields[row+1][col+1] += 1 # 남동

        if col < (len(fields) - 1):
            fields[row][col+1] += 1 # 동

        if row > 0 and col < (len(fields) - 1):
            fields[row-1][col+1] += 1 #북동 

        if row > 0:
            fields[row-1][col] += 1 #북

        if row > 0 and col > 0:
            fields[row-1][col-1] += 1 #북서

        if col > 0:
            fields[row][col-1] += 1 #서

        if row < (len(fields) - 1) and col > 0:
            fields[row+1][col-1] += 1 # 남서

    fields

    open = list()
    for i in range(10):
        open.append(["-"] * 10)

    cnt = 0
    for f in fields:
        for v in f:
            if v >= 9:
                cnt += 1

    while cnt > 0:
        m,n = map(int, (input("0에서 9까지의 숫자 입력 : ").split()))
        open[m][n] = str(fields[m][n])

    #     for i in open:
    #         print(i)

        if fields[m][n] >= 9:
            cnt -= 1

            if m < len(fields) - 1:
                open[m+1][n] = str(fields[m+1][n]) # 남

            if m < (len(fields) - 1) and n < (len(fields) - 1):
                open[m+1][n+1] = str(fields[m+1][n+1]) # 남동

            if n < (len(fields) - 1):
                open[m][n+1] = str(fields[m][n+1]) # 동

            if m > 0 and n < (len(fields) - 1):
                open[m-1][n+1] = str(fields[m-1][n+1]) #북동 

            if m > 0:
                open[m-1][n] = str(fields[m-1][n]) #북

            if m > 0 and n > 0:
                open[m-1][n-1] = str(fields[m-1][n-1]) #북서

            if n > 0:
                open[m][n-1] = str(fields[m][n-1]) #서

            if m < (len(fields) - 1) and n > 0:
                open[m+1][n-1] = str(fields[m+1][n-1]) # 남서

            print(f"지뢰!, 남은 지뢰 갯수 : {cnt}")
        if fields[m][n] < 9:
            print("성공")

        display(open)