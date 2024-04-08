#문장에서 내가 원하는 것들만 따로 변경 가능함 
#name값과 massage를 바꿔주면 출력되는 값도 변경됨

#input('name : ') 하면 마치 Scanner sc와 같은 효과를 봄
# 이 파일을 실행시킬 때 이름을 먼저 물어보고 작성한 이름을 바탕으로 massage를 생성해냄

name=input('name:')
massage='hi, '+name+' ...... bye,'+ name

#다 같은 값이 출력됨
print('hi, sori ..... bye, sory')
print('hi, '+name+' ...... bye,'+ name)
print('massage : ',massage)