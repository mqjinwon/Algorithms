# It takes 32 minutes 37 seconds
# I solve this problem by wrong direction
# 정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램을 작성하세요. 예를 들어 1을 입력했을 때 다음은 3이 하나라도 포함되어 있으므로 세어야 하는 시각입니다.
# 5

max_hour = int(input())
max_min = 59
max_sec = 59

target_num = 3

count = 0
for hour in range(max_hour+1):
    for minute in range(max_min+1):
        for second in range(max_sec+1):
            if str(target_num) in (str(hour) + str(minute) + str(second)):
                count += 1    

print(count)