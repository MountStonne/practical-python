# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
#payment = 2684.11
total_paid = 0.0
count = 0
while principal > 0:
    count += 1
    if count <= 12:
        payment = 3684.11
    else: 
        payment = 2684.11
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
    

print('Total paid', total_paid)
print(count)