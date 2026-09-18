# \d for digits, \w for word characters, \s for whitespace characters, and their uppercase counterparts for negation.
# example 
# (555)-555-5555 the regular expression will be 
# r"(\d{3})\-\d{3}-\d{4}" or 
# r"(\d\d\d)-\d\d\d-\d\d\d\d"

# Note: if there are multiple matches, re.search() will return the first match only.
# To find all matches, use re.findall().

text = "The agent's number is 408-555-1234. & another number is Call soon!"

import re

pattern = "number"
match = re.search(pattern , text)
print(match)
print(match.span())
print(match.start())
print(match.end())

matches = re.findall(pattern, text)
print(matches)

#finditer() returns an iterator yielding match objects for all non-overlapping matches of the pattern in the string.
for each_match in re.finditer(pattern, text):
    print(each_match)