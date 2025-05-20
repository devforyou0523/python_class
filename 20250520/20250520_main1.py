#외부 라이브러리 import (datatime)
import datetime
now = datetime.datetime.now()
output_a = f"{now.year}년 {now.month}월 {now.day}일 {now.hour}시 {now.minute}분 {now.second}초"
output_b = now.strftime("%Y년 %m월 %d일 %H시 %M분 %S초")
output_c = now.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}".format(*"년월일시분초"))

print(output_a)
print(output_b)
print(output_c)