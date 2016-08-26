def readNextItem(string, delimiter=' ', transform=None):
    """
    This is a generator function that reads next item from the string
    """
    stringBuffer = ''
    for char in string:
        if (char == delimiter):
            # if no transform function is specified, return our collected string in buffer,
            # else return result of transform function. Then reset the stringBuffer
            yield stringBuffer if transform is None else transform(stringBuffer)
            stringBuffer = ''
        else:
            stringBuffer += char
    
    # when for loop ends above, stringBuffer has unyielded result.
    yield stringBuffer if transform is None else transform(stringBuffer)

#############################
# Example usage #1:
############################
testString = '1,2,3,4'
stringGenerator = readNextItem(testString, ',', int)    # get a generator that splits on ',' and transforms items to int
nextItem = next(stringGenerator, None)                  # get first item from the generator, returns 'None' if generator stops

while (nextItem is not None):                           # loop till generator has stopped
    print(nextItem)
    nextItem = next(stringGenerator, None)              # read next item from generator

#############################
# Example usage #2:
############################
for x in readNextItem('a b c d'):
    print(x)

#############################
# Example usage #3:
############################
for x in readNextItem('1 2 3 4', transform=int):            # default delimited value. only passing transform function
    print('{}'.format(x+3))

#############################
# Example usage #4:
############################
testString = 'a b c d'
stringGenerator = readNextItem(testString, ' ', lambda x: x.upper())              # get a generator that splits on default ' ', then transforms result to uppercase
nextItem = next(stringGenerator, None)                  # get first item from the generator, returns 'None' if generator stops

while (nextItem is not None):                           # loop till generator has stopped
    print(nextItem)
    nextItem = next(stringGenerator, None)              # read next item from generator