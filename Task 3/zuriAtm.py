# Database
import database




# databaseOfAccounts = {}

def init():
    '''
    Initializing the system
    '''

    print('welcome to Zuri Bank')
    haveAccount = int(input('Do you have an account with us: 1 (Yes) or 2 (No) \n'))
    if (haveAccount == 1):
        login()
    elif (haveAccount == 2):
        register()
    else:
        print('You have selected an Invalid option.\n')
        init()





# login
# account number and password


def login():
    """ 
    Logging into the bank application to perform transactions.
    """
 
    print('************Login into your account*******************')
    try:
        loginOrForgottenPass= int(input('To login enter 1.\nForgotten password or Account Number enter 2.\n'))
    except ValueError:
        print('Input was not a number')
        login() 
    if ( loginOrForgottenPass == 1):
        try:
            userAccountNo = int(input('Please enter your Account Number?\n'))
        except ValueError:
            print('The input were not number.')
            login()
        userPassword = input('Please enter your password?\n')

        for accountNum,userDetail in databaseOfAccounts.items():
            if (userAccountNo == accountNum):
                if (userPassword == userDetail[3]):
                    
                    print('Login Successful.')
        else:             
            print('Invalid Account or Password')
            bankOperations(userDetail)            
    elif (loginOrForgottenPass == 2):
        forgottenInfo()
        





# register
# username, email, and password
# generate user ID

def register():
    """
    Registering a New Bank customer.
    """
    print('****************Registration from for Zuri Bank****************')
    email = input('what is your email address? \n')
    firstName = input('what is your first name? \n')
    lastName = input('What is your last name? \n')
    password = input('create your password?\n')
    

    accountNo = genAccountNo()

    is_user_created = database.create(accountNo,[firstName, lastName,email, password])
    if is_user_created:
        print('Your account has been created.\nHere is your account Number %d please keep it safe.' % accountNo)
        login()
    else:
        print('Something went wrong.')
        register()

def genAccountNo():
    """
    Generate Account Number Using Random package.

    """
    from random import randint

    accountNumber = randint(0000000000, 9999999999)
    return accountNumber





# bank operations


def bankOperations(user):
    print('Welcome %s, %s to Zuri Bank.\n****** Bank of the free ******' %(user[0], user[1]))
    try:
        SelectedOption = int(input('What would you like to do?\nPlease Select an option.\n(1) deposit.\n(2) Withdrawal.\n(3)Logout.\n(4) Exit.\n'))
    except ValueError:
        print('Input was not a number')
        bankOperations(user)
    if (SelectedOption == 1):
        depositsOperation(user)
    elif(SelectedOption == 2):
        withdrawalOperation(user)
    elif(SelectedOption == 3):
        print('You have successfully Logout.\nTo perform another transaction please login.')
        logout()
    elif( SelectedOption == 4):
        print('You are exiting the application.')
        exit()
    else:
        print('Invalid option selected.')
        bankOperations(user)




def withdrawalOperation(user):
    '''
    withdrawal operations.
    '''
    try:

        userWithdrawal = int(input('Enter ammount to withdrawal?\n'))
    except ValueError:
        print('Input was not a number')
        withdrawalOperation(user)
    if (len(user) != 5):
        print('Please deposit into your account')
        bankOperations(user)

    elif (userWithdrawal <= int(user[-1]) and int(user[-1]) > 0):
        newBalance = user[-1] - userWithdrawal
        user[-1]= newBalance
        print('Please take your cash.')
        bankOperations(user)

    
    elif (userWithdrawal > int(user[-1])):
        print('Insufficent funds.')
        bankOperations(user)


def depositsOperation(user):
    '''
    deposit operations.
    '''
    try:
        deposits = int(input('enter the ammount you want to deposit?\n'))
    except ValueError:
        print('Input was not a number')
        depositsOperation(user)
    if (len(user) != 5):
        user.append(deposits)
        print('You have successfully made your first deposits.\nyou deposited # %d' %user[-1])
        bankOperations(user)
        
    elif (len(user) == 5):
        user[-1] =+ deposits
        print('You have sucessfully deposited.')
        bankOperations(user)

def logout():
    """
    function for logging out 
    """
    login()


def forgottenInfo():
    """
    function to reset your account. 
    """

    for accountNo, userDetail in databaseOfAccounts.items():
        try:
            forgottenInfo = int(input('Forgotten account number enter 1.\nForgotten password enter 2.\n'))
        except ValueError:
            print('Input was not a number')
            forgottenInfo()
        if (forgottenInfo == 1):
            print('To validate it is you.')
            email= input('Please enter your email?\n')
            lastName = input('Please enter your last name?\n')
            password = input('please enter your password?\n')
            
            if (email == userDetail[0]):
                if (lastName == userDetail[2]):
                    if(password == userDetail[3]):
                        print('Your Account Number is %d.\nPlease keep it safe.' %accountNo)
            login()

        elif (forgottenInfo == 2):
            print('To validate it is you.')
            accountNumber = int(input('Please enter your acount number?'))
            email= input('Please enter your email?\n')
            lastName = input('Please enter your last name?\n')
            if (accountNumber == accountNo):
                if (email == userDetail[0]):
                    if (lastName == userDetail[2]):
                        print('You are validated.\nPlease enter your new password')
                        newPass = input('Please enter your new password?\n')
                        reNewPass = input('Please repeat your new password?\n')
                        if (newPass == reNewPass):
                            userDetail[3] = newPass
                            print('Your password has be reset. Please keep it safe.')     
            login()

        else:
            print('Invalid option')
            forgottenInfo()


print( init())

