from audioop import reverse

text = "Meenu"

print("Reversed: ", text[::-1])

reversed_text =""
for i in text:
    reversed_text = i+reversed_text
print(reversed_text)

temp_list =list(text)
temp_list.reverse()
print(temp_list)