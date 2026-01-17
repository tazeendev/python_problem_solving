user_name=input('Enter the user name :')
password=int(input('Enter the passwords :'))
if user_name == 'admin' and password == 123456 :
    print('Login successfully')
else:
    print('Inavalid user name or password')