
fo = open('sec1.txt','r')
sec = []
for i in fo:
    sec.append(i[:-1])
fo.close()
f = open('Section1_14_01_2022.txt',encoding='utf-8')
data = []
print("Example input")
print("Sec 1 : 10")
print("Sec 2 : 13")
print("Sec 3 : 15")
time_class = input("Enter Class Time Start : ")
if time_class == "10":
    print("-------------\nSEC 1\n-------------")
elif time_class =="13":
    print("-------------\nSEC 2\n-------------")
elif time_class =="15":
    print("-------------\nSEC 3\n-------------")
line = f.readline()
line2 = f.readline()
time_check = []

time = line.split()
time_check = time[0].split(":")
time_check_2 = int(time_check[0])-1
if time_check_2 ==8:
    code = line2.split()
    if code[0] in sec:
        print("PRESENT :",time[0],code[0])
        data.append(code[0])
if time_check[0] == str(int(time_class)-1):
    code = line2.split()
    if code[0] in sec:
        print("PRESENT :",time[0],code[0])
        data.append(code[0])
if time_check[0] == time_class:
    time_check = time[0].split(":")
    if int(time_check[1])<=10:
        code = line2.split()
        if code[0] in sec:
            print("PRESENT :",time[0],code[0])
            data.append(code[0])
               
    if int(time_check[1])>10:
        code = line2.split()
        if code[0] in sec:
            print("LATE :",time[0],code[0])
            data.append(code[0])
time_check = []
while line:
    #print(line)
    #print(line2)
    
    line = f.readline()
    line2 = f.readline()
    if line2 != "":
        time = line.split()
        time_check = time[0].split(":")
        time_check_2 = int(time_check[0])-1
        if time_check_2 ==8:
            code = line2.split()
            if code[0] in sec:
                print("PRESENT :",time[0],code[0])
                data.append(code[0])
        if time_check[0] == str(int(time_class)-1):
            code = line2.split()
            if code[0] in sec:
                print("PRESENT :",time[0],code[0])
                data.append(code[0])
        if time_check[0] == time_class:
            time_check = time[0].split(":")
            if int(time_check[1])<=10:
                code = line2.split()
                if code[0] in sec:
                    print("PRESENT :",time[0],code[0])
                    data.append(code[0])
               
            if int(time_check[1])>10:
                code = line2.split()
                if code[0] in sec:
                    print("LATE :",time[0],code[0])
                    data.append(code[0])
                  

for i in sorted(sec):
    if i not in sorted(data):
        print("ABSENT :",i)
    

    

f.close()


