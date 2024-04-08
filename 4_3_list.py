
#리스트 만들기
#리스트는 통계에서 정말 많이 사용한다고 함
#[]안에 작성하면 됨 
student = ["egoing","sori","maru"] # student의 이름을 가진 리스트 생성

grades = [2,1,3]

#만약 student의 sori를 출력하고 싶다면?
print('student[1]',student[1])

#student가 몇 개의 원소로 이루어져있는지?
print("len(student)",len(student))


#리스트의 값 중 가장 크거나 작은 값을 알고 싶을 때
# 최소값은 min(), 최대값은 max()
print("min(grades)",min(grades))
print("max(grades)",max(grades))


#통계를 내보자
#statics를 import하기 
#mean은 평균을 뽑을 수 있음
import statistics
print("statistics.mean(grades)",statistics.mean(grades))


#많은 값 중에서 하나만 뽑아보자 (random에서 choice)
import random
print("random.choice(student)",random.choice(student))