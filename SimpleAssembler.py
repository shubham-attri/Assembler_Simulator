# # This is the code for question 1, here we are a given a input file 
# # with instructions and we have to convert that into binary codes for 
# # the machine to understand and handle the error accordingly
# # we are given with the  op code for the instructions and value for the registers
# #there are different types and we have to write the type accordinlgy

# from sys import stdin
# from decimal import Decimal

# def decimal_to_binary(n):#function to convert decimal value into binary
#     num1 = n
#     a = ""
#     while num1>0:
#         a = a + str(num1%2)
#         num1 = num1//2
#     for i in range(8- len(a)):
#         a = a + "0"
#     return a[::-1] #returns string of binary numbers
# # print(decimal_to_binary(12))



# #making a dictionary for the op codes 
# opcode ={
#     "add":"10000" ,
#     "sub": "10001" ,
#     # "mov":{"immediate":"10010","register":"10011"},#handelling the mov instruction because it have 2 condtions afterwards
#     # "mov":"10011",
#     "ld": "10100",
#     "st":"10101",
#     "mul":"10110",
#     "div":"10111",
#     "rs":"11000",
#     "ls":"11001",
#     "xor":"11010",
#     "or":"11011",
#     "and":"11100",
#     "not":"11101",
#     "cmp":"11110",
#     "jmp":"11111",
#     "jlt":"01100",
#     "jgt":"01101",
#     "je":"01111",
#     "hlt":"01010",
#     "movf":"00010"
# }


# #making a dictionary for register adresses
# register ={
#     "R0":"000",
#     "R1":"001",
#     'R2':"010",
#     "R3":"011",
#     "R4":"100",
#     "R5":"101",
#     "R6":"110",
#     "FLAGS":"111"
# }

# #defining the type according to which the output would be written
# typeA = ["add","sub","mul","xor","and","or","addf","subf"]
# typeB = ["mov immediate","rs","ls","movf"]
# typeC = ["mov register","div", "not","cmp"] # move value need to be handelled carefully
# typeD = ["ld","st"]
# typeE = ["jmp","jlt","jgt","je"]
# typeF = ["hlt"]
# types = [typeA,typeB,typeC,typeD,typeD,typeE,typeF] #to check which type the instruction belongs to


# # with open("input.txt","r+") as f:
# #     data = f.read().split("\n")  #opening the file and storing each line in data string format.
# # print(type(data))  
# # print(data[0])
# # print(len(data))
# data = []
# for line in stdin:
#     if(line=="" or line=="\n"):
#         continue
#     data.append(line)

# not_instructions =0 #a variable to count the number of non instruction lines so that the var lines comes after instruction codes

# def binary(n,m):
#     num=int(n)
#     binary=''
#     temp=bin(num)
#     temp=temp.replace('0b',"")
#     if m==1:
#         binary+='0'*(3-len(temp))
#     binary+=temp
#     return binary
# def decimal(n):
#     num=int(n)
#     binary=''
#     for i in range(10):
#         num=num*2
#         if str(num)[0]=="0":
#             return binary
#         if(str(num)[0]=="1"):
#             binary+="1"
#             num=int(str(num)[1:])
#         else:
#             binary+="0"
#     return binary
# def floattobin(n):
#     num=n
#     n=str(float(n))
#     leng=n.index('.')
#     result=''
#     temp=''
#     if float(n)%1!=0:
#         temp=[i for i in n.split('.')]
#         pow=len(binary(temp[0],0))-1
#         if(temp[0]!=0):
#             w=binary(temp[0],0)
#             result=binary(pow,1)+w[1:]+decimal(temp[1])
#         else:
#             result=binary(pow,1)+decimal(temp[1])
#     else:
#         num=num[:leng]
#         temp=binary(num,0)
#         c=0
#         pow=len(temp)-1
#         if temp[-1]=="0":
#             for i in range(len(temp)-1,0,-1):
#                 if temp[i]=="0" and temp[i-1]=="1":
#                     c=i
#                     break
#             temp=temp[:c]
#         result=binary(pow,1)+temp[1:]
#     if len(result)>=9:
#         print("Error The Given Immediate Value is out of bounds")
#         quit()
#     else:
#         result+="0"*(8-len(result))
#     return result
# # n=input()
# # print(floattobin(n))
# # print(type(floattobin(n)))   



# for i in range(len(data)):
#     if data[i][0:3] == "var" :#incremnting if the first word is not a instruction
#         not_instructions += 1
# # print(not_instructions)

# list =[] # making a list with each line and the words separated by a space.
# for i in range(len(data)):
#     list.append(data[i].split())
# # print(list)

# for i in range(not_instructions):
#     if (list[i][0] != "var"):
#         print("Error in line number: ", i + 1, "Not all variables defined in the beginning")
#         quit()

# # print("register value "+register[list[2][1]])

# line_data ="" #this is a string of data of the first instruction stored ina string with each instruction added to it with a \n char

# var_dict = {} #dictinary for variables
# label_dict = {}#dictionary for labels
# output = []
# # print(list[1][1] in register)
# # print(list)
# k=0
# for i in range(len(list)):
#     if list[i] == []:
#         continue
#     if list[i][0][-1] ==":"  :
#         label_dict[list[i][0][:-1]] = decimal_to_binary(i - not_instructions)
#     if(list[i][0] not in opcode and list[i][0] == "var"):
#         var_dict[list[i][1]] = decimal_to_binary(len(list)-not_instructions+k)
#         k+=1



# # print("var-",var_dict)
# # print("label ",label_dict)

# # print(label_dict)

# if (len(list[-1]) != 1 or list[-1][0] != "hlt") and (len(list[-1]) != 2 or list[-1][0][-1] != ":" or list[-1][1] != "hlt"):
#     print("Error: no hlt instruction")
#     quit()

# for i in range(len(list)):
#     # print(label_dict,"\n")
#     #handelling the error things at the start of the program
#     if (list[i] == []):
#         continue
#     for x in label_dict:
#         if x in var_dict:
#             print("Label name same as variable name in line number ",i+1)
#             quit()
    
#     if(list[i][0] not in opcode and list[i][0] !="var" and  list[i][1] not in opcode and list[i][0]!="var"):
#         if(list[i][0] != "mov" and list[i][1] != "mov" ):
#             print("Typo in instruction name in line number: ",i+1)
#             break

    

#     # instead of printing print all the instructions store them in list
#     if list[i][0] in opcode : #basic case with no move and label
#         # print(opcode[list[i][0]])
#         line_data += opcode[list[i][0]]+"\n"
        
        

#         if list[i][0] in typeA:
#             # print("type A "+list[i][0])
#             if (len(list[i]) != 4):
#                 print("Error in line number: ", i + 1, "\nGeneral Syntax Error")
#                 break

#             # if list[i][1] =="FLAGS" or list[i][2] =="FLAGS" or  list[i][3] =="FLAGS": # handelling the FLAGS error because it cannot be used in any other place but with move instruction
#             #     print("Illegal use of flags register in line number:  ",i+1)
#             #     break
#             for item in list:
#                 if item == "FLAGS":
#                     print("Illegal use of flags in line number: ",i+1)
#                     quit()

#             if list[i][1] not in register or list[i][2] not in register or list[i][3] not in register:  #printing error type accordingly and breaking the loop ie the program with the line number
#                 print("Typo in register name in line number: ",i+1)
#                 break
#             print(opcode[list[i][0]]+"00"+register[list[i][1]]+register[list[i][2]]+register[list[i][3]])
#             output.append(opcode[list[i][0]]+"00"+register[list[i][1]]+register[list[i][2]]+register[list[i][3]]) #appending to the output list to store the value
#         elif list[i][0] in typeB:
#             # print("type B "+list[i][0])
#             if (len(list[i]) != 3):
#                 print("Error in line number: ", i + 1, "\nGeneral Syntax Error")
#                 break
            
#             if list[i][0] == "movf":
#                 print(opcode[list[i][0]]+register[list[i][1]]+ floattobin(list[i][2][1:]))
#                 continue
            
#             elif list[i][2][1:].isdigit() ==False :
#                 print("invalid immediate value in line number: ",i+1)
#                 break
                
#             for item in list:
#                 if item == "FLAGS":
#                     print("Illegal use of flags in line number: ",i+1)
#                     quit()
#             # if list[i][1]=="FLAGS":
#             #     print("Illegal use of flags register in line number: ",i+1)
#             #     break
            
#             if list[i][1] not in register:
#                 print("Typo in register name in line number: ",i+1)
#                 break
            
#             # elif len(decimal_to_binary(int(list[i][2][1:]))) >8:
#             #     print("Illegal immediate value more than 8 bits, in line number: ",i+1)
#             #     break
#             if type(list[i][2][1:]) == str:
#                  print(opcode[list[i][0]]+register[list[i][1]]+decimal_to_binary(int(list[i][2][1:])))
#             # output.append(opcode[list[i][0]]+register[list[i][1]]+decimal_to_binary(int(list[i][2][1:])))

#         elif list[i][0] in typeC:
#             # print("type C "+list[i][0])
#             for item in list:
#                     if item == "FLAGS":
#                         print("Illegal use of flags in line number: ",i+1)
#                         quit()

#             if (len(list[i]) != 3):
#                 print("Error in line number: ", i + 1, "\nGeneral Syntax Error")
#                 break

#             # if list[i][1] =="FLAGS" or list[i][2]=="FLAGS":
#             #     print("Illegal use of FLAGSs register in line number: ",i+1)
#             #     break
#             if list[i][1] not in register or list[i][2] not in register:
#                 print("Typo in register name in line number: ",i+1)
#                 break
#             print(opcode[list[i][0]]+"00000"+register[list[i][1]]+register[list[i][2]])
#             output.append(opcode[list[i][0]]+"00000"+register[list[i][1]]+register[list[i][2]])

#         elif list[i][0] in typeD:
#             # print("type D "+list[i][0])
#             if (len(list[i]) != 3):
#                 print("Error in line number: ", i + 1, "\nGeneral Syntax Error")
#                 break
#             if list[i][1] not in register :
#                 print("Typo in register name in line number: ",i+1)
#                 break
#             # if register[list[i][2][:-1]] == "FLAGS":
#             #     print("Illegal use of flags in line number: ",i+1)
#             #     break

#             for item in list:
#                         if item == "FLAGS":
#                             print("Illegal use of flags in line number: ",i+1)
#                             quit()

#             if list[i][2] not in var_dict and list[i][2][:-1] not in label_dict :
#                 print("Variables not declared at the begining, Error in line number: ",i+1)
#                 break
#             if list[i][2] not in var_dict and list[i][2][:-1]  in label_dict :
#                 print("Misuse of label as variable in line number: ",i+1)
#                 break
#             print(opcode[list[i][0]]+register[list[i][1]]+var_dict[list[i][2]])
#             output.append(opcode[list[i][0]]+register[list[i][1]]+var_dict[list[i][2]])
#         elif list[i][0] in typeE:
#             # print("type E "+list[i][0])
#             if (len(list[i]) != 2):
#                 print("Error in line number: ", i + 1, "\nGeneral Syntax Error")
#                 break
#             if list[i][1] not in label_dict:
#                 print("Variables not declared at the begining, Error in line number: ",i+1)
#                 break
#             if list[i][1] not in label_dict:
#                 print("Misuse of label as variable in line number: ",i+1)
#                 break
#             print(opcode[list[i][0]]+"000"+label_dict[list[i][1]])
#             output.append(opcode[list[i][0]]+"000"+label_dict[list[i][1]])
#         elif list[i][0] in typeF:
#             # print("type F "+list[i][0])
#             if (len(list[i]) != 1):
#                 print("Error in line number: ", i + 1, "\nGeneral Syntax Error")
#                 break
#             if i < len(list)-1:
#                 for j in range(i + 1, len(list)):
#                     if (list[j] != []):
#                         print("hlt not being used as the last instruction, Error in line number: ",i+1)
#                         quit()
#             print(opcode[list[i][0]]+"00000000000")
#             output.append(opcode[list[i][0]]+"00000000000")
        
#         # if (list[len(list) - 1][0] != "hlt"):
#         #     print("Error: No hlt present")
#         #     break
    
#     if list[i][0] =="mov":  #mov instruction without the label

#         # if len(list[i] != 3 ):
#         #     print("Incomplete instruction and error in line number ",i+1)
#         #     break
        
#         if len(list[i]) <3:
#             print("Incomplete instruction in line number ",i+1)
#             break
#         if list[i][2][0] == "$":  #immediate value 
#             # print("10010")
#             if list[i][1]== "FLAGS":
#                 print("Illegal use of FLAGS register: ",i+1)
#                 break
#             if list[i][1] not in register:
#                 print("Typo in register name in line number: ",i+1)
#                 break
#             if list[i][2][1:].isdigit() ==False :
#                 print("invalid immediate value in line number: ",i+1)
#                 break
#             if int(list[i][2][1:]) >256 or int(list[i][2][1:]) < 0:
#                 print("Invalid immediate value in line number: ",i+1)
#                 break
#             line_data += "10010"+"\n"
#             print("10010"+register[list[i][1]]+decimal_to_binary(int(list[i][2][1:])))
#             output.append("10010"+register[list[i][1]]+decimal_to_binary(int(list[i][2][1:])))


#         elif list[i][2] in register: #register in instruction
#             # print("10011")
#             for item in list:
#                 if item == "FLAGS":
#                     print("Illegal use of flags in line number: ",i+1)
#                     quit()

#             # if register[list[i][2]] == "FLAGS" or register[list[i][1]]:
#             #     print("Illegal use of flags in line number: ",i+1)
#             #     break
#             if list[i][1] not in register or list[i][2] not in register:
#                 print("Typo in register name in line number: ",i+1)
#                 break
#             line_data += "10011"+"\n"
#             print("10011"+"00000" + register[list[i][1]]+register[list[i][2]])
#             output.append("10011"+ "00000" + register[list[i][1]]+register[list[i][2]])


            

#     # if(list[i][0] not in opcode and list[i][0] == "var"):
#     #     var_dict[list[i][1]] = decimal_to_binary(len(list)-not_instructions) # we have stored the values of the variable in a dictionary
#         # print(var_dict)
#         # print(label_dict)
    




#     if list[i][0][-1] ==":":#label cases
#         # label_dict[list[i][0][:-1]] = list[i][0][-1]

#         # print(label_dict)
#         if i != len(data) : # assuming hlt is only instruction with no label
#             if list[i][1] in opcode:
#                 # print(i)
#                 # print(opcode[list[i][1]])
#                 line_data += opcode[list[i][1]] +"\n"
#                 if list[i][1] in typeA:
#                     # print("type A "+list[i][1])

#                     if (len(list[i]) != 5):
#                         print("Error in line number: ", i + 1, "\nGeneral Syntax Error")
#                         break
                    
#                     for item in list:
#                         if item == "FLAGS":
#                             print("Illegal use of flags in line number: ",i+1)
#                             quit()

#                     if(list[i][2] not in register or list[i][3] not in register or list[i][4] not in register):
#                         print("Typo in register name in line number: ",i+1)
#                         break

#                     print(opcode[list[i][1]]+"00"+register[list[i][2]]+register[list[i][3]]+register[list[i][4]])
#                     output.append(opcode[list[i][1]]+"00"+register[list[i][2]]+register[list[i][3]]+register[list[i][4]])
#                     # label_dict[list[i][0][:-1]] = opcode[list[i][1]]+"00"+register[list[i][2]]+register[list[i][3]]+register[list[i][4]]
#                 elif list[i][1] in typeB:
#                     # print("type B "+list[i][1])
#                     if (len(list[i]) != 4):
#                         print("Error in line number: ", i + 1, "\nGeneral Syntax Error")
#                         break
                    
#                     if list[i][0] == "movf":
#                         print(opcode[list[i][1]]+register[list[i][2]]+ floattobin(list[i][3][1:]))

#                     elif list[i][2][1:].isdigit() ==False :
#                         print("invalid immediate value in line number: ",i+1)
#                         break
#                     for item in list:
#                         if item == "FLAGS":
#                             print("Illegal use of flags in line number: ",i+1)
#                             quit()

#                     if list[i][2] not in register:
#                         print("Typo in register name in line number: ",i+1)
#                         break
#                     if int(decimal_to_binary(int(list[i][3][1:]))) >8:
#                         print("Illegal immediate value more than 8 bits, in line number: ",i+1)
#                         break

#                     print(opcode[list[i][1]]+register[list[i][2]]+decimal_to_binary(int(list[i][3][1:])))
#                     output.append(opcode[list[i][1]]+register[list[i][2]]+decimal_to_binary(int(list[i][3][1:])))
#                     # label_dict[list[i][0][:-1]] = opcode[list[i][1]]+"00"+register[list[i][2]]+register[list[i][3]]+register[list[i][4]]
#                 elif list[i][1] in typeC:
#                     # print("type C "+list[i][1])
#                     if (len(list[i]) != 4):
#                         print("Error in line number: ", i + 1, "\nGeneral Syntax Error")
#                         break
                    
#                     for item in list:
#                         if item == "FLAGS":
#                             print("Illegal use of flags in line number: ",i+1)
#                             quit()

#                     if list[i][2] not in register or list[i][3] not in register:
#                         print("Typo in register name in line number: ",i+1)
#                         break

#                     print(opcode[list[i][1]]+"00000"+register[list[i][2]]+register[list[i][3]])
#                     output.append(opcode[list[i][1]]+"00000"+register[list[i][2]]+register[list[i][3]])
#                     # label_dict[list[i][0][:-1]] = opcode[list[i][1]]+"00"+register[list[i][2]]+register[list[i][3]]+register[list[i][4]]
#                 elif list[i][1] in typeD:
#                     # print("type D "+list[i][1])
#                     if (len(list[i]) != 4):
#                         print("Error in line number: ", i + 1, "\nGeneral Syntax Error")
#                         break
                    
#                     for item in list:
#                         if item == "FLAGS":
#                             print("Illegal use of flags in line number: ",i+1)
#                             quit()

#                     if list[i][2] not in register :
#                         print("Typo in register name in line number: ",i+1)
#                         break
#                     if list[i][3] not in var_dict and list[i][3][:-1] not in label_dict :
#                         print("Variables not declared at the begining, Error in line number: ",i+1)
#                         break
#                     if list[i][3] not in var_dict and list[i][3][:-1]  in label_dict :
#                         print("Misuse of label as variable in line number: ",i+1)
#                         break


#                     print(opcode[list[i][1]]+register[list[i][2]]+var_dict[list[i][3]])
#                     output.append(opcode[list[i][1]]+register[list[i][2]]+var_dict[list[i][3]])
#                     # label_dict[list[i][0][:-1]] = opcode[list[i][1]]+"00"+register[list[i][2]]+register[list[i][3]]+register[list[i][4]]
#                 elif list[i][1] in typeE:
#                     # print("type E "+list[i][1])
#                     if (len(list[i]) != 3):
#                         print("Error in line number: ", i + 1, "\nGeneral Syntax Error")
#                         break

#                     if list[i][2] not in label_dict:
#                         print("Variables not declared at the begining, Error in line number: ",i+1)
#                         break
#                     if list[i][2] in var_dict:
#                         print("Misuse of variable as label in line number: ",i+1)
#                         break

#                     print(opcode[list[i][1]]+"000"+label_dict[list[i][2]])
#                     output.append(opcode[list[i][1]]+"000"+label_dict[list[i][2]])
#                     # label_dict[list[i][0][:-1]] = opcode[list[i][1]]+"00"+register[list[i][2]]+register[list[i][3]]+register[list[i][4]]
#                 elif list[i][1] in typeF:
#                     # print("type F "+list[i][1])
#                     if (len(list[i]) != 2):
#                         print("Error in line number: ", i + 1, "\nGeneral Syntax Error")
#                         break
  

#                     if i < len(list)-1:
#                         for j in range(i + 1, len(list)):
#                             if (list[j] != []):
#                                 print("hlt not being used as the last instruction, Error in line number: ",i+1)
#                                 quit()

#                     print(opcode[list[i][1]]+"00000000000")
#                     output.append(opcode[list[i][1]]+"00000000000")
#                     # label_dict[list[i][0][:-1]] = opcode[list[i][1]]+"00"+register[list[i][2]]+register[list[i][3]]+register[list[i][4]]

#                 # if (list[len(list) - 1][1] != "hlt"):
#                 #     print("Error: No hlt present")
#                 #     break
                          

#             if list[i][1] =="mov":
#                 # print(i)
#                 if list[i][3][0] =="$":
#                     if list[i][2] not in register:
#                         print("Typo in register name in line number: ",i+1)
#                         # print("label mov immediate")
#                         # print(list[i][2] in register)
#                         break

#                     if register[list[i][2]] == "FLAGS":
#                         print("Illegal use of flag register: ",i)
#                         break
                    
#                     if list[i][2][1:].isdigit() ==False :
#                         print("invalid immediate value in line number: ",i+1)
#                         break
#                     if int(list[i][3][1:]) >256 or int(list[i][3][1:]) < 0:
#                         print("Invalid immediate value in line number: ",i+1)
#                         break

#                     line_data += "10010" +"\n"
#                     print("10010"+register[list[i][2]]+decimal_to_binary(int(list[i][3][1:])))
#                     output.append("10010"+register[list[i][2]]+decimal_to_binary(int(list[i][3][1:])))

#                 elif len(list[i])==4:
#                     # print("10011")

#                     if register[list[i][2]] not in register or register[list[i][3]] not in register:
#                         print("Typo in register name in line number: ",i+1)
#                         break
#                     for item in list:
#                         if item == "FLAGS":
#                             print("Illegal use of flags in line number: ",i+1)
#                             quit()
#                     line_data += "10011"+"\n"
#                     print("10011"+"00000" + register[list[i][2]]+register[list[i][3]])
#                     output.append("1001100000"+register[list[i][2]]+register[list[i][3]])

#                 # if list[i][0][:-1] in label_dict:
#                 #     print(label_dict[list[i][0][:-1]])

        
#         if i == len(data) :
#             if list[i][1] in opcode:
#                 print(list[i][1])
#                 line_data += list[i][1]+"\n"



# # print(line_data)

# line_d = line_data.split() #this stores the instruction value that we are finally going to print in the program
# # print(line_d)

# # print(output)

import sys
opcodes={"add":"10000","sub":"10001","mov":"10010",
        "mov2":"10011","ld":"10100","st":"10101",
        "mul":"10110","div":"10111","rs":"11000",
        "ls":"11001","xor":"11010","or":"11011",
        "and":"11100","not":"11101","cmp":"11110",
        "jmp":"11111","jlt":"01100","jgt":"01101",
        "je":"01111","hlt":"01010","addf":"00000",
        "subf":"00001","movf":"00010"}
registers={'R0': '000',
           'R1': '001',
           'R2': '010',
           'R3': '011',
           'R4': '100',
           'R5': '101',
           'R6': '110',
           'FLAGS': '111'
        }
typeA=["add","sub","mul","xor","or","and","addf","subf"]
typeB=["mov","rs","ls","movf"]
typeC=["mov2","div","not","cmp"]
typeD=["ld","st"]
typeE=["jmp","jlt","jgt","je"]
typeF=["hlt"]
memoryadd={}
var={}
labels={}
indata=[]
duplicates={}
def dectobin(n):
    return int(n,2)
def bintofloat(n):
    binary=''
    binary+='1'+n[3:]+"0"*100
    pow=n[:3]
    pow=dectobin(pow)
    temp=''
    temp=binary[:pow+1]+"."+binary[pow+1:]
    i=0
    k=0
    sum=0
    while(temp[i+1]!="."):
        i+=1
    for j in range(0,temp.index(".")):
        sum+=int(temp[j])*(2**i)
        k+=1
        i-=1
    i=1
    for j in range(temp.index(".")+1,len(temp)):
        sum+=int(temp[j])*(2**-i)
        i+=1
    return sum
def binary(n,m):
    num=int(n)
    binary=''
    temp=bin(num)
    temp=temp.replace('0b',"")
    if m==1:
        binary+='0'*(3-len(temp))
    binary+=temp
    return binary
def decimal(n):
    num=int(n)
    binary=''
    for i in range(10):
        num=num*2
        if str(num)[0]=="0":
            return binary
        if(str(num)[0]=="1"):
            binary+="1"
            num=int(str(num)[1:])
        else:
            binary+="0"
    return binary
def floattobin(n):
    num=n
    n=str(float(n))
    leng=n.index('.')
    result=''
    temp=''
    if float(n)%1!=0:
        temp=[i for i in n.split('.')]
        pow=len(binary(temp[0],0))-1
        if(temp[0]!=0):
            w=binary(temp[0],0)
            result=binary(pow,1)+w[1:]+decimal(temp[1])
        else:
            result=binary(pow,1)+decimal(temp[1])
    else:
        num=num[:leng]
        temp=binary(num,0)
        c=0
        pow=len(temp)-1
        if temp[-1]=="0":
            for i in range(len(temp)-1,0,-1):
                if temp[i]=="0" and temp[i-1]=="1":
                    c=i
                    break
            temp=temp[:c]
        result=binary(pow,1)+temp[1:]
    if len(result)>9:
        print("Error The Given Immediate Value is out of bounds")
        quit()
    else:
        result+="0"*(8-len(result))
    return result
def binarycovert(n):
        num=int(n)
        binary=''
        temp=bin(num)
        temp=temp.replace('0b',"")
        binary+='0'*(8-len(temp))
        binary+=temp
        return binary
def hltcheck(state):
        #to check the state of the hlt command
        count=0
        for i in range(len(state)):
                if 'hlt' in state[i]:
                        count+=1
                if count > 1:
                        print("Error at line",indata.index(state[i])+1,"hlt instruction has been typed more than once!")
                        quit()
        if count==0:
                print("No hlt command int the given instuctions!")
                quit()
        for i in range(len(state)):
                if ":" in state[i][0]:
                        if state[i][1]=="hlt" and i!=len(state)-1:
                                print("Error at line",indata.index(state[i])+1,"hlt instruction is not the last instruction")
                                quit()
                else:
                        if state[i][0]=="hlt" and i!=len(state)-1:
                                print("Error at line",indata.index(state[i])+1,"hlt instruction is not the last instruction")
                                quit()
def varcount(state):
        #to count the number of vairables 
        count=0
        for i in range(len(state)):
                if state[i][0]=='var':
                        count+=1
                else:
                        break
        return count
def varcheck(state):
        #to check if all the variables have been declared in the start
        flag=0
        for i in range(len(state)):
                if state[i][0]!='var':
                        flag=1
                if flag==1 and state[i][0]=='var':
                        print("Error at line",indata.index(state[i])+1,"variable has been declared in between instructions")
                        quit()
def memorydict(state):
        idx=0
        for i in range(len(state)):
                if state[i][0]== 'var':
                        pass
                else:
                     memoryadd[tuple(state[i])]=idx
                     idx+=1
        for i in range(varcount(state)):
                memoryadd[tuple(state[i])]=idx
                idx+=1
def addvar(memeryadd):
        for i in memeryadd:
                if i[0]=='var' and i[1] not in var.keys():
                        var[i[1]]=memoryadd[i]
def addlabel(memoryadd):
        for i in memoryadd:
                if ':' in i[0]:
                        labels[i[0]]=memoryadd[i]
def insttypocheck(state):
        for i in range(len(state)):
                if state[i][0]!="":
                        if ":" in state[i][0]:
                                if state[i][1] not in opcodes.keys() and state[i][1] !='var' or state[i][1]=='mov2':
                                        print("Typo detected in line",indata.index(state[i])+1,"kindly check the list of intructions.")
                                        quit()
                        else:
                                if state[i][0] not in opcodes.keys() and state[i][0] !='var' or state[i][0]=='mov2':
                                        print("Typo detected in line",indata.index(state[i])+1,"kindly check the list of intructions.")
                                        quit()
def varandregmixup(state):
        for i in range(len(state)):
                if state[i][0]!="":
                        if ":" in state[0]:
                                if state[i][1]=="var" and state[i][2] in registers.keys():
                                        print("Error at line",indata.index(state[i])+1,"Register Used as a Variable")
                                        quit()
                        else:
                                if state[i][0]=="var" and state[i][1] in registers.keys():
                                        print("Error at line",indata.index(state[i])+1,"Register Used as a Variable")
                                        quit()
def regtypocheck(state):
        for i in range(len(state)):
                if state[i][0]!="":
                        if ":" in state[i][0]:
                                if state[i][1] == 'mov' and "$" in state[i][3] and state[i][2] not in registers.keys():
                                        print("Error at line",indata.index(state[i])+1,"Kindly check the Register")
                                        quit()
                                elif state[i][1] == 'mov' and "$" not in state[i][3] and state[i][2] not in registers.keys():
                                        print("Error at line",indata.index(state[i])+1,"Kindly check the Register")
                                        quit()
                                elif state[i][1] in typeA and (state[i][2] not in registers.keys() or state[i][3] not in registers.keys() or state[i][4] not in registers.keys()):
                                        print("Error at line",indata.index(state[i])+1,"Kindly check the Register")
                                        quit()
                                elif state[i][1] in typeB and state[i][2] not in registers.keys():
                                        print("Error at line",indata.index(state[i])+1,"Kindly check the Register")
                                        quit()
                                elif state[i][1] in typeC and (state[i][2] not in registers.keys() or state[i][3] not in registers.keys()):
                                        print("Error at line",indata.index(state[i])+1,"Kindly check the Register")
                                        quit()
                                elif state[i][1] in typeD and state[i][2] not in registers.keys():
                                        print("Error at line",indata.index(state[i])+1,"Kindly check the Register")
                                        quit()
                        else:   
                                if state[i][0] == 'mov' and "$" in state[i][2] and state[i][1] not in registers.keys():
                                        print("Error at line",indata.index(state[i])+1,"Kindly check the Register")
                                        quit()
                                elif state[i][0] == 'mov' and "$" not in state[i][2] and state[i][1] not in registers.keys():
                                        print("Error at line",indata.index(state[i])+1,"Kindly check the Register")
                                        quit()
                                elif state[i][0] in typeA and (state[i][1] not in registers.keys() or state[i][2] not in registers.keys() or state[i][3] not in registers.keys()):           
                                        print("Error at line",indata.index(state[i])+1,"Kindly check the Register")
                                        quit()
                                elif state[i][0] in typeB and state[i][1] not in registers.keys():
                                        print("Error at line",indata.index(state[i])+1,"Kindly check the Register")
                                        quit()
                                elif state[i][0] in typeC and (state[i][1] not in registers.keys() or state[i][2] not in registers.keys()):
                                        print("Error at line",indata.index(state[i])+1,"Kindly check the Register")
                                        quit()
                                elif state[i][0] in typeD and state[i][1] not in registers.keys():
                                        print("Error at line",indata.index(state[i])+1,"Kindly check the Register")
                                        quit()
def defvar(state):
        for i in range(len(state)):
                if state[i][0]!='':
                        if ":" not in state[i][0]:
                                if state[i][0] in typeD and (state[i][2] not in var.keys()and state[i][2]+":" not in labels.keys()):
                                        print("Error at line",indata.index(state[i])+1,"Use of undefined variable.")
                                        quit()
                        else:
                                if state[i][1] in typeD and (state[i][3] not in var.keys() and state[i][3]+":" not in labels.keys()):
                                        print("Error at line",indata.index(state[i])+1,"Use of undefined variable.")
                                        quit()
def labelcheck(state):
        for i in range(len(state)):
                if state[i][0]!="":
                        if ":" in state[i][0]:
                                if state[i][1] in typeE and state[i][2]+":" not in labels.keys() and state[i][2] not in var.keys():
                                        print("Error at line",indata.index(state[i])+1,"USe of undefined label.")
                                        quit()
                        else:
                                if state[i][0] in typeE and state[i][1]+":" not in labels.keys() and state[i][1] not in var.keys():
                                        print("Error at line",indata.index(state[i])+1,"Use of undefined label.")
                                        quit()
def flagcheck(state):
        for i in range(len(state)):
                if state[i][0]!="":
                        if ":" in state[i][0]:
                                if (state[i][1]=="mov" and "$" in state[i][3]) and state[i][2]=="FLAGS":
                                        print("Error at line",indata.index(state[i])+1,"Illegal use of flag registers")
                                        quit()
                                elif (state[i][1]=="mov" and "$"  not in state[i][3]) and state[i][3]=="FLAGS":
                                        print("Error at line",indata.index(state[i])+1,"Illegal use of flag registers")
                                        quit()
                                elif state[i][1] in typeA and "FLAGS" in state[i] :
                                        print("Error at line",indata.index(state[i])+1,"Illegal use of flag registers")
                                        quit()
                                elif state[i][1] in typeB and state[i][2]=="FLAGS" and state[i][1]!='mov':
                                        print("Error at line",indata.index(state[i])+1,"Illegal use of flag registers")
                                        quit()
                                elif state[i][1] in typeC and (state[i][2]=="FLAGS" or state[i][3]=="FLAGS") and state[i][1]!='mov':
                                        print("Error at line",indata.index(state[i])+1,"Illegal use of flag registers")
                                        quit()
                                elif state[i][1] in typeD and state[i][2]=="FLAGS":
                                        print("Error at line",indata.index(state[i])+1,"Illegal use of flag registers")
                                        quit()
                        else: 
                                if (state[i][0]=="mov" and "$" in state[i][2]) and state[i][1]=="FLAGS":
                                        print("Error at line",indata.index(state[i])+1,"Illegal use of flag registers")
                                        quit()
                                elif (state[i][0]=="mov" and "$"  not in state[i][2]) and  state[i][2]=="FLAGS":
                                        print("Error at line",indata.index(state[i])+1,"Illegal use of flag registers")
                                        quit()
                                elif state[i][0] in typeA and "FLAGS" in state[i]:
                                        print("Error at line",indata.index(state[i])+1,"Illegal use of flag registers")
                                        quit()
                                elif state[i][0] in typeB and state[i][1]=="FLAGS" and state[i][0]!='mov':
                                        print("Error at line",indata.index(state[i])+1,"Illegal use of flag registers")
                                        quit()
                                elif state[i][0] in typeC and (state[i][1]=="FLAGS" or state[i][2]=="FLAGS") and state[i][1]!='mov':
                                        print("Error at line",indata.index(state[i])+1,"Illegal use of flag registers")
                                        quit()
                                elif state[i][0] in typeD and state[i][1]=="FLAGS":
                                        print("Error at line",indata.index(state[i])+1,"Illegal use of flag registers")
                                        quit()
def immvalue(state):
        for i in range(len(state)):
                if state[i][0]!="":
                        if ":" in state[i][0]:
                                if state[i][1] in typeB and "$" in state[i][3] and state[i][1]!="movf"  and (float(state[i][3][1:])<0 or float(state[i][3][1:])>255 or float(state[i][3][1:])%1!=0 or state[i][3][1:].isalpha()):
                                        print("Error at line",indata.index(state[i])+1,"Illegal Immediate Value.")
                                        quit()
                        else:
                                if state[i][0] in typeB and "$" in state[i][2] and state[i][0]!="movf"  and (float(state[i][2][1:])<0 or float(state[i][2][1:])>255 or float(state[i][2][1:])%1!=0 or state[i][2][1:].isalpha()):
                                        print("Error at line",indata.index(state[i])+1,"Illegal Immediate Value.")
                                        quit()
def instsyntax(state):
        for i in range(len(state)):
                if state[i][0]!="":
                        if ":" in state[i][0]:
                                if state[i][1]=="mov" and len(state[i])!=4:
                                        print("Error at line",indata.index(state[i])+1,":Syntax Error")
                                        quit()
                                elif (state[i][1]=="mov" and "$"  not in state[i][3]) and len(state[i])!=4:
                                        print("Error at line",indata.index(state[i])+1,":Syntax Error")
                                        quit()
                                elif state[i][1] in typeA and len(state[i])!=5:
                                        print("Error at line",indata.index(state[i])+1,":Syntax Error")
                                        quit()
                                elif state[i][1] in typeB and len(state[i])!=4:
                                        print("Error at line",indata.index(state[i])+1,":Syntax Error1")
                                        quit()
                                elif state[i][1] in typeC and len(state[i])!=4:
                                        print("Error at line",indata.index(state[i])+1,":Syntax Error")
                                        quit()
                                elif state[i][1] in typeD and len(state[i])!=4:
                                        print("Error at line",indata.index(state[i])+1,":Syntax Error")
                                        quit()
                                elif state[i][1] in typeE and len(state[i])!=3:
                                        print("Error at line",indata.index(state[i])+1,":Syntax Error")
                                        quit()
                                elif state[i][1] in typeF and len(state[i])!=2:
                                        print("Error at line",indata.index(state[i])+1,":Syntax Error")
                                        quit()
                        else: 
                                if state[i][0]=="mov" and len(state[i])!=3:
                                        print("Error at line",indata.index(state[i])+1,":Syntax Error")
                                        quit()
                                elif (state[i][0]=="mov" and "$"  not in state[i][2]) and len(state[i])!=3:
                                        print("Error at line",indata.index(state[i])+1,":Syntax Error")
                                        quit()
                                elif state[i][0] in typeA and len(state[i])!=4:
                                        print("Error at line",indata.index(state[i])+1,":Syntax Error")
                                        quit()
                                elif state[i][0] in typeB and len(state[i])!=3:
                                        print("Error at line",indata.index(state[i])+1,":Syntax Error")
                                        quit()
                                elif state[i][0] in typeC and len(state[i])!=3:
                                        print("Error at line",indata.index(state[i])+1,":Syntax Error")
                                        quit()
                                elif state[i][0] in typeD and len(state[i])!=3:
                                        print("Error at line",indata.index(state[i])+1,":Syntax Error")
                                        quit()
                                elif state[i][0] in typeE and len(state[i])!=2:
                                        print("Error at line",indata.index(state[i])+1,":Syntax Error")
                                        quit()
                                elif state[i][0] in typeF and len(state[i])!=1:
                                        print("Error at line",indata.index(state[i])+1,":Syntax Error")
                                        quit()
def emptylabel(state):
        for i in range(len(state)):
                if ":" in state[i][0] and len(state[i])==1:
                        print("Error at line",indata.index(state[i])+1,"Empty Label.")
def duplicatevar(state):
        for i in range(len(state)):
                if state[i][0]=='var':
                        if state[i][1] not in duplicates.keys():
                                duplicates[state[i][1]]=1
                        else:
                                duplicates[state[i][1]]+=1
                        if duplicates[state[i][1]] > 1:
                                print("Error at line",indata.index(state[i])+1,"Same variable defined twice.")
                                quit()
def labelinlabel(state):
        for i in range(len(state)):
                if ":" in state[i][0] and ":" in state[i][1]:
                        print("Error at line",indata.index(state[i])+1,"Nested Labels not allowed")

def output(inst):
        if ':' in inst[0]:
                if inst[1] == 'mov' :
                        if "$" in inst[3]:
                                print(opcodes['mov']+registers[inst[2]]+binarycovert(inst[3][1:]))
                        else: 
                                print(opcodes['mov2']+'0'*5+registers[inst[2]]+registers[inst[3]])
                elif inst[1] in typeA:
                        print(opcodes[inst[1]]+'0'*2+registers[inst[2]]+registers[inst[3]]+registers[inst[4]])
                elif inst[1] in typeB and inst[1]!="movf":
                        print(opcodes[inst[1]]+registers[inst[2]]+binarycovert(inst[3][1:]))
                elif inst[1] in typeC:
                        print(opcodes[inst[1]]+'0'*5+registers[inst[2]]+registers[inst[3]])
                elif inst[1] in typeD:
                        print(opcodes[inst[1]]+registers[inst[2]]+binarycovert(var[inst[3]]))
                elif inst[1] in typeE:
                        print(opcodes[inst[1]]+'0'*3+binarycovert(labels[inst[2]+":"]))
                elif inst[1] in typeF:
                        print(opcodes[inst[1]]+'0'*11)
                elif inst[1]=="movf":
                        print(opcodes['movf']+registers[inst[2]]+floattobin(inst[3][1:]))
        else: 
                if inst[0] == 'mov' :
                        if "$" in inst[2]:
                                print(opcodes['mov']+registers[inst[1]]+binarycovert(inst[2][1:]))
                        else: 
                                print(opcodes['mov2']+'0'*5+registers[inst[1]]+registers[inst[2]])
                elif inst[0] in typeA:
                        print(opcodes[inst[0]]+'0'*2+registers[inst[1]]+registers[inst[2]]+registers[inst[3]])
                elif inst[0] in typeB and inst[0]!="movf":
                        print(opcodes[inst[0]]+registers[inst[1]]+binarycovert(inst[2][1:]))
                elif inst[0] in typeC:
                        print(opcodes[inst[0]]+'0'*5+registers[inst[1]]+registers[inst[2]])
                elif inst[0] in typeD:
                        print(opcodes[inst[0]]+registers[inst[1]]+binarycovert(var[inst[2]]))
                elif inst[0] in typeE:
                        print(opcodes[inst[0]]+'0'*3+binarycovert(labels[inst[1]+":"]))
                elif inst[0] in typeF:
                        print(opcodes[inst[0]]+'0'*11)
                elif inst[0]=="movf":
                        print(opcodes['movf']+registers[inst[1]]+floattobin(inst[2][1:]))
def labelsandvar(state):
        for i in range(len(state)):
                if state[i][0]!='':
                        if ":" not in state[i][0]:
                                if state[i][0] in typeD and (state[i][2] not in var.keys() and state[i][2]+":" in labels.keys()):
                                        print("Error at line",indata.index(state[i])+1,"Label has been used a variable.")
                                        quit()
                                if state[i][0] in typeE and (state[i][1] in var.keys() and state[i][1]+":" not in labels.keys()):
                                        print("Error at line",indata.index(state[i])+1,"Variable has been used a label.")
                                        quit()
                        else:
                                if state[i][1] in typeD and (state[i][3] not in var.keys() and state[i][3]+":" in labels.keys()):
                                        print("Error at line",indata.index(state[i])+1,"Label has been used a variable.")
                                        quit()
                                if state[i][1] in typeE and (state[i][2] in var.keys() and state[i][2]+":" not in labels.keys()):
                                        print("Error at line",indata.index(state[i])+1,"Variable has been used a label.")
                                        quit()
def floatcheck(state):
         for i in range(len(state)):
                if state[i][0]!='':
                        if ":" not in state[i][0]:
                                if state[i][0]=="movf" and ("." not in state[i][2] or float(state[i][2][1:])<1):
                                        print("Error at line",indata.index(state[i])+1,"Illegal Float value.")
                                        quit()
                        else:
                                if state[i][1]=="movf" and ("." not in state[i][3] or float(state[i][3][1:])<1):
                                        print("Error at line",indata.index(state[i])+1,"Illegal Float Value.")
                                        quit()
def main():
        for line in sys.stdin:
                if ''==line:
                        break
                indata.append((line.strip()).split())
        data=[i for i in indata if i !=[]]
        memorydict(data)
        addvar(memoryadd)
        addlabel(memoryadd)
        hltcheck(data)
        varcheck(data)
        labelinlabel(data)
        duplicatevar(data)
        emptylabel(data)
        instsyntax(data)
        insttypocheck(data)
        defvar(data)
        flagcheck(data)
        immvalue(data)
        labelsandvar(data)
        varandregmixup(data)
        regtypocheck(data)
        floatcheck(data)
        labelcheck(data)
        for i in data:
                output(i)
if __name__=="__main__":
        main()
