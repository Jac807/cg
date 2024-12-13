a=[]
n=int(input("enter the number of student who attend the training program="))
print(n)
for i in range(n):
 f=int(input("enter the roll no of student who who attend the training program="))
 a.append(f)
print(a)
k=int(input("enter roll no which have to search=")) 

def linear_search(a,n,k):
    for i in range(n):
      if(a[i]==k):
       print("student attended the training program")
       break
    else:
       print("student not attend the training program")   



def sentinel_search(a,n,k):
   a.append(k)
   for i in range(len(a)-1):
      if(a[i]==k):
       print("student attended the training program")
       break
   else:
       print("student not attend the training program")   


flag=1
while (flag==1):
	print("1.linear search")
	print("2.sentinel search")
	print("3.Exit")
	x=int(input("Enter your choice="))
	if x==1:
	  print("linear search is=")
	  linear_search(a,n,k)
	
	elif x==2:
	  print("sentinel search is=")
	  sentinel_search(a,n,k)
	
	elif x==3:
	  print("Exit")
	  flag=0  
	  
	else:
	  print("invalid choice")
