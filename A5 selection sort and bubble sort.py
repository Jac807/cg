a=[]
n=int(input("enter number of students"))
print(n)
for i in range(n):
 f=float(input("enter percentage of students"))
 a.append(f)
print(a)

def bubble_sort(a,n):
 for i in range(1,n-1):
  for j in range(0,n-1):
   if(a[j]>a[j+1]):
    temp=a[j]
    a[j]=a[j+1]
    a[j+1]=temp
 print("sorted list is=",a)
  
 a.reverse()
 print(a[0:5])


def selection_sort(a,n):
 for i in range(n-1):
  min=i
  for j in range(i+1,n):
     if(a[min]>a[j]):
      temp=a[j]
      a[j]=a[min]
      a[min]=temp
 print("sorted list is",a)


 a.reverse()
 print(a[0:5])
  
flag=1
while(flag==1):
   print("1.bubble sort")
   print("2.selection sort")
   print("3.Exit")
   x=int(input("Enter your choice="))
   if x==1:
     print("bubble sort is=")
     bubble_sort(a,n)
   elif x==2:
     print("selection sort  is=")
     selection_sort(a,n)
   elif x==3:
     print("Exit")
     flag=0  
   else:
    print("invalid choice")
   

			 		
