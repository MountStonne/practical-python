# bounce.py
#
# Exercise 1.5

height = 100
count = 1
while height > 1:
    height = height * (3/5)
    print(count, round(height, 4))
    count += 1