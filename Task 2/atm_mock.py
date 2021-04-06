from datetime import datetime

print('Welcome to Zuri ATM')
name = input('Please enter your name?\n')
allowedUsers = ['Seyi', 'Mike','Love']
allowedPassword = ['passwordSeyi','passwordMike', 'passwordLove']
currentBalance = 1000000.00



if name in allowedUsers:
    
    password = input('Enter your password?\n')
    userId = allowedUsers.index(name)
    if password == allowedPassword[userId]:
        timeDate = datetime.now()
        print('Welcome %s to Zuri Atm.' %name )
        print(f'Time of Login: {timeDate.strftime("%X")}\
            Date of Login: {timeDate.strftime("%x")}')

        print('***************Options*****************\nPlease choose an option.')

        print('1, Withdrawal')
        print('2, Cash Deposits')
        print('3, Complaint')

        selectedOption = int(input("Please selection an option:\n"))

        if (selectedOption == 1):
            print('You selected %s' %selectedOption)
            withDrawal = float(input('How much would you like to withdraw (Naira)?\n'))
            if (currentBalance < withDrawal):
                print(f'Insufficent Funds for this transaction.\
                    \nYour current balance is #{currentBalance}. Please make a deposit?\n')
            elif(currentBalance >= withDrawal and currentBalance > 0.00):
                print('Take your cash\nYou have been logged out')


        elif (selectedOption == 2):
            print('You selected %s' %selectedOption)
            deposit = int(input('how much would you like to deposit?\n'))
            currentBalance =+ deposit
            print(f'You have sucessful deposited #%s.\nYour new account balance is #{currentBalance}.'%deposit)
        
        elif( selectedOption == 3):
            print('You selected %s' %selectedOption)
            complaint = input('What issue will you like to report.')
            print('Thank you for contacting us.')
        else:
            print('Invalid Option selected. Please try again.')

    else:
        print('Password Incorrect, please try again')

else: 
    print('Name not found. Please try again.')