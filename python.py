
import math 


message = "\t Stanley's cat"
print(message)

for x in range(0, 5):
    print(x)


print (ord('*'))



def addition(a, b):
    return (a+b)
def subtraction(a,b):
   return (a - b)
    
def Division(a,b):
    return (a/b)
def modulors(a,b):
    return (a%b)
def multi(a,b):
    return (a*b)
def display_func():
  print("CHOICES")
  print("1.add \n 2.subtract \n 3.modulors\
     \n 4.Divide \n 5.miltiplication")
  choices =(input("Enter choice: "))
  print("Enter two numbers")
  f_num = input("Enter a number: ")
  f_num = int(f_num)
  s_num = input("enter a number: ")
  s_num = int(s_num)

  if choices=='1':
   add_func= addition(f_num , s_num)
   print(add_func)

  elif choices=='2':
      sub_func = subtraction(f_num, s_num)
      print(sub_func)

  elif choices=='3':
      modulors_func = modulors(f_num, s_num)
      print(modulors_func)

  elif choices=='4':
      div_func =Division(f_num, s_num)
      print(div_func)

  elif choices=='5':
      mul_func = multi(f_num, s_num)
      print(mul_func)

  else:
      print("ooops! Check the menu again and make the right choice")





display_func()    