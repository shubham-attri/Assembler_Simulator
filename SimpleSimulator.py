import sys
import matplotlib.pyplot as plt
R0 = R1 = R2 = R3 = R4 = R5 = R6 = FLAGS = "0000000000000000"
PC = 0
newPC = 0
mlist=[1.0, 1.03125, 1.0625, 1.09375, 1.125, 1.15625, 1.1875, 1.21875, 1.25, 1.28125, 1.3125, 1.34375, 1.375, 1.40625, 1.4375, 1.46875, 1.5, 1.53125, 1.5625, 1.59375, 1.625, 1.65625, 1.6875, 1.71875, 1.75, 1.78125, 1.8125, 1.84375, 1.875, 1.90625, 1.9375, 1.96875, 2.0, 2.0625, 2.125, 2.1875, 2.25, 2.3125, 2.375, 2.4375, 2.5, 2.5625, 2.625, 2.6875, 2.75, 2.8125, 2.875, 2.9375, 3.0, 3.0625, 3.125, 3.1875, 3.25, 3.3125, 3.375, 3.4375, 3.5, 3.5625, 3.625, 3.6875, 3.75, 3.8125, 3.875, 3.9375, 4.0, 4.125, 4.25, 4.375, 4.5, 4.625, 4.75, 4.875, 5.0, 5.125, 5.25, 5.375, 5.5, 5.625, 5.75, 5.875, 6.0, 6.125, 6.25, 6.375, 6.5, 6.625, 6.75, 6.875, 7.0, 7.125, 7.25, 7.375, 7.5, 7.625, 7.75, 7.875, 8.0, 8.25, 8.5, 8.75, 9.0, 9.25, 9.5, 9.75, 10.0, 10.25, 10.5, 10.75, 11.0, 11.25, 11.5, 11.75, 12.0, 12.25, 12.5, 12.75, 13.0, 13.25, 13.5, 13.75, 14.0, 14.25, 14.5, 14.75, 15.0, 15.25, 15.5, 15.75, 16.0, 16.5, 17.0, 17.5, 18.0, 18.5, 19.0, 19.5, 20.0, 20.5, 21.0, 21.5, 22.0, 22.5, 23.0, 23.5, 24.0, 24.5, 25.0, 25.5, 26.0, 26.5, 27.0, 27.5, 28.0, 28.5, 29.0, 29.5, 30.0, 30.5, 31.0, 31.5, 32.0, 33.0, 34.0, 35.0, 36.0, 37.0, 38.0, 39.0, 40.0, 41.0, 42.0, 43.0, 44.0, 45.0, 46.0, 47.0, 48.0, 49.0, 50.0, 51.0, 52.0, 53.0, 54.0, 55.0, 56.0, 57.0, 58.0, 59.0, 60.0, 61.0, 62.0, 63.0, 64.0, 66.0, 68.0, 70.0, 72.0, 74.0, 76.0, 78.0, 80.0, 82.0, 84.0, 86.0, 88.0, 90.0, 92.0, 94.0, 96.0, 98.0, 100.0, 102.0, 104.0, 106.0, 108.0, 110.0, 112.0, 114.0, 116.0, 118.0, 120.0, 122.0, 124.0, 126.0, 128.0, 132.0, 136.0, 140.0, 144.0, 148.0, 152.0, 156.0, 160.0, 164.0, 168.0, 172.0, 176.0, 180.0, 184.0, 188.0, 192.0, 196.0, 200.0, 204.0, 208.0, 212.0, 216.0, 220.0, 224.0, 228.0, 232.0, 236.0, 240.0, 244.0, 248.0, 252.0]

registers = {
    "000": R0,
    "001": R1,
    "010": R2,
    "011": R3,
    "100": R4,
    "101": R5,
    "110": R6,
    "111": FLAGS
}


def binToDec(binary):
    binary = int(binary)
    decimal = i = 0
    while (binary != 0):
        # print((binary))
        dec = binary % 10
        decimal = decimal + dec * (2 ** i)
        binary = binary // 10
        i += 1
    return decimal


def dtob(dec):
    s = ""
    while (dec > 0):
        s = (str)(dec % 2) + s
        dec = dec // 2
    if (len(s) < 16):
        s = (16 - len(s)) * "0" + s
    return s


def fdtob(dec):
    s = ""
    while (dec > 0):
        s = (str)(dec % 2) + s
        dec = dec // 2
    if (len(s) < 16):
        s = (16 - len(s)) * "0" + s
    return s

def binToDec(binary):
    binary=int(binary)
    decimal = i = 0
    while (binary != 0):
        dec = binary % 10
        decimal = decimal + dec * (2 ** i)
        binary = binary // 10
        i += 1
    return decimal

def floattob(dec):
    final=""
    for i in range(5):
        dec=float("0."+str(dec))
        # dec=float(dec)
        dec=dec*2
        final=final+str(dec)[0]
        dec=str(dec)[2:]
    return final

def btofloat(binary):
    decimal = 0
    i=1
    while ((binary) != 0):
        try:
            dec=int(str(binary)[0])
        except:
            return decimal
        decimal = decimal + dec * (0.5 ** i)
        i += 1
        try:
            binary = binary[1:]
        except:
            return decimal    
    return decimal    

def exponent(num):
    num=int(num.split(".")[0])
    l=fdtob(num)
    for i in range(len(l)):
        if l[i]=="1":
            break
    expo=len(l[i:])-1
    return [fdtob(expo)[-8:],l[i:]]

def floatingpoint(num):
    num=str(num)
    dec=(num.split(".")[1])
    expo,mane=exponent(num)
    dec=floattob(dec)
    # print("floattob",dec)
    return str(expo)[-3:]+(str(mane[1:])+str(dec))[:5]
    
def floattodecimal(num):
    expo=num[:3]
    mane=num[3:]
    i=binToDec(expo)
    if i<5:
        dexpo=(binToDec("1"+mane[:i]))
        dmane=(btofloat(mane[i:]+"0"*(5-i)))
    else:
        dexpo=(binToDec("1"+mane+"0"*(i-5)))
        dmane=0
    return ((float(dexpo)+float(dmane)))


def add(inst):
    global newPC
    newPC += 1
    registers[inst[13:16]] = dtob(binToDec(int(registers[inst[10:13]])) + binToDec(int(registers[inst[7:10]])))
    
    if binToDec(int(registers[inst[13:16]])) > 65535:
        registers["111"] = "0000000000001000"
        # registers[inst[13:16]] = "1" * 16
        registers[inst[13:16]] = registers[inst[13:16]][-16:]
    else:
        registers["111"] = "0" * 16

def addf(inst):
    global newPC
    newPC += 1
    num = (floattodecimal((registers[inst[10:13]][8:])) + floattodecimal((registers[inst[7:10]][8:])))
    # print("..",floattodecimal(registers[inst[10:13]]),floattodecimal(registers[inst[7:10]]))
    if num not in mlist:
    # if binToDec(int(registers[inst[13:16]])) > 65535:
        registers["111"] = "0000000000001000"
        registers[inst[13:16]] = "1" * 16
    else:
        registers["111"] = "0" * 16
        registers[inst[13:16]] = "00000000"+floatingpoint(str(num))


def sub(inst):
    global newPC
    newPC += 1
    # print("sub",binToDec(int(registers[inst[7:10]])), binToDec(int(registers[inst[10:13]])))
    registers[inst[13:16]] =  dtob(binToDec(int(registers[inst[7:10]])) - (binToDec(int(registers[inst[10:13]]))))
    if (binToDec(int(registers[inst[7:10]])) - (binToDec(int(registers[inst[10:13]])))) < 0:
        registers["111"] = "0000000000001000"
        registers[inst[13:16]] = "0" * 16
    else:
        registers["111"] = "0" * 16


def subf(inst):
    global newPC
    newPC += 1
    # registers[inst[13:16]] =  dtob(floattodecimal((registers[inst[7:10]])) - (floattodecimal((registers[inst[10:13]]))))
    num =  (floattodecimal((registers[inst[7:10]][8:])) - (floattodecimal((registers[inst[10:13]][8:]))))
    # if binToDec(int(registers[inst[13:16]])) < 0:
    #     registers["111"] = "0000000000001000"
    #     registers[inst[13:16]] = "0" * 16
    # else:
    #     registers["111"] = "0" * 16
    if num not in mlist:
        registers["111"] = "0000000000001000"
        registers[inst[13:16]] = "1" * 16
    if num < 0:
    # if binToDec(int(registers[inst[13:16]])) > 65535:
        registers["111"] = "0000000000001000"
        registers[inst[13:16]] = "0" * 16
    else:
        registers["111"] = "0" * 16
        registers[inst[13:16]] = "00000000"+floatingpoint(str(num))

def mul(inst):
    global newPC
    newPC += 1
    # print("mul",binToDec(int(registers[inst[10:13]])), binToDec(int(registers[inst[7:10]])))
    registers[inst[13:16]] = dtob(binToDec(int(registers[inst[10:13]])) * binToDec(int(registers[inst[7:10]])))
    if binToDec(int(registers[inst[13:16]])) > 65535:
        registers["111"] = "0000000000001000"
        registers[inst[13:16]] = registers[inst[13:16]][-16:]
    elif binToDec(int(registers[inst[13:16]])) < 0:
        registers["111"] = "0000000000001000"
        registers[inst[13:16]] = "0" * 16
    else:
        registers["111"] = "0" * 16


def xor(inst):
    global newPC
    newPC += 1
    registers[inst[13:16]] = dtob(binToDec(int(registers[inst[10:13]])) ^ binToDec(int(registers[inst[7:10]])))
    registers["111"] = "0" * 16


def or1(inst):
    global newPC
    newPC += 1
    registers[inst[13:16]] = dtob(binToDec(int(registers[inst[10:13]])) | binToDec(int(registers[inst[7:10]])))
    registers["111"] = "0" * 16


def and1(inst):
    global newPC
    newPC += 1
    
    registers[inst[13:16]] = dtob(binToDec(int(registers[inst[10:13]])) & binToDec(int(registers[inst[7:10]])))
    registers["111"] = "0" * 16
    


def movr(inst):
    global newPC
    newPC += 1
    registers[inst[13:16]] = registers[inst[10:13]]
    registers["111"] = "0" * 16


def div(inst):
    global newPC
    newPC += 1
    registers["000"] = dtob(binToDec(int(registers[inst[10:13]])) // binToDec(int(registers[inst[13:16]])))
    registers["001"] = dtob(binToDec(int(registers[inst[10:13]])) % binToDec(int(registers[inst[13:16]])))
    registers["111"] = "0" * 16


def not1(inst):
    global newPC
    newPC += 1
    newstr=''
    for i in str((registers[inst[10:13]])):
        if i=='1':
            newstr+="0"
        else:
            newstr+="1"
    registers[inst[13:16]] = newstr
    registers["111"] = "0" * 16

def cmp1(inst):
    global newPC
    newPC += 1
    if ((binToDec(int(registers[inst[10:13]]))) > binToDec(int(registers[inst[13:16]]))):
        registers["111"] = "0000000000000010"
    elif ((binToDec(int(registers[inst[10:13]]))) == binToDec(int(registers[inst[13:16]]))):
        # print(binToDec(int(registers[inst[10:13]])),binToDec(int(registers[inst[13:16]])))
        registers["111"] = "0000000000000001"
    elif ((binToDec(int(registers[inst[10:13]]))) < binToDec(int(registers[inst[13:16]]))):
        # print(binToDec(int(registers[inst[10:13]])),binToDec(int(registers[inst[13:16]])))
        registers["111"] = "0000000000000100"


def movi(inst):
    global newPC
    newPC += 1
    registers[inst[5:8]] = dtob(binToDec(inst[8:]))
    registers["111"] = "0" * 16

def movf(inst):
    global newPC
    newPC += 1
    registers[inst[5:8]] = "00000000"+floatingpoint(floattodecimal(inst[8:]))
    registers["111"] = "0" * 16

def ls(inst):
    global newPC
    newPC += 1
    registers["111"] = "0" * 16
    registers[inst[5:8]] = dtob((binToDec(registers[inst[5:8]])) * 2 ** binToDec(inst[8:]))


def rs(inst):
    global newPC
    newPC += 1
    registers["111"] = "0" * 16
    registers[inst[5:8]] = dtob((binToDec(registers[inst[5:8]])) // 2 ** binToDec(inst[8:]))


def ld(inst):
    global newPC
    newPC += 1
    registers[inst[5:8]] = mem[binToDec(inst[8:])]
    registers["111"] = "0" * 16


def st(inst):
    global newPC
    newPC += 1
    mem[binToDec(inst[8:])] = registers[inst[5:8]]
    registers["111"] = "0" * 16


def jmp(inst):
    global newPC
    newPC = binToDec(inst[8:])
    registers["111"] = "0" * 16


def jgt(inst):
    global newPC
    if (registers["111"] == "0000000000000010"):
        newPC = binToDec(inst[8:])
    else:
        newPC+=1
    registers["111"] = "0" * 16


def jlt(inst):
    global newPC
    # print("heello",newPC)
    if (registers["111"] == "0000000000000100"):
        newPC = binToDec(inst[8:])
    else:
        newPC+=1
    registers["111"] = "0" * 16
    # print(newPC)
    # exit()

def je(inst):
    global newPC
    if (registers["111"] == "0000000000000001"):
        newPC = binToDec(inst[8:])
    else:
        newPC+=1
    registers["111"] = "0" * 16


A = {
    "10000": add,
    "10001": sub,
    "10110": mul,
    "11010": xor,
    "11011": or1,
    "11100": and1,
    "00000": addf,
    "00001": subf,
}
B = {
    "10010": movi,
    "11001": ls,
    "11000": rs,
    "00010": movf,

}
F = {
    "01010": "hlt"
}

C = {
    "10011": movr,
    "10111": div,
    "11101": not1,
    "11110": cmp1
}

D = {
    "10100": ld,
    "10101": st,
}

E = {
    "11111": jmp,
    "01100": jlt,
    "01101": jgt,
    "01111": je,
}


def execute(inst):
    # 
    # (type(inst))
    if (inst[:5] in A):
        A[inst[:5]](inst)
    if (inst[:5] in B):
        B[inst[:5]](inst)
    if (inst[:5] in C):
        C[inst[:5]](inst)
    if (inst[:5] in D):
        D[inst[:5]](inst)
    if (inst[:5] in E):
        E[inst[:5]](inst)


with open("test.txt", "w") as w:
    pass

instruction_list = []

for line in sys.stdin:
    if line == '' or line == '\n':
        break
    instruction_list.append(line.strip())

mem = instruction_list
l = len(instruction_list)
while (l < 256):
    mem.append("0" * 16)
    l += 1


def regprint():
    print(registers["000"], registers["001"], registers["010"], registers["011"], registers["100"], registers["101"],
          registers["110"], registers["111"], sep=" ")


def memdump():
    for i in mem:
        with open("test.txt", "a") as w:
            w.write(i)
            w.write("\n")
        print(i)


def dtob2(dec):
    s = ""
    while (dec > 0):
        s = (str)(dec % 2) + s
        dec = dec // 2
    if (len(s) < 8):
        s = (8 - len(s)) * "0" + s
    return s
y=[0]
x=[]
halt_flag = 0
while (halt_flag == 0):
    if PC>255:
        exit()
# for ijk in range(0,50):
    instruction = mem[PC]
    if (instruction[:5] == "01010"):
        halt_flag = 1
    execute(instruction)
    if(instruction[:5] in D):
        y.append(-binToDec(instruction[8:]))
    print(dtob2(PC), end=" ")
    PC = newPC
    y.append(PC)
    # print(newPC)
    regprint()
n=len(y)
for i in range(n):
    if y[i]<0:
        x.append(x[i-1])
    else:
        x.append(i)

memdump()

# print(len(x),len(y))


for i in range(len(y)):
    if(y[i]<0):
        y[i]*=(-1)
plt.scatter(x, y, c ="blue")
plt.show()