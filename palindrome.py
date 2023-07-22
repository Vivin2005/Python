str=input("ENTER THE STRING TO CHECK PALINDROME OR NOT:")
str=str.casefold()

if(str==str[::-1]):
	print("IT IS PALINDROME")
else:
	print("IT IS NOT A PALINDROME")