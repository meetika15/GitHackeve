#Welcome to HackEve v20

#takes a string s as argument and converts it from binary to decimal form
def bin_to_dec(s):
	

	return int(s,2) #Number n in decimal form will be returned


#takes a number n as argument and converts it from decimal to hexadecimal form
def dec_to_hex(n):
	
	
	return hex(str1) #String str1 will be returned in hexadecimal form

#takes a string s as argument in hexadecimal form and returns its 1's compliment
def hex_compliment(s):
	
	
	return hex(hex(str1) ^ 0xFF) #String str1 will be returned as 1's compliment



s = input("Enter the binary string: ")

digits = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
a = bin_to_dec(s)
b = dec_to_hex(a)
c = hex_compliment(b)


print("Final output is",c)