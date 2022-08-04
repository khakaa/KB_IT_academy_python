def start_game():
    import random
    com = random.randint(1,100)
    cnt = 0

    for i in range(10):
        print(f"랜덤숫자 : {com}")
        user = int(input())
        print(f"시도 횟수 : {i+1}")

        if com < user:
            print("낮춰주세요")
        elif com > user:
            print("높여주세요")

        if (i == 9 and com != user):
            print("당신은 바보~")
        elif com == user:
            print("정답입니다")
            break

        print("\n")