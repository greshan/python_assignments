#Implement a  program  for finding a square of a number. (without using standard api)


def square(n):

    if (n < 0):
      n = -n

    res = n


    for i in range(1, n):
        res += n

    return res

n = int(input("Enter The number: "))

print("n =", n , end=", ")
print("n^2 =", square(n))
