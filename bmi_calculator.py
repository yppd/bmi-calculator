# 1st input: enter height in meters e.g: 1.65
height = input()
# 2nd input: enter weight in kilograms e.g: 72
weight = input()


nominator = int(weight)
denominator = (float(height) **2)

BMI = int(nominator / denominator)
print(BMI)