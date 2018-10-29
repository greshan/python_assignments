#29. In a given list find the total number of odd numbers, even numbers and their respetive sum and average.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
count_odd = 0
count_even = 0
sume = 0
sum1 = 0
for x in numbers:
    if not x % 2:
        count_even+=1
        sume += x
    else:
        count_odd+=1
        sum1 += x

aveo = sum1/count_odd
avee = sume/count_even
print("Number of even numbers, sum and average :",count_even, sume, avee)
print("Number of odd numbers, sum and average :",count_odd, sum1, aveo)
