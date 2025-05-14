
#In this program I am going to make a calculator.
'''First I will take 2 numbers from the user than compute it
   to provide them the answer'''
#If you are applying (if) statement with a string ,remember to put ('')inverted commas.
#STARTED!!!

print('''Heloo user!!!
I am here to provide you a well made calculator.
You can use it to ease your calculation.''')
n1=float(input('Enter the first number.:-'))
n2=float(input('Enter the second number.:-'))
o=input('Enter the Operator you want-(+)(-)(x)(%).:-')
if o == '+':
    print( n1 ,'+', n2 ,'=', n1+n2)
elif o == '-':
    print( n1 ,'-', n2 ,'=', n1-n2)
elif o == 'x':
    print( n1 ,'x', n2 ,'=', n1*n2)
else:
    o == '%'
    print( n1 ,'%', n2 ,'=', n1/n2)
k=input('Press key to close')    


    
    
