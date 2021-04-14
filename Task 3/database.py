# create record

# find user





def create(account_number,user_detail):

    completion_state = False

    try:

        file = open('data/user_record/'+ str(account_number) + '.txt', 'x' )
        

    except FileExistsError:
        print('user already exist.')

        return completion_state

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
    pass 


create(5873434638, ['h','h','h','h'])