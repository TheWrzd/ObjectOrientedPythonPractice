
accountsList = []

def newAccount(aName, aBalance, aPassword):
    global accountsList
    newAccountDict = {'name': aName, 'balance': aBalance, 'password': aPassword}
    accountsList.append(newAccountDict)

def show(accountNumber):
    global accountsList
    print('Account', accountNumber)
    thisAccountDict = accountsList[accountNumber]
    print('     Name: ', thisAccountDict['name'])
    print('     Balance: ', thisAccountDict['balance'])
    print('     Password: ', thisAccountDict['password'])
    print()

def getBalance(accountNumber, password):
    global accountsList
    thisAccountDict = accountsList[accountNumber]
    if thisAccountDict['password'] != password:
            print('incorrect password')
            return None
    return thisAccountDict['balance']

def deposit(accountNumber, depositAmount, password):
    global accountsList
    thisAccountDict = accountsList[accountNumber]
    if password != thisAccountDict['password']:
        print('incorrect password')
        return None
    thisAccountDict['balance'] = int(thisAccountDict['balance'])
    thisAccountDict['balance'] = thisAccountDict['balance'] + int(depositAmount)
    accountsList[accountNumber] = thisAccountDict
    return getBalance(accountNumber, password)

def withdraw(accountNumber, withdrawAmount, password):
    global accountsList
    thisAccountDict = accountsList[accountNumber]
    if password != thisAccountDict['password']:
        print('incorrect password')
        return None
    thisAccountDict['balance'] = int(thisAccountDict['balance'])
    thisAccountDict['balance'] = thisAccountDict['balance'] - int(withdrawAmount)
    accountsList[accountNumber] = thisAccountDict
    return getBalance(accountNumber,password)


#Create two sample accounts
print("Oz account number: ",len(accountsList))
newAccount("Oz","5000","vamp")

print("lamarr's account nubmer: ", len(accountsList))
newAccount("LaMarr","99000", "open")

while True:
    print()
    print()
    print('Press b to get the balance')
    print('Press d to make a deposit')
    print('Press n to create a new accout')
    print('Press w to make a withdrawal')
    print('Press s to show all actions')
    print('Press q to quit')
    print()

    action = input('what do you want to do? ')
    action = action.lower() #set to lower case
    action = action[0] #just use the first char
    print()

    if action == 'b':
        print('Get Balance: ')
        userAccountNumber = input('Please enther your account number: ')
        userAccountNumber = int(userAccountNumber)
        password = input('Please enter your password: ')
        theBalance = getBalance(userAccountNumber, password)
        if theBalance is not None:
            print('Your balance is : ', theBalance)
    
    elif action == 'd':
        print('Deposit:')
        userAccountNumber = input('Please enter account number: ')
        userAccountNumber = int(userAccountNumber)
        userDepositAmount = input('Please enter amount to deposit: ')
        userPassword = input('Please enter the password: ')

        newBalance = deposit(userAccountNumber, userDepositAmount, userPassword)
        if newBalance is not None:
            print('Your new balance is : ', newBalance)
    
    elif action == 'n':
        print('New Account:')
        userName = input('What is your name? :')
        userStartingAmount = input('What is the amount of your intial deposit? :')
        userStartingAmount = int(userStartingAmount)
        userPassword = input('What password would you like set for your account? :')

        userAccountNumber = len(accountsList)
        newAccount(userName, userStartingAmount, userPassword)
        print('Your new account number is: ', userAccountNumber)

    elif action == 'w':
        print('Withdraw')
        userAccountNumber = input('Please enter account number: ')
        userAccountNumber = int(userAccountNumber)
        userWithdrawAmount = input('What is the amount of your withdraw? :')
        userPassword = input('Please enter you password: ')

        newBalance = withdraw(userAccountNumber,userWithdrawAmount, userPassword)
        if newBalance is not None:
            print("Your new Balance is : ", newBalance)
    
    elif action == 's':
        print()
        print('Press b to get the balance')
        print('Press d to make a deposit')
        print('Press n to create a new accout')
        print('Press w to make a withdrawal')
        print('Press s to show all actions')
        print('Press q to quit')
    
    elif action == 'q':
        break
        
print('Done')