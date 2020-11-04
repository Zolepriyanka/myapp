class UnderAge(Exception):  
   def __init__(self,value):
       self.value=value
   def __str__(self):
       return(self.value)

def verify_age(age):
 try:
      if int(age)<18:
          raise UnderAge(age)
      else:
          print("Age:"+str(age))
 except UnderAge as ua:
       print("UnderAge Exception Occurred:age value is:",ua.value)


verify_age(23)
verify_age(17)
a = [int(x) for x in input().split()]





                
