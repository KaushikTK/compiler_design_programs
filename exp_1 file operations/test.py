import numpy as np

print('1. Add')
print('2. Delete')
print('3. Display')
print('4. Update')
print('5. Calculate avg')
print('6. Exit')

data = []

#x = np.load('data.npy')
#print(str(x))
#data.append([100,56,67,45])
#data = np.array(data)
#np.save('data.npy',data);


def add(roll,a,b,c,data):
    data.append([roll,a,b,c])
    data = np.array(data)
    print('data added')
    print('The data in file now is: ')
    print(str(data))
    print('\n')
    np.save('data.npy',data)

def delete(roll,data):
    for i in range(len(data)):
        if(data[i][0] == roll):
            del(data[i:i+1])
            np.save('data.npy',data)
            print('data deleted')
            print('The data in file now is: ')
            print(str(data))
            print('\n')
            return 
    print('roll number not found')

def display(roll,data):
    x = ['Roll:','Mark 1:','Mark 2:','Mark 3:']
    for i in range(len(data)):
        if(data[i][0] == roll):
            for j in range(1,4):
                print(x[j]+str(data[i][j]))
    print('\n')

def update(roll, ip, m, data):
    for i in range(len(data)):
        if(data[i][0] == roll):
            data[i][ip] = m
            np.save('data.npy',data)
            print('data updated')
            print('The data in file now is: ')
            print(str(data))
    print('\n')
            
def cal_avg(roll,data):
    for i in range(len(data)):
        if(data[i][0] == roll):
            tot = data[i][1]+data[i][2]+data[i][3]
            tot = float(tot/3)
            print('the average of the marks is: '+ str(tot))
    print('\n')


while(True):
    choice = int(input('enter the operation u want to execute: '))

    if(choice == 6):
        break
    else:
        data = np.load('data.npy')
        data = list(data)
        if(choice == 1):
            roll = int(input('enter roll: '))
            a = float(input('mark 1: '))
            b = float(input('mark 2: '))
            c = float(input('mark 3: '))
            add(roll,a,b,c,data)

        elif(choice == 2):
            roll = int(input('enter roll: '))
            delete(roll,data)

        elif(choice == 3):
            roll = int(input('enter roll: '))
            display(roll,data)

        elif(choice == 4):
            roll = int(input('enter roll: '))
            ip = input('enter 1 for updating mark 1, 2 for mark 2 and 3 for mark 3: ')
            m = float(input('enter the new mark:'))
            update(roll,int(ip),m,data)

        elif(choice == 5):
            roll = int(input('enter roll: '))
            cal_avg(roll,data)

        elif(choice == 6):
            break