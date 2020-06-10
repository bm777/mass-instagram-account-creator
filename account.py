import string 
import random

def genName():
	fisrtname = ["Totaleta", "Alphonse", "louisse", "paulle", "lior", "Citrouille"]
	lastname  = ["Demir", "Saphir", "Ozbal", "Ayduin", "Camtel", "Orange"]

	return "".join(random.choice(fisrtname) + " " +random.choice(lastname)) 

def username(size=7, chars=string.ascii_lowercase+random.choice(['.', '_'])):

	return ''.join(random.choice(chars) for _ in range(size))

def genMail():

	return ''.join(username() + "@gmail.com")

if __name__ == '__main__':
	print(genMail())