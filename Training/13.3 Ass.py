#Exception Handling
while(True):
    try:
        userInput= input("Enter only number (Enter anything else for Exception Handling): ")
        number= int(userInput)
        print('Number Entered:',number)
    except Exception as ex:
        print('Error:', ex.__class__.__name__)

    print('\n')
