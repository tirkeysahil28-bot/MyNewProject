#Identify the user name of vovels in user name
username = input("Enter your name: ")

vowels = "aeiouAEIOU"
count = 0

for char in username:
    if char in vowels:
        count += 1

print("Number of vowels =", count)
