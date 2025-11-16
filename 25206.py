grade_dic = {
  'A+': 4.5,
  'A0': 4.0,
  'B+': 3.5,
  'B0': 3.0,
  'C+': 2.5,
  'C0': 2.0,
  'D+': 1.5,
  'D0': 1.0,
  'F': 0.0
}

total_grade = 0
total_credit = 0
for i in range(20):
sbj_name, credit, grade = input().split()
if grade == 'P':
  continue

credit = float(credit)
grade_f = grade_dic[grade]

total_grade += credit * grade_f
total_credit += credit

print(round(total_grade / total_credit, 6))
