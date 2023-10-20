top=0
a_tat=0.0
a_wt=0.0
at=[]
bt=[]

n=int(input("No. of Process:"))

for i in range(n):
    pro=int(input("P%d Arrival Time :: " %(i+1)))
    at.append(pro)
    pro=int(input("P%d Burst time :: " %(i+1)))
    bt.append(pro)

ct=[]
tat=[]
wt=[]
print()

for i in range(n):
    if i==0:
        top=top+ bt[i]
        ct.append(top)
    
    elif i>0:
        if top <at[i]:
            top=at[i] + bt[i]
            ct.append(top)
        
        else: 
            top=top + bt[i]
            ct.append(top)

print("CT: ", ct, "\nAT: ",at)
print("COmpleted Time Calculator")

for i in range(n):
    var=ct[i]- at[i]
    tat.append(var)
    var1=tat[i]-bt[i]
    wt.append(var1)

for i  in range(n):
    print(str(i+1) + "\t\t"+ str(at[i])+ "\t\t" + str(bt[i]) + "\t\t" + str(ct[i]) + "\t\t" + str(wt[i]))

    a_tat= a_tat +tat[i]
    a_wt = a_wt +wt[i]

a_tat=a_tat /n
a_wt= a_wt /n
print()

print("AVG TAT:: ",a_tat)
print("AVERAGE WT :: ",a_wt)
