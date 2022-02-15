# round.py
# This program is created to round a float number
# rounds a number
# be careful of round, it rounds to the nearest even number
# eg 4.5 rounds to 4
# but 5.5 rounds to 6
# so do not use it accuracy is essential

# By_Philip_Akinbami

numbertoround = float(input( 'type a float number '))
roundnumber = int(round(numbertoround))
print('{} is rounded to {}' .format(numbertoround, roundnumber))
