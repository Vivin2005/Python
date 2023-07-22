import math

def add(x,y):
	return x+y
def sub(x,y):
	return x-y
def mul(x,y):
	return x*y
def div(x,y):
	return x/y
def exp(x,y):
	return x**y
def floorDiv(x,y):
	return x//y
def modu(x,y):
	return x%y
	
print("SELECT THE OPERATION:")
print("1.ADDITION")
print("2.SUBRACTION")
print("3.MULTIPLE")
print("4.DIVISION")
print("5.EXPONENTIAL")
print("6.FLOOR DIVISION")
print("7.MODULE")

while True:
	option=input("CHOOSE OPTION(1,2,3,4,5,6,7) :")
	if option in ('1','2','3','4','5','6','7'):
		num1=float(input("ENTER FIRST NUMBER:"))
		num2=float(input("ENTER SECOND NUMBER:"))
		if option==1:
			print(num1, '+' ,num2, "=",add(num1,num2))
		elif option==2:
			print(num1, '-' ,num2, "=" ,sub(num1,num2))
		elif option==3:
			print(num1, '*' ,num2, "=",mul(num1,num2))
		elif option==4:
			print(num1, '/' ,num2, "=",div(num1,num2))
		elif option==5:
			print(num1, '**' ,num2, "=",exp(num1,num2))
		elif option==6:
			print(num1, '//' ,num2, "=",floorDiv(num1,num2))
		elif option==7:
			print(num1, '%' ,num2, "=",modu(num1,num2))
		break
		
	else:
				print("INVALID OPERATOR")
		