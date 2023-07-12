#PYTHON inputs text as string so always rememebr 
#to typecast into int if dealing with numbers
mark=int(input('What is your score')) 
if mark>80:
    print('Outstanding')
elif mark>40:
    print('great')
else:
    print('GOOD')