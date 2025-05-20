#datetime 시간 추가
import datetime

now = datetime.datetime.now()
after = now + datetime.timedelta(weeks= 1, days= 1, hours= 1, minutes= 1, seconds= 1)
year_after = now.replace(year= now.year+1)

print(now.strftime("현재: %Y{} %m{} %d{} %H{} %M{} %S{}".format(*"년월일시분초")))
print(after.strftime("미래: %Y{} %m{} %d{} %H{} %M{} %S{}".format(*"년월일시분초")))
print(year_after.strftime("1년 후: %Y{} %m{} %d{} %H{} %M{} %S{}".format(*"년월일시분초")))