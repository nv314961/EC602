# this script will remove trailing zeros from a string containing numbers with
# trailing zeros after a decimal point. 
# caveat: these numbers must be on their own line,
# or you must modify the str.split() command.

def removeTrailingZeros(out):
    outLines = out.split('\n')
    del outLines[-1] # empty \n element was appearing at the end of outLines
    newOut = ""
    for i in outLines:
        try:
            i = '{:g}'.format(float(i)) # the magic: remove trailing zeros
            newOut += (i + '\n') # construct new string, include \n
        except ValueError: # when we don't get a string with just a number (time), just pass it as is to the new string
            newOut += (i + '\n')
            continue
    return newOut
	
def main():
	str = "1.000\none 1 1 1 1\n3.000\none 3 3 1 1\n"
	print(str)
	str = removeTrailingZeros(str)
	print(str)
if __name__ == '__main__':
    main()