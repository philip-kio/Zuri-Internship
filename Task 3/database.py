# create record

# find user



import os
import validation



user_db_path = 'data/user_record/'

def create(user_account_number,firstName,lastName,email, password):
    if does_acount_exist(user_account_number):
        return False
    prepared_user_details = firstName + ',' + lastName + ',' + email + ',' + password
    if does_email_exist(email):
        print('user already exists.')
        return False

    completion_state = False

    try:

        file = open(user_db_path +  str(user_account_number) + '.txt', 'x' )
        

    except FileExistsError:
       does_file_contain_data = read(user_db_path +  str(user_account_number) + '.txt' )
       if not does_file_contain_data:
           delete(user_account_number)



        

    else:
        file.write(str(prepared_user_details));
        completion_state = True
        file.close();
    
    return completion_state 

# create a file
# name of the file would be account-number.txt
# add user detail to the file 
# return true

def does_acount_exist(user_account_number):
    
    # find user with account number
    # fetch the content of the file
    all_users= os.listdir(user_db_path)
    
    
    for user in all_users:
        
        if user == str(user_account_number)+ '.txt':
            
            return True
    else: 
        return False


def does_email_exist(email):
    
    # find user with account number
    # fetch the content of the file
    all_user = os.listdir(user_db_path)
    
    for user in all_user:
        userlist= read(user).split(',')
        if email in userlist:
            return True
        else: 
            return False




def update(user_details):
    pass
# find user with account number
# fetch the content of the file
#update the conetent of the file and save

def read(user_account_number):
    # find user with account number
    # fetch the content of the file
    #update the conetent of the file and save
    is_valid_account_number = validation.account_number_validation(user_account_number)
    try:
        if is_valid_account_number:
            file = open(user_db_path +  str(user_account_number) + '.txt', 'r' )
            
        else:
            file = open(user_db_path + user_account_number, 'r')
    except FileNotFoundError:
        return 'user not found.'
    except FileExistsError:
        return 'user doesn\'t exist' 
    except TypeError:
        print('Invlid account number format')
    else:
        return file.readline()
    return False





def delete(user_account_number):
    validate =False
    try:
        if type(user_account_number) == int:
            validate = True
    except ValueError:
        return 'error in account number'  

    finally:
        is_delete_successful = False


        if os.path.exists(user_db_path+ str(user_account_number) +'.txt'):

            try:
                os.remove(user_db_path + str(user_account_number)+'.txt')
                is_delete_successful = True


            except FileNotFoundError:
                print('file not  found')


            finally:
                return is_delete_successful


        else:

            print('file %d does not exist.'%(user_account_number)) 

            return is_delete_successful



def authenticated_user(account_number, password):
    if does_acount_exist(account_number):
        
        user = read(account_number).split(',')
        if password == user[3]:
            return user
    return False

# create(5873434638, ['h','h','h','h'])
# print(does_email_exist('philip@zuri.team'))
# print(does_acount_exist(8302458221))
# print(authenticated_user(8302458221,'wemove3'))