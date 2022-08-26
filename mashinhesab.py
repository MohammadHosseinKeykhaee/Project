## Mashin hesab  Basic :  + - / *  %%%%%%  Advanced : //, mod, ^2,  ^n, | | , sin, cos , tan , cot , √ , pr: (adade aval)
import math
use = int(input('chand bar mikhahid az mashinhesab estefade konid?: '))
use_type = input('B = Basic or A= Advanced?): ')
if use_type == "B" or use_type == "b" or use_type == "Basic":
    for i in range(use):
        num1 = float(input("Enter number 1:"))
        num2= float(input("Enter number 2:"))
        op_list = ["Enter operator:", "+",   "-" ,   "*" , "/" , "option goftari farsi:" ,  "jam" , "tafrigh" , "zarb" , "taghsim"] 
        print('\n'.join( op_list))    # faghat bareye nameyeshe liste option haye mojood be karbar 
        op_list = input([" Button (Enter operator)", "+",   "-" ,   "*" , "/" , "option goftari farsi:" ,  "jam" , "tafrigh" , "zarb" , "taghsim", ":"] )
        if op_list == "+"  or op_list == "jam":
             
             total = num1+num2
             print ("Answer =", total)
        elif op_list == "-" or op_list == "tafrigh":
            
            total = num1-num2
            print ("Answer =", total)
        elif op_list == "*" or op_list == "zarb":
            
            total = num1*num2
            print ("Answer =", total)
        elif op_list == "/" or op_list == "taghsim":
             if num2 == 0:
                print('Error...taghsim bar sefr mojaz nist')
                print('shoma', i + 1 ,'bar az mashin hesab estefadeh kardid')
                continue
             else:
                 total = num1 / num2
                 print ("Answer =", total)
        else:
            print('Error....operator ra dorost vared nakardid')
            continue
        print('shoma', i + 1 ,'bar az mashin hesab estefadeh kardid') 
##########     (Advanced) #########
elif use_type == "A" or use_type == "a" or use_type == "Advanced" or use_type == "advanced":
    for i in range(use):
        num1 = float(input("Enter number 1:"))
        op_list =["Enter operator:",  "//", "mod", "^2",  "^n", "| |" , "sin", "cos" , "tan" , "cot" , "√ ", "pr: (adade aval)" , "option goftari farsi:", "taghsim sahih", "baghimandeh", "tavane 2", "tavane adad", "ghadre motlagh" , "sinus", "cosinus, tangant", "cotangant", "jazr", "adade aval"]
        print('\n'.join( op_list))    # faghat bareye nameyeshe liste option haye mojood be karbar
        op_list = input([" Button (Enter operator):",  "//", "mod", "^2",  "^", "| |" , "sin", "cos" , "tan" , "cot" , "√ ", "pr: (adade aval)" , "option goftari farsi:", "taghsim sahih", "baghimandeh", "tavane 2", "tavane adadi", "ghadremotlagh" , "sinus", "cosinus, tangant", "cotangant", "jazr", "adade aval"])
        if op_list == "||"  or op_list == "ghadremotlagh":
           total = math.fabs(num1)
           print('ghadre motlaghe =', total)
        elif op_list == "√ "  or op_list == "jazr":
            total = math.sqrt(num1)
            print('jazr =', total)
        elif op_list == "mod"  or op_list == "baghimandeh":
             num2 = float(input('Enter number 2:'))
             if num2 == 0:
                print('Error')
                continue
             total = num1 % num2
             print(num1,"%",num2,"=","mod (baghimandeh ) =" , total)
        elif op_list == '//'  or op_list ==  'taghsim sahih':
            num2 = float(input('Enter number 2:'))
            if num2 == 0:
                print('Error')
                continue
            else:
                total = num1 // num2
                print(num1,'//',num2,"=", "taghsim sahih =", total)
        elif  op_list == '^2' or op_list == 'tavan2':
            total = math.pow(num1,2)
            print(num1, "^2 =",total )
        elif  op_list == '^' or op_list == 'tavan adai':
            num2 = float(input('Enter number 2:'))
            total = math.pow(num1,num2)
            print(num1, "^", num2, " = " ,total)
        elif op_list == 'pr' or op_list == 'adade aval':
            num1 = int(num1)
            if num1>1:
                for i in range(2,num1//2):
                     if(num1%i)==0:
                        print(num1,"adade aval nist")
                        break
                else:
                    print(num1,"adade aval ast")
            else:
                print(num1,"na aval ast va na adade morakad")
        elif op_list == 'sin' or op_list == 'sinus':
             total = math.sin(num1)
             print('Answer=', total)
        elif op_list == 'cos' or op_list == 'cosinus':
             total = math.cos(num1)
             print('Answer=', total)
        elif op_list == 'tan' or op_list == 'tangant':
             total = math.tan(num1)
             print('Answer=', total)
        elif op_list == 'cot' or op_list == 'cotangant':
             total = math.atan(num1)
             print('Answer=', total)
        else:
            print('\nError....operator ra dorost vared nakardid')
        continue
    print('\shoma', i + 1 ,'bar az mashin hesab estefadeh kardid')
else:
    print('\operatot tarif nashodeh')
