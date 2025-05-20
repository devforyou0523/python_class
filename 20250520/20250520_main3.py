#urllib 라이브러리를 이용한 url 접속
from urllib import request

target = request.urlopen("http://google.com")
output = target.read()

print(output)