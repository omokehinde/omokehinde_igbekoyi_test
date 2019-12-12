# Question B

def checkVersion(v1,v2):
    try:
        if float(v1) < float(v2):
            return v1 + ' is less than ' + v2
        if float(v1) > float(v2):
            return v1 + ' is greater than ' + v2
        if float(v2) == float(v2):
            return v1 + ' and ' + v2 + ' are equal.'
    except:
        return 'Please call the method like this: checkVersion("float","float")'

# print(checkVersion('1.2','2.3'))
# print(checkVersion('3.3','2.3'))
# print(checkVersion('foo','2.3'))