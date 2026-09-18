import re 

text = "The rain in Spain. My phone number is 123-456-7890. Call me!"

# without quantifiers
phone_w_q = re.search(r"\d\d\d-\d\d\d-\d\d\d\d", text)
print(phone_w_q.group())  # Output: 123-456-7890
print(phone_w_q)  # Output: <re.Match object; span=(27, 39), match='123-456-7890'>

#with quantifiers
phone = re.search(r'\d{3}-\d{3}-\d{4}', text)
if phone:
    print("Phone number found:", phone.group()) 
    print(phone)
else:
    print("No phone number found.")


print("--------------------------")
print("First 3 digits of the phone number:")

first_3_digit = phone.group()[:3]
print(first_3_digit)  # Output: 123

phone = re.search(r'\d{3}', text)
print("--------------------------")
print("First 3 digits of the phone number using regex:",phone.group())  # Output: 123



#another way to get the first 3 digits of the phone number using regex
phone_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
print(phone_pattern)


phone_match = re.search(phone_pattern, text)
if phone_match:
    print("First 3 digits of the phone number using regex:", phone_match.group())  # Output: 123-456-7890
    print("First 3 digits of the phone number using regex:", phone_match.group(1))  # Output: 123
