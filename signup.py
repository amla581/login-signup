import json
import os
main_dict={}
list=[]
dic_out={}
user_info={}
if os.path.exists("userdetails.json"):
    pass
else:
    f=open("userdetails.json","w+")
    f.close()
choose = int(input("choose 1. for sign up or 2. for log in="))
if choose == 1:
    name=input("enter your first and last name__=")
    pas=input("enter your password (password should conatain Upper,Small Letter, Special Character and number)=")
    u,l,d,s=0,0,0,0
    for check in pas:
        if (check.isupper()):
            u+=1
        if (check.isdigit()):
            d+=1
        if (check.islower()):
            l+=1
        if(check=='@'or check=='$' or check=='_'):
            s+=1
        if(os.path.isfile('Signup_page.json')):
            op=open("Signup_page.json","r")
            aaa=json.load(op)
            for i in aaa["User"]:
                if i["username"]==name:
                    print("This user is Already Exists")
                    break    
    try:        
        with open("userdetails.json","r") as output:
                user_data=json.load(output)
                for info in user_data["user"]:
                    pass
    except:
        pass
    if (l>=1 and u>=1 and s>=1 and d>=1 and l+s+u+d==len(pas)):
        pas1=input("enter your password again=")
        if pas==pas1: 
            if os.stat("userdetails.json"):
                print("Congracts",name,"You are signed up Succesfully")
                description=input("Enter your Description=")
                birth_date=input("enter Your Date Of Birth=")
                Gender=input("enter your Gender=")
                hobbies=input("Enter Your hobby=")
        
                user_info["description"]=description
                user_info["d_o_b"]=birth_date
                user_info["Gender"]=Gender
                user_info["Hobbies"]=hobbies
                dic_out["Username"]=name
                dic_out["Password"]=pas
                dic_out["Profile"]=user_info
                list.append(dic_out)
                main_dict["user"]=list
            try:
                with open("userdetails.json","r+") as file:
                    read_file= file.read()
                    userdata=json.loads(read_file)
                    for i in userdata:
                        if i =="user":
                            x=userdata[i]
                            x.append(dic_out.copy())
                            main_dict["user"]=x
                            json.dumps(main_dict,file)
                            file.close()
                    
            except:
                with open("userdetails.json","w") as f:
                    f.write(json.dumps(main_dict, indent=4))
        # else:
            # if check["username"]!=name and check["password"]!=pas:
                # print("you successful s")
            # else:
                # print("already exist")


elif choose==2:
    user_name=input("enter your username=")
    log_in_password=input("enter your Log in Password=")
    with open("userdetails.json","r") as log_in_file:
        log_in_info=json.load(log_in_file)
        for output_data in log_in_info["user"]:
            if output_data["Username"] == user_name and output_data["Password"]==log_in_password:
                print("********************************************")
                print(user_name+ "You Logged In Succesfully","\U0001F929")
                print("................")
                print("     PROFILE       ")
                print("................")
                print("Username",":",output_data["Username"])
                print("Gender",":",output_data["Profile"]["Gender"])
                print("Bio",":",output_data["Profile"]["description"])
                print("Dob",":",output_data["Profile"]["d_o_b"])
                break
        else:
            print("Password and username are Invalid")