'''
Created on Feb 27, 2014

@author: mchan_000
'''

########## Helper Functions ##################
def pCalc(listR=[0]):
    sum=0
    for ele in listR:
        sum+=1/ele
    return 1/sum
def sCalc(listR=[0]):
    sum=0
    for ele in listR:
        sum+=ele
    return sum
def checkNum(i):
    if i == '.': return True
    try:
        a=int(i)
        return True
    except: return False
########### Legwork Functions ##########################
def calculate(QQ):
    sP=[]
    eP=[]
    for i in range(len(QQ)):
        if   QQ[i] == "(": sP.append(i)
        elif QQ[i] == ")": eP.append(i)
    if len(sP) != len(eP):
        print("Incorrect Syntax")
        for ele in QQ: print(str(ele),end="")
        print()
    link={}
    keys=[]
    numKeys=0
    pCount=0
    for i in range(len(QQ)):
        if QQ[i]=='(':
            for j in range(i,len(QQ)):
                if QQ[j]  =="(": pCount+=1
                elif QQ[j]==")": pCount-=1
                if pCount == 0:
                    link[i] = j
                    keys.append(i)
                    numKeys+=1
                    break
    keys = keys[::-1]
    for num in keys:
        endBlock = link[num]
        sol = solve(QQ[num+1:endBlock])
        getRidOf=int((endBlock-num)/2)-1
        temp = ['-',0]*getRidOf
        QQ.insert(num+1,sol)
        L=QQ[:num+2]
        L.extend(temp)
        L.extend(QQ[endBlock+1:])
        QQ = L
    return solve(QQ)
        
def solve(block):
    Qop=[]
    QQ=[]
    for ele in block:
        if ele=="(" or ele==")": continue
        if ele=="-" or ele=="=": Qop.append(ele)
        else: QQ.append(ele)
    QQ = QQ[::-1]
    Qop = Qop[::-1]
    while len(QQ) > 1:
            int1=QQ.pop()
            int2=QQ.pop()
            oper=Qop.pop()
            if oper == '-': QQ.append(sCalc([int1,int2]))
            else          : QQ.append(pCalc([int1,int2]))
    return QQ[0]
#####################################
def parseResist(string):
    saved=string
    if string == "": string = "0"
    string = "(" + string + ")"
    QQ=[]
    multi = ""
    for i in range(len(string)):
        letter = string[i]
        if letter == ' ': continue
        if not checkNum(letter):
            if len(multi)>0:
                QQ.append(float(multi))
                multi = ""
            QQ.append(letter)
        elif letter=='.':
            multi+='.'
        elif checkNum(letter):
            multi+=letter
    if len(multi)>0: QQ.append(float(multi))
    if len(QQ)%2==0:
        print(saved + "\nSomething's wrong...")
        return "Unknown"
    return calculate(QQ)
    
###########################
if __name__ == "__main__":
    s=""
    while True:
        s = input("Enter a resistance string (-1 to quit): ")
        if s=='-1': break
        print('Equiv. Resist: ' + str(parseResist(s)) + ' ohms')


