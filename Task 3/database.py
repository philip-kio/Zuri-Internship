# create record

# find user



import os

user_db_path = 'data/user_record/'

def create(account_number,user_detail):

    completion_state = False

    try:

        file = open(user_db_path +  str(account_number) + '.txt', 'x' )
        

    except FileExistsError:
        print('user already exist.')


        

    else:
        file.write(str(user_detail));
        completion_state = True
        file.close();
    
    return completion_state 

# create a file
# name of the file would be account-number.txt
# add user detail to the file 
# return true


def find(user_account_number):
    pass
    # find user with account number
    # fetch the content of the file






def update(user_details):
    pass
# find user with account number
# fetch the content of the file
#update the conetent of the file and save

def read(user_account_number):
    # find user with account number
    # fetch the content of the file
    #update the conetent of the file and save
    pass




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



# create(5873434638, ['h','h','h','h'])
print(delete(5873434638))