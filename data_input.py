#!/usr/bin/env python3

if __name__=="__main__":
	while True:
		print("Enter your present age:", end=" ")
		age = input()
		try:
			age = int(age)
		except ValueError:
			print("Please use numeric digits.")
			continue
		if age<1:
			print("Please enter a positive number.")
			continue 
		break
	print(f"Your age is "_" ")
