def account_number_validation(account_number):
    if account_number:
    
        try:
            int(account_number)
            if len(str(account_number)) == 10:
                return True
            
        except ValueError:
            # print('Invalid Account number, account number should be an integer.')
            return False

        except TypeError:
            # print('Invalid account type')
            return False

    else:
        # print('account bumber is required field')
        return False
