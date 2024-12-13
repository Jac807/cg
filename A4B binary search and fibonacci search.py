a=[]
n=int(input("enter the number who attended the training program="))
print(n)
for i in range (n):
 f=int(input("enter the roll nos of student who attended the training program"))
 print("please enter number in ascending order")
 a.append(f)
print(a)
k=int(input("enter roll no which have to search"))

def binary_search(a,n,k):
 l=0
 u=n-1
 while (l<=u):
   mid=int((l+u)/2)
   if (k==a[mid]):
     print("student attend the training program")
     break
   elif (k>a[mid]):
     l=mid+1
   elif (k<a[mid]):
     u=mid-1
 else:
    print("student not attend the training program")   

 

def fibonaaci_search(a,n,k): 
      offset=-1
      fibn_2=0
      fibn_1=1
      fibn=fibn_1+fibn_2
      while(fibn<=n):
         fibn_2=fibn_1
         fibn_1=fibn
         fibn=fibn_1+fibn_2
      while(fibn_1!=0):
         i=min((offset+fibn_2),n-1)
         if(k>a[i]):
            fibn=fibn_1
            fibn_1=fibn_2
            fibn_2=fibn-fibn_1
         elif(k<a[i]):
            fibn=fibn_2
            fibn_1=fibn_1-fibn_2
            fibn_2=fibn-fibn_1
         elif(k==a[i]):
          print("student attended the program")
          break
      else:
         print("student not attended the program")


flag=1
while(flag==1):
   print("1.binary search")
   print("2.fibonacci search")
   print("3.Exit")
   x=int(input("Enter your choice="))
   if x==1:
     print("binary search is=")
     binary_search(a,n,k)
   elif x==2:
     print("fibonacci search is=")
     fibonaaci_search(a,n,k)
   elif x==3:
     print("Exit")
     flag=0  
   else:
    print("invalid choice")
   

			 		
