def interleaving(str1,str2,str3):
    if len(str1)+len(str2) != len(str3):
        return False
    if len(str1) == 0:
        return str2 == str3
    if len(str2) == 0:
        return str1 == str3
    if str1[0] == str3[0] and interleaving(str1[1:],str2,str3[1:]):
        return True
    if str2[0] == str3[0] and interleaving(str1,str2[1:],str3[1:]):
        return True
    return False

str1 = "aabcc"
