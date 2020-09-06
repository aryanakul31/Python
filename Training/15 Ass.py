def addition(a, b):
    print('Addition of ',a,'and',b,'is', (a+b))

def subtraction(a, b):
    print('Subtraction of ',a,'and',b,'is', (a-b))

def multiplication(a, b):
    print('Multiplication of ',a,'and',b,'is', (a*b))

def division(a, b):
    try:
        print('Division of ',a,'and',b,'is', (a/b))
    except Exception as ex:
        print('Division Error:',ex.__class__.__name__)


choice= 'n'
while(choice is 'n'):
    print("Enter 'y' to exit")
    print('1 for Addition')
    print('2 for Subtraction')
    print('3 for Multiplication')
    print('4 for Division')
    user_input= input('Enter your choice: ')
    if user_input is 'y':
        choice='y'
    else:
        try:
            number=int(user_input)
            number_1= int(input('Enter the first number: '))
            number_2= int(input('Enter the second number: '))
            if number==1:
                addition(number_1, number_2)
            elif number==2:
                subtraction(number_1, number_2)
            elif number==3:
                multiplication(number_1, number_2)
            elif number==4:
                division(number_1, number_2)
            else:
                print('Please enter a correct value')
        except Exception as ex:
            print('Error:',ex.__class__.__name__)
        finally:
            print('\n\n')
