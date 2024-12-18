l = int(input("Enter your algorithm total size :"))
#arrival time
p = []
at = []
bt = []
ct = []
tat = []
wt = []
#process
print("\t\t\t\tENTER YOUR PROCEES")

for i in range (0,l):
        ele = int(input("Enter process :"))
        p.append(ele)
    
def process(p):
    v=0
    for v in range(0,l):
        print(p[v])
process(p)

 #arrival time
print("\t\t\t\tENTER YOUR ARRIVAL TIME ")
for j in range (0,l):
    ele = int(input("Enter arrival time  :"))
    at.append(ele)

#burstand  time
print("\t\t\t\tENTER YOUR BURSTAND TIME ")
for k in range (0,l):
    ele = int(input("Enter busstand time :"))
    bt.append(ele)

#complition time

ele=0
for c in range(0,l):
    ele = ele + bt[c]
    ct.append(ele)
 
print("GRANT CHART :",ct)

#turn - around- time

tatc = 0
for i in range(0,l):
    tatc = ct[i] - at[i]
    print(tatc)
    tat.append(tatc)
   
print("tat:",tat)

#wainting- time

wtc = 0
for w in range(0,l):
    wtc = tat[w] - bt[w]
    print(wtc)
    wt.append(wtc)
  


#print
print("PROCESS","\tA.T ","\t B.T", "\tC.T","\tF.T ","\t T-O-T","\t W.T")
for i in range(0,len(bt)):
        print("p",[i],"\t",at[i],"\t",bt[i],"\t",ct[i],"\t",tat[i],"\t",wt[i])

