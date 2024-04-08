#나 혹은 다른 개발자가 만든 코드를 내가 사용할 수 있는 방법 
# pandas를 사용하고 싶다면 pip.org에서 사용가능 
# 여기에다가 설치할 때는 python3 -m pip install pandas 이렇게 작성하면 됨 
# python3 -m pip install pandas
import pandas
house = pandas.read_csv('house.csv')
print(house)

# 만약 초반에 있는 몇 줄만 출력하고 싶을땐?
print(house.head()) #앞 5줄만 출력
print(house.head(2)) #앞 2줄만 출력


print(house.describe()) # 지금 내용에 대한 요약을 해줌 // 엄청난 기능이라고 함






