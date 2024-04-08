print('hello world') #작은 따옴표도 출력가능
print("hello world") #큰 따옴표도 출력가능 (결과 값은 둘 다 똑같음)

#줄바꾸기
# (''' ~ ''') '''(혹은 """)를 작성하면 줄바꿈도 가능 
print(''' 
hello
world
''') # 결과값이 hello와 world가 줄바꿈되어서 출력됨


# 문자와 관련된 계산

# 문자끼리 덧셈
print("'1'+'1'", '1'+'1') # 2가 아닌 11이 출력됨 (문자로 인식되어서 문자로 그대로 출력됨)

#문자를 반복적으로 출력
print("hello world"*1000) # 1000번 출력됨!

#문자의 개수 알아보기(len())
print("len('hello world'*1000)",len('hello world'*1000))  # len()은 글자 수가 몇 개인지 알 수 있음 

#문자를 다른 문자로 치환해보기(replace())
# 바꿀문장.replace('바꾸길 원하는 문자열','새롭게 바꿀 문자')
print("'hello world'.replace('world','universe')",'hello world'.replace('world','universe'))
