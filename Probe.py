height = float(input('Heigh: '))
weight = float(input('Weigh: '))

bmi = round(weight / height ** 2, 2)
print(bmi)
if bmi < 18.5:
    print('Not enough')
elif bmi < 25:
    print('Good')
elif bmi < 30:
    print('Much')
else:
    print('Too much')