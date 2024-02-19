#function to find the length of distinct characters in a string
def appeal(string):
    #set to store the distinct characters
    distinctcharacters = set()
    #loop to add the distinct characters to the set
    for i in string:
        distinctcharacters.add(i)
    #return the length of the set
    return len(distinctcharacters)

print(appeal("hello"))