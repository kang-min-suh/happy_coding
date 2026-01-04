# 행성의 한글 이름을 입력하면 영어 이름을 반환하는 프로그램 만들기 
planet_dict = {
    "수성":"Mecury", "금성":"Venus",  "지구":"Earth",  "화성":"Mars", 
     "목성":"Jupiter",  "토성":"Saturn", "천왕성":"Uranus", "해왕성":"Neptune"
}
planet_name = input("행성의 이름을 입력하세요: ")
print(planet_dict[planet_name])
