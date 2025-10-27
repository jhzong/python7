# 990101-1111111
# 070101-2111111
# 070101-4111111

import datetime
now = datetime.datetime.now()

# 주민번호를 입력받아, 남/여인지 출력

jumin=input("주민번호를 입력하시오.")
sex=int(jumin[7])
if sex%2==0:
    print("여자입니다.")
else:
    print("남자입니다.")
    
# 생월을 따서 이벤트 대상자 판별
b_month=int(jumin[2:4])
c_month=now.month
if b_month==c_month:
    print("이벤트 대상자입니다.")
else:
    print("이벤트 대상자가 아닙니다.")