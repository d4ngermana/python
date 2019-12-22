username = input('Your Username?')
password = input('Enter Your Password')

password_length = len(password)
password_string = '*' * password_length

print(f'Hey {username}, Your password {password_string} is {password_length} letters long')