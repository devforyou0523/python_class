dict_a = {"name":"7D 건조 망고", "type":"당절임","ingredent":["망고","설탕","메타중아황산나트륨","치자황색소"],"origin":"필리핀"}

key = input("접근할 키 >")

if key in dict_a:
    print(dict_a[key])
else:
    print("존재하지 않는 키에 접근하고 있습니다.")