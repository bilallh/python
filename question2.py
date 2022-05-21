count_odd = 0
count_even = 0
odd_sum = 0
even_sum = 0

lower = int(input("Enter the lower limit for the range:"))
upper = int(input("Enter the upper limit for the range:"))

print("All the odd numbers")
for i in range(lower, upper + 1):
	if (i % 2 != 0):
		count_odd += 1
		odd_sum += i
		print(i)
print("All the even numbers")
for i in range(lower, upper + 1):
	if (i % 2 == 0):
		count_even += 1
		even_sum += i
		print(i)

print(f"count of odd number is {count_odd}")
print(f"count of even number is {count_even}")

print(f"Sum of odd number is {odd_sum}")
print(f"Sum of Even number is {even_sum}")

odd_avg = odd_sum / count_odd

even_avg = even_sum / count_even

print(f"Avg of odd numbers is {odd_avg}")
print(f"Avg of Even number is {even_avg}")