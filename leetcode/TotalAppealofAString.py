#function to find the length of distinct characters in a string
def appeal(string):
    #set to store the distinct characters
    distinctcharacters = set()
    #loop to add the distinct characters to the set
    for i in string:
        distinctcharacters.add(i)
    #return the length of the set
    return len(distinctcharacters)

string = "code"
countsingle  = len(string)
print(appeal("abbca"))



#function to find substring of a string with x length
def substring(string, x):
    #list to store the substring
    substring = []
    #loop to find the substring
    for i in range(len(string)-x+1):
        substring.append(string[i:i+x])
    #return the list
    return substring

print(substring("abbca", 2))


for i in range(1, len(string)):
    for j in substring(string, i+1):
        countsingle += appeal(j)



        



print(countsingle)