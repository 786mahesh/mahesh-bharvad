m=int(input("Enter one subject total marks :"))
t=m+m+m+m
print("YOUR TOTAL MARKS:",t)
print("NEDD OF MARKS FROM PASS THIS EXAM :",m-40)

  #slp marks grade calculation
s = float(input("Enter a slp marks:"))    
if s<=m and s>=m-10:
        grade="a"
elif s<m-10 and s>=m-20:
        grade="b"
elif s<m-20 and s>=m-30:
    grade="c"
elif s<m-30 and s>=m-40:
        grade="d"
else:
        grade="FAILL..!!"

         #rdbms marks grade calculation
r = float(input("Enter a rdbms marks:"))
if r<=m and r>=m-10:
        grade1="a"
elif r<m-10 and r>=m-20:
        grade1="b"
elif r<m-20 and r>=m-30:
        grade1="c"
elif r<m-30 and r>=m-40:
        grade1="d"
else:
        grade1="FAILL..!!"

        #bos marks grade calculation
b = float(input("Enter a bos marks:"))
if b<=m and b>=m-10:
        grade2="a"
elif b<m-10 and b>=m-20:
        grade2="b"
elif b<m-20 and b>=m-30:
        grade2="c"
elif b<m-30 and b>=m-40:
        grade2="d"
else:
        grade2="FAILL..!!"

        # dsa marks grade calculation
d = float(input("Enter a dsa marks:"))
if d<=m and d>=m-10:
        grade3="a"
elif d<m-10 and d>=m-20:
        grade3="b"
elif d<m-20 and d>=m-30:
        grade3="c"
elif d<m-30 and d>=m-40:
        grade3="d"
else:
        grade3="FAILL..!!"
print("\t\t\t********MARKSHEET********")
print("\n**SUBJECT**","\t\t\t*MARKS*","\t\t\t**GRADE**")
print(" SLP","\t\t\t\t",s,"\t\t\t\t",grade)
print(" RDBMS","\t\t\t\t",r,"\t\t\t\t",grade1)
print(" BOS","\t\t\t\t",b,"\t\t\t\t",grade2)
print(" DSA","\t\t\t\t",d,"\t\t\t\t",grade3)

    #parsantage calculation
p=s+r+b+d
print("YOUR ALL SUBJECT TOTAL MARKS:",t)
print("YOU ARE TAKE MARKS IN EXAM :",p)
if p==p:
        print("\t\tCONGRATILATION...!!!")
        print("\t\t YOUR ARE FIRST THIS EXAM ")
elif p<p and p>=p-50:
       print("\t\tCONGRATILATION...!!!")
       print("\t\t YOUR ARE SECOUND THIS EXAM ")
elif p<p-50 and p>=p-100:
      print("\t\tCONGRATILATION...!!!")
      print("\t\t YOUR ARE THIRD THIS EXAM ")
elif p<p-100 and p>=p-160:
      print("PASS THIS EXAM")
else:
      print("YOU ARE FAILL THI EXAM...!!!")
ans=t*100/p
print("\nYOUR PARSANTAGE :=",ans)
print("\t\t\t\t----------")
print("\t\t\t\t|print|")
print("\t\t\t\t---------")



