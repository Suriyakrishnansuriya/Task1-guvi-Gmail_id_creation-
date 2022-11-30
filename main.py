
"""---> email/username should have "@" and followed by "."
      eg:- sherlock@gmail.com
            nothing@yahoo.in

---> it should not be like this 
       eg:- @gmail.com
            there should not be any "." immediate next to "@"
            eg:- my@.in
            it should not start with special characters and numbers
eg:- 123#@gmail.com

---> password (5 < password length > 16)
              Must have minimum one special character,
              one digit,
              one uppercase, 
              one lowercase character"""

# create user name
name = input('Enter your Name: ')
import re
x=True
if len(name) > 16 or re.search('[A-Z0-9]',name):
    print('entered invalid answer')
else:
    if name.isalpha():
        if name == name.upper():
            print('capital letters not allowed')
        elif name.isspace():
            print('input error')
        elif re.search('\d', name):
            print('input error')
        elif re.search('[0-9]', name):
            print('error')
        else:
            # email id create
            email = input('Enter your email id: ')
            if len(email) >= 8:
                if email[0].isalpha():
                    if ('@' in email) and (email.count('@') == 1):
                        if (email[-4] == '.') ^ (email[-3] == '.'):
                            if ('.' in email) and (email.count('.') == 1):
                                for i in email:
                                    if i.isalpha():
                                        if i == i.upper():
                                            print('capital letters not allowed')

                                    elif i.isspace():
                                        print('space not allowed')
                                    elif i.isdigit():
                                        continue
                                    elif i == '_' or '.' or '@':
                                        # password program
                                        import re
                                        p = input("Enter your password: ")
                                        if (len(p) < 6 or len(p) > 12):
                                            print('invalid input')
                                            if not re.search("[a-z]", p):
                                                break
                                            elif not re.search("[0-9]", p):
                                                break
                                            elif not re.search("[A-Z]", p):
                                                break
                                            elif not re.search("[$#@]", p):
                                                break
                                            elif re.search("\s", p):
                                                break
                                        else:
                                            print("Valid Password")
                                            import pickle
                                            #creating
                                            results = {name, email, p}
                                            with open('pickle.txt', 'ab') as f:
                                                pickle.dump(results, f)
                                            #reopen
                                            with open('pickle.txt', 'rb') as f:
                                                new_results=pickle.load(f)
                                                old_results=pickle.load(f)
                                                if old_results!=new_results:
                                                    print('your Email id is created successfully')
                                                else:
                                                    print("this email id is already available please try to log in")
                                            break

                                    else:
                                        print('email id is wrong')
                            else:
                                print('invalid input')
                        else:
                            print('please enter valid server detail')
                    else:
                        print('@ not more than one letter')
                else:
                    print('first letter not be in Number')
            else:
                print('input error')

'''import pickle
f=open('pickle.txt','rb')
new_results= pickle.load(f)
if results==new_results:
    print('email id is alredy exits')'''
'''A=list(new_results)
if A[0] or A[1]==A[0] or A[1]:
    '''

'''class customer:
    def __init__(self, name, email, p):
        self.email=email
        print('email id is alredy exits')'''

