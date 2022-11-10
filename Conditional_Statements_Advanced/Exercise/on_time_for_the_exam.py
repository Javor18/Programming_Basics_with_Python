exam_hour = int(input())
exam_minute = int(input())
arrive_hour = int(input())
arrive_minute = int(input())

arrive_time = (arrive_hour * 60) + arrive_minute
exam_time = (exam_hour * 60) + exam_minute

diff_min = abs(exam_time - arrive_time)

if exam_time < arrive_time:
    print (f'Late')
    if diff_min >=60:
        hour = diff_min // 60
        minute = diff_min % 60
        if minute < 10:
            print(f'{hour}:0{minute} hours after the start')
        else:
            print(f'{hour}:{minute} hours after the start')
    else:
        print(f'{diff_min} minutes after the start')
elif arrive_time == exam_time or diff_min <= 30:
    print(f'On time')
    if diff_min >=1 or diff_min <= 30:
        print(f'{diff_min} minutes before the start')
else:
    print(f'Early')
    if diff_min >= 60:
        hour = diff_min // 60
        minute = diff_min % 60
        if minute < 10:
            print(f'{hour}:0{minute} hours before the start')
        else:
            print(f'{hour}:{minute} hours before the start')
    else:
        print(f'{diff_min} minutes before the start')