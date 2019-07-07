import string

def RCtoAbs(row,column):
		strPosition = ''
		iStr = int((column - 1) / 26)
		jStr = int(column - (iStr * 26))
		for z in iStr,jStr:
			if z != 0:
				strPosition = strPosition + chr(z + 64)
		strPosition = strPosition + str(row)
		
		return strPosition
