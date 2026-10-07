email=input("Enter your email:")
k,j,d=0,0,0
if len(email)>=6:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@")==1):
            if (email[-4]==".") ^ (email[-3]=="."):
                for i in email:
                    if i.isspace():
                        k=1
                    elif i.isalpha():
                        if i==i.upper():
                            j=1
                    elif i.isdigit():
                        continue
                    elif i=="_" or i=="." or i=="@":
                        continue
                    else:
                        d=1
                if k==1 or j==1 or d==1:
                    print('''Wrong email because:
                            1. Email has space
                            2. Email has upper case alphabets
                            3. Email has any other special characters
                          ''')
                else:
                    print("Right Email")
                        
            else:
                print("Wrong email -'.' should be at 3rd or 4th position from the end")
        else:
            print("Wrong email - @ should be present in the email and it should be present only once")
    else:
        print("Wrong email - First character should be an alphabet")
else:
    print("Wrong Email - length of the email should be greater than 6")
