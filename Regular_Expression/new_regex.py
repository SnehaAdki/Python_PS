import re

print(re.search(r'cat','This is the cat in the hat.'))

print(re.search(r'cat|dog','This is the cat in the hat. The dog also needs mat'))

print(re.findall(r'cat|dog','This is the cat in the hat. The dog also needs mat'))

all_match = re.finditer(r'cat|dog','This is the cat in the hat. The dog also needs mat')
for each_match  in all_match:
    print(each_match)
    print(each_match.span(),each_match.group()) 


all_matches_at = re.findall(r'at','This is the cat in the hat. The dog also needs mat')
print(all_matches_at) #['at', 'at', 'at']


all_matches_xat = re.findall(r'.at','This is the cat in the hat. The dog also needs mat')
print(all_matches_xat) #[' cat', ' hat', ' mat']


all_matches_xat = re.findall(r'...at','This is the cat in the hat. The dog also needs mat splat')
print(all_matches_xat) #['e cat', 'e hat', 's mat', 'splat']


#start_with
starts_with = re.findall(r'^This','This is the cat in the hat. The dog also needs mat') #['This']
print(starts_with) #['This']

starts_with = re.findall(r'^1','1 is the number') #['1']
print(starts_with) #['1']

starts_with = re.findall(r'^\d','1 is the number') #['1']
print(starts_with) #['1']

starts_with = re.findall(r'^\d','The 1 is the number') #[]
print(starts_with) #[]


#ends with
ends_with = re.findall(r'mat$','This is the cat in the hat. The dog also needs mat') #['mat']
print(ends_with)

ends_with = re.findall(r'\d$','This is the cat in the hat. The dog also needs mat') #[]
print(ends_with)

ends_with = re.findall(r'\d$','This is the cat in the hat. The dog also needs mat 122' ) #['2']
print(ends_with)

ends_with = re.findall(r'.*\d$','This is the cat in the hat. The dog also needs mat 122' ) #['This is the cat in the hat. The dog also needs mat 122']
print(ends_with)



#exclude all find all characters except digits
phrase = 'there are 3 numbers 34 inside 5 this sentence'
pattern = r'[^\d]'
returned_list = re.findall(pattern,phrase)
print(returned_list) #['t', 'h', 'e', 'r', 'e', ' ', 'a', 'r', 'e', ' ', ' ', 'n', 'u', 'm', 'b', 'e', 'r', 's', ' ', ' ', 'i', 'n', 's', 'i', 'd', 'e', ' ', ' ', 't', 'h', 'i', 's', ' ', 's', 'e', 'n', 't', 'e', 'n', 'c', '


phrase = 'there are 3 numbers 34 inside 5 this sentence'
pattern = r'[^\d]+' 
returned_list = re.findall(pattern,phrase)
print(returned_list) #['there are ', ' numbers ', ' inside ', ' this sentence']

test_phrase = 'This is a string! But it has punctuation. How can we remove it?'
print(re.findall(r'[^!.? ]+',test_phrase)) #['This', 'is', 'a', 'string', 'But', 'it', 'has', 'punctuation', 'How', 'can', 'we', 'remove', 'it']




