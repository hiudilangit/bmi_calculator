#name = "Hiu"
#weight_kg = 85
#height_m = 1.8

#bmi = weight_kg / (height_m ** 2)

#if bmi < 25:
#    print("is healthy")
#else:
#    print("is overweight")

#print(bmi)


#BMICalc version 0.2 with new codebase

name = input('what is your name?')
print(name)

weight = input('how much do you weigh in kg?')
print(weight, 'kg')

height = input('how tall are you in m?')
print(height, 'm')

bmi = weight / (height ** 2)

if bmi < 25:
    print(name, 'you are considered healthy')
else:
    print(name, 'you are overweight. consider working out.')

print(bmi)
