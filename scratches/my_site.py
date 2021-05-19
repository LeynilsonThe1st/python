user_first_name = str(input('First name: ')).capitalize()
user_last_name = str(input('Last name: ')).capitalize()
user_full_name = user_first_name + ' ' + user_last_name

if user_full_name.strip().isalpha():
    print(user_full_name)
else:
    print('\n\t invalid name')
        
print(type(user_full_name))

print(user_full_name.strip())


user_id = input('Your ID: ')

print('\n\t Fullname: ', user_full_name)


class User:
    __name = ''
    __email = ''

    def __init__(self, name, email):
        self.__name = name
        self.__email = email

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_email(self, email):
        self.__email = email

    def get_email(self):
        return self.__email


leynilson = User('leynilson', 'leynilson_harden@hotmail.com')

print(leynilson.get_email())
