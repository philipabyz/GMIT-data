# Abosulte.py
# This program is created to convert a floating non absolute number to absolute
# By_Philip_Akinbami

# In the question, number is ambiguous but the
# output implies that we should be dealing with floats
# So I am casting the input to a float

notabsolute = float(input('type a non absolute number '))
absolutenumber = abs(notabsolute)
print('The absolute number of {} is {}' .format(notabsolute,absolutenumber))
