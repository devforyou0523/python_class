#조건식을 활용한 리스트
list_a = ["사과", "자두", "초콜릿", "바나나", "체리"]

output = [fruit for fruit in list_a if fruit != "초콜릿"]

print(output)