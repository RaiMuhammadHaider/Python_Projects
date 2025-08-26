import re
email_condition = "^[A-Z a-z 0-9.]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
User_email = input('Enter Your Email : ')

if re.search(email_condition,User_email):
    print('Email is Valid')
else:
    print('Email is not Valid') 