#Name: Abdulrahman Ashraf Mohamed Ahmed Hassan          ID: 20231094



#convert from binary to decimal
def binary_to_decimal1(num):
    arr = list(num)
    result = 0
    n = 0
    i = -1
    while n < len(arr):
         result = result + int(arr[i]) * (2 ** n)
         i-= 1
         n+= 1
    print("The decimal number is : ")
    print(result)


#convert from decimal to binary
def decimal_to_binary1(num):
   arr = []
   while int(num) > 0:
        arr.append(int(num) % 2)
        num = int(num) // 2
   arr.reverse()
   print("The binary number is : ")
   for i in arr :
      print(i,end="")



#convert from octal to decimal
def octal_to_decimal1(num):
    arr = list(num)
    result = 0
    n = 0
    i = -1
    while n < len(arr):
          result = result + int(arr[i]) * (8 ** n)
          i-= 1
          n+= 1
    print("The decimal number is : ")
    print(result)



#convert from decimal to octal
def decimal_to_octal1(num):
    arr = []
    while int(num) > 0:
        arr.append(int(num) % 8)
        num = int(num) // 8
    arr.reverse()
    print("The octal number is : ")
    for i in arr:
        print(i, end="")


#convert from decimal to hexa
def decimal_to_hexa1(num):

    arr = []
    while int(num) > 0:
        if (int(num) % 16) < 10:
            arr.append(num % 16)
        if (int(num) % 16) == 10:
            arr.append("A")
        if (int(num) % 16) == 11:
            arr.append("B")
        if (int(num) % 16) == 12:
            arr.append("C")
        if (int(num) % 16) == 13:
            arr.append("D")
        if (int(num) % 16) == 14:
            arr.append("E")
        if (int(num) % 16) == 15:
            arr.append("F")
        num = int(num) // 16
    arr.reverse()
    print("The hexadecimal is : ")
    for i in arr:
        print(i, end="")


# convert from hexa to decimal
def hexa_to_decimal1(num):
    hexa_num = num.strip().upper()
    table = {
        '0': 0, '1': 1, '2': 2, '3': 3,
        '4': 4, '5': 5, '6': 6, '7': 7,
        '8': 8, '9': 9, 'A': 10, 'B': 11,
        'C': 12, 'D': 13, 'E': 14, 'F': 15}
    position = len(hexa_num) - 1
    decimal_number = 0

    for x in hexa_num:
        decimal_number = decimal_number + table[x] * pow(16, position)
        position-= 1
    print("The decimal number is : ", decimal_number)


#convert from binary to decimal
def binary_to_decimal(num):         #was created to
    arr = list(num)
    result = 0
    n = 0
    i = -1
    while n < len(arr):
         result = result + int(arr[i]) * (2 ** n)
         i-= 1
         n+= 1
    return result


#convert from decimal to binary
def decimal_to_binary(num):
   arr = []
   while int(num) > 0:
        arr.append(int(num) % 2)
        num = int(num) // 2
   arr.reverse()
   print("The binary number is : ")
   for i in arr :
      print(i,end="")


#convert from octal to decimal
def octal_to_decimal(num):
    arr = list(num)
    result = 0
    n = 0
    i = -1
    while n < len(arr):
          result = result + int(arr[i]) * (8 ** n)
          i-= 1
          n+= 1
    return result



#convert from decimal to octal
def decimal_to_octal(num):
    arr = []
    while int(num) > 0:
        arr.append(int(num) % 8)
        num = int(num) // 8
    arr.reverse()
    print("The octal number is : ")
    for i in arr:
        print(i,end="")




#convert from decimal to hexa
def decimal_to_hexa(num):
    arr = []
    while int(num) > 0:
        if (int(num) % 16) < 10:
            arr.append(int(num) % 16)
        if (int(num)% 16) == 10:
            arr.append("A")
        if (int(num) % 16) == 11:
            arr.append("B")
        if (int(num) % 16) == 12:
            arr.append("C")
        if (int(num) % 16) == 13:
            arr.append("D")
        if (int(num) % 16) == 14:
            arr.append("E")
        if (int(num) % 16) == 15:
            arr.append("F")
        num = int(num) // 16
    arr.reverse()
    print("The hexadecimal is : ")
    for i in arr:
        print(i,end="")



# convert from hexa to decimal
def hexa_to_decimal(num):
    hexa_num = num.strip().upper()              #the built in function strip() :it removes commas and spaces
    table = {
        '0': 0, '1': 1, '2': 2, '3': 3,
        '4': 4, '5': 5, '6': 6, '7': 7,
        '8': 8, '9': 9, 'A': 10, 'B': 11,
        'C': 12, 'D': 13, 'E': 14, 'F': 15}
    position = len(hexa_num) - 1
    decimal_number = 0

    for x in hexa_num:
        decimal_number = decimal_number + table[x] * pow(16, position)
        position -= 1
    return decimal_number


#convert from binary to octal
def binary_to_octal(num):
    num1 = binary_to_decimal(num)
    decimal_to_octal(num1)


#convert from binary to hexa
def binary_to_hexa(num):
    hex = binary_to_decimal(num)
    decimal_to_hexa(hex)


#convert from octal to binary
def octal_to_binary(num):
    bin = octal_to_decimal(num)
    decimal_to_binary(bin)


#convert from hexa to binary
def hexa_to_binary(num):
    bin = hexa_to_decimal(num)
    decimal_to_binary(bin)


#convert from octal to hexa
def octal_to_hexa(num):
   hex = octal_to_decimal(num)
   decimal_to_hexa(hex)


#convert from hexa to octal
def hexa_to_octal(num):
    oct = hexa_to_decimal(num)
    decimal_to_octal(oct)

#menu
def menu():
    while True:
        print()
        print("**=> Numbering System Converter <=**")
        print("A) insert a new number\nB) Exit program")

        choice = input("choice is ").upper()

        if choice.upper() == "A":
            num = input("==>please insert a number : ").upper()  # (num)is the number which user will insert

            if all(char in '0123456789ABCDEFG' for char in str(num)):   #check if the insert number is valid or not
                print("Number entered", num)
            else:
                print("=> please insert a valid number")

                continue

        elif choice.upper() == "B":
            print("program exited")

            break

        else:                                                            #check if the choice is valid or not
            print("=>Error:please select a valid choice")

            continue

        print("*please select the base you want to convert a number from*")
        print("A) Decimal \nB) binary\nC) octal\nD) hexadecimal")
        base_from = input("choose the base to convert from: ").upper()
        if base_from == "A" or base_from == "B" or base_from == "C" or base_from == "D":     #check if the choice is valid or not
            print("the base you chose to convert from is:", base_from)
            if base_from == "B" and all(char in '01' for char in str(num)):    #check if the insert number is binary or not
                print()
            elif base_from == "C" and all(char in '01234567' for char in str(num)):    #check if the insert number is octal or not
                print()
            elif base_from == "A" and all(char in '0123456789' for char in str(num)):      #check if the insert number is Decimal or not
                print()
            elif base_from == "D" and all(char in '0123456789ABCDEF' for char in str(num)):     #check if the insert number is hexadecimal or not
                print()

            else:
                print("=>Error: please insert a valid number")

                continue
        else:
            print("=>Error: please select a valid choice")

            continue

        print("** Please select the base you want to convert a number to **")
        print("A) Decimal \nB) binary\nC) octal\nD) hexadecimal")
        base_to = input("choose the base to convert to: ").upper()
        if base_to == "A" or base_to == "B" or base_to == "C" or base_to == "D":         #check if the choice is valid or not
            print("the base you choose to convert to is: ", base_to)
        else:
            print("=>Error: please select a valid choice")

            continue

        if base_from == "A" and base_to == "B":             #calling to the function decimal_to_binary1(num) if user choiced base_from is decimal and base_to is binary
            decimal_to_binary1(num)
        elif base_from == "A" and base_to == "C":        #calling to the function decimal_to_octal1(num) if user choiced base_from is decimal and base_to is octal
            decimal_to_octal1(num)
        elif base_from == "A" and base_to == "D":           #calling to the function decimal_to_hexa1(num) if user choiced base_from is decimal and base_to is hexa
            decimal_to_hexa1(num)
        elif base_from == "B" and base_to == "A":       #calling to the function binary_to_decimal1(num) if user choiced base_from is binary and base_to is decimal
            binary_to_decimal1(num)
        elif base_from == "B" and base_to == "C":       #calling to the function binary_to_octal(num) if user choiced base_from is binary and base_to is octal
            binary_to_octal(num)
        elif base_from == "B" and base_to == "D":       #calling to the function binary_to_hexa(num) if user choiced base_from is binary and base_to is hexa
            binary_to_hexa(num)
        elif base_from == "C" and base_to == "A":       #calling to the function octal_to_decimal1(num) if user choiced base_from is octal and base_to is decimal
            octal_to_decimal1(num)
        elif base_from == "D" and base_to == "A":       #calling to the function hexa_to_decimal1(num) if user choiced base_from is hexa and base_to is decimal
            hexa_to_decimal1(num)
        elif base_from == "C" and base_to == "B":       #calling to the function octal_to_binary(num) if user choiced base_from is octal and base_to is binary
            octal_to_binary(num)
        elif base_from == "C" and base_to == "D":       #calling to the function octal_to_hexa(num) if user choiced base_from is octal and base_to is hexa
            octal_to_hexa(num)
        elif base_from == "D" and base_to == "B":       #calling to the function hexa_to_binary(num) if user choiced base_from is hexa and base_to is binary
            hexa_to_binary(num)
        elif base_from == "D" and base_to == "C":       #calling to the function hexa_to_octal(num) if user choiced base_from is hexa and base_to is octal
            hexa_to_octal(num)

menu()


                                    #****TEST****


#decimal_to_binary1(123)
'''expected: 1111011
output: 1111011'''

#decimal_to_octal1(123)
'''expected: 173
output: 173'''

#decimal_to_hexa1(123)
'''expected: 7B
output: 7B'''

#binary_to_decimal1('1101')
'''expected: 13
output: 13'''

#binary_to_octal('1101')
'''expected: 15
output: 15'''

#binary_to_hexa('1101')
'''expected: D
output: D'''

#octal_to_decimal1('161')
'''expected: 113
output: 113'''

#hexa_to_decimal1('928')
'''expected: 2344
output: 2344'''

#octal_to_binary('161')
'''expected: 1110001
output: 1110001'''

#octal_to_hexa('161')
'''expected: 71
output: 71'''

#hexa_to_binary('928')
'''expected: 100100101000
output: 100100101000'''

#hexa_to_octal('928')
'''expected: 4450
output: 4450'''