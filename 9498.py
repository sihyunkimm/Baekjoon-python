점수 = int(input())

if 점수 >= 90 :
    학점 = "A"

elif 점수 >= 80 and 점수 < 90:
    학점 = "B"

elif 점수 >= 70 and 점수 < 80:
    학점 = "C"

elif 점수 >= 60 and 점수 < 70:
    학점 = "D"

else:
    학점 = "F"

print(학점)