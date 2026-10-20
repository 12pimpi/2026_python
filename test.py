import random

def 심판(나, 컴퓨터):
    if 컴퓨터 == 나 :
        return "무승부"
    elif (나 == "가위" and 컴퓨터 == "보") or (나 == "바위" and 컴퓨터 == "가위") or (나 == "보" and 컴퓨터 == "바위"):
        return "승리" 
    else:
        return "패배"

print("유저는 가위, 바위, 보를 5번 선택해주십시오.")
나 = []
컴퓨터 = []
승리_횟수 = 0

for i in range(5):
    선택 = input(f"{i+1}번째 선택: ")
    나.append(선택)
    컴퓨터.append(random.choice(["가위", "바위", "보"]))
    결과 = 심판(나[i], 컴퓨터[i])
    print(f"{i+1}판: {나[i]} vs {컴퓨터[i]} => 결과: {결과}")
    if 결과 == "승리" : 
        승리_횟수 += 1

print(f"총{승리_횟수}승!!")