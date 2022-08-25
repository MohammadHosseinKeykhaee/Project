import math

use = int(input('chand bar mikhahid az mashinhesab estefade konid?: '))
basic_advanced = input('B = Basic or A= Advanced?): ')

if basic_advanced == 'B' or basic_advanced =='b' or basic_advanced =='Basic' or basic_advanced == 'basic':
    for i in range(use):
        op = input('\nEnter the operator\n+ or sum, - or subtract \n/ or division, * or multiply: ')
        num1 = float(input('please enter firt number: '))
        num2 = float(input('please enter second number: '))
        if op == '+' or op == 'sum' or op == 'jam':
            jam = num1 + num2
            print('\nhasele jame', num1, 'and', num2,  'is:', jam)
        elif op == '-' or op == 'subtract' or op == 'menha':
            tafrigh = num1 - num2
            print('\nhasel tafrighe', num1, 'az', num2, 'is: ', tafrigh)
        elif op == '*' or op == 'multiply' or op == 'zarb':
            zarb = num1 * num2
            print('\nhasele zarbe', num1, 'dar', num2, 'is: ', zarb)
        elif op == '/' or op == 'division' or op == 'taghsim':
            if num2 == 0:
                print('\nError...taghsim bar sefr mojaz nist')
                continue
            else:
                taghsim = num1 / num2
                print('\nhasel taghsime', num1, 'bar', num2, 'is: ', taghsim)
        
        else:
            print('\nError....operator ra dorost vared nakardid')
            continue
        print('\shoma', i + 1 ,'az mashin hesab estefadeh kardid')

elif basic_advanced == 'A' or basic_advanced =='a' or basic_advanced =='Advanced' or basic_advanced == 'advanced':
    for i in range(use):
        op = input('\noperator ra entekhab konid\n// or correctdivision, mod or baghimandeh\n ^2 or power2, ^ or power or tavan\n | ghadremotlagh or absolutevalue, sin, cos, tan, cot\n √ or squareroot or jazr, primenumber or Adade aval: ')
        num1 = float(input('Enter number: '))
        if op == '^2' or op == 'power2' or op == 'tavan' or op == '|' or op == 'absolutevalue' or op == 'ghadrmotlagh' or op == 'sin' or op == 'cos' or op == 'tan' or op == 'cot' or op == '√' or op == 'squareroot' or op == 'primenumber' or op == 'Adade aval' :
            if op == '^2' or op == 'power2' or op == 'tavan':
                power_2 = math.pow(num1,2)
                print('\n', num1, 'to power of 2: ', power_2)
            elif op == '|' or op == 'absolutevalue' or op == 'ghadrmotlagh':
                ghadremotlagh = math.fabs(num1)
                print('\nghadre motlaghe', num1, 'is: ', ghadremotlagh)
            elif op == 'sin':
                sin = math.sin(num1)
                print('\nsine', num1, 'hast:', sin)
            elif op == 'cos':
                cos = math.cos(num1)
                print('\ncosine', num1, 'hast:', cos)
            elif op == 'tan':
                tan = math.tan(num1)
                print('\ntangent', num1, 'hast:', tan)
            elif op == 'cot':
                cot = math.atan(num1)
                print('\ntangent', num1, 'hast:', cot)
            elif op == '√' or op == 'squareroot' or op == 'jazr':
                sr = math.sqrt(num1)
                print('\nJazre', num1, 'hast:', sr)
            elif op == 'Adade aval' or op == 'prime number':
                num1 = int(num1)
                if num1 > 1:
                 for i in range(2,num1):
                    if (num1 % i) == 0:
                        print(num1,"adade aval nist")
                        break
                 else:
                     print(num1,"adade aval ast")
        elif op == '//' or op == 'correctdivision' or op == 'mod' or op == 'remaining' or op== 'baghimande' or op == '^' or op == 'power':
            num2 = float(input('Enter number: '))
            if op == '//' or op == 'correctdivision':
                if num2 == 0:
                    print('Error')
                    continue
                else:
                    cd = num1 // num2
                    print('\ncorrect division of', num1, 'by', num2, ': ', cd)
            elif op == 'mod' or op == 'remaining' or op == 'baghimande':
                if num2 == 0:
                    print('Error')
                    continue
                else:
                    mod = num1 % num2
                    print('\nmod', num1, 'va', num2, 'hast: ', mod)
            elif op == '^' or op == 'power':
                pow = math.pow(num1, num2)
                print('\n', num1, 'to power of',num2, ':', pow)
        else:
            print('\nError....operator ra dorost vared nakardid')
            continue
        print('\shoma', i + 1 ,'bar az mashin hesab estefadeh kardid')
else:
    print('\operatot tarif nashodeh')