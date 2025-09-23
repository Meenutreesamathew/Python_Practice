text = input("Enter your text")

rev = text[::-1]

if text == rev:
    print("palindrome")
else:
    print("Not Palindrome")