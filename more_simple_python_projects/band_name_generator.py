import random

#1. Create a greeting for your program.
print("Welcome to the fortnite name system.")
#2. Ask the user for the city that they grew up in.
one=input("What are three things you like?\n1. ")
two=input("2. ")
three=input("3. ")

l=len(two)
m=l//2

n = random.choice(one) + random.choice(one)

#3. Ask the user for the name of a pet.
fn=input("Whats your favorite number\n")
#4. Combine the name of their city and pet and show them their band name.
print("Your name is " + one[0:2] + two[m-1:m+1] + three[-2::1] + fn)
print(f"Or... {random.choice(one) + random.choice(one)+random.choice(two)+random.choice(two) + random.choice(three) + random.choice(three)+ fn}")
#5. Make sure the input cursor shows on a new line, see the example at:
#   https://replit.com/@appbrewery/band-name-generator-end