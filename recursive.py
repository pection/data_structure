def recur_factorial(n):
	if n ==0:
		return 1
	if n == 1:
		return n
	else: 
		return n*recur_factorial(n-1)

num = int(input("Enter a number "))

if num < 0 :
	print("Sorry ,factorial dfoes not exist for negative numbers")
elif num ==0 :
	print("The factorial of 0 is 1")
else:
	print(f"The facetorial of {num} is {recur_factorial(num)}")

