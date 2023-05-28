name = input("What’s Your name? ")
year_of_birth = int(input('Year of birth: '));
#Input the mark in range 1 to 10
mark = float(input('Your mark: '));
while mark<0 or mark >10:
    mark = float(input('The mark must be in range 1 to 10. Please enter the other one:  '));
#Print a notification
if mark >=5:
    print('Mr/Miss ', name,' have passed! Congratulation!');
else:
    print('Mr/Miss ', name, ' have not passed ! Come on!');