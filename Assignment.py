python 2.7.15

print ("*****************************************")
print ("{{{{{{{{{*---Assignment work---*}}}}}}}}}")
print ("*****************************************")
print ("log in ..")
username = raw_input("name: ")
rollno = raw_input("rollno: ")
Class = input("class: "  )
regno = input("reg.no; ")
print "hello ,",username 
def maths():
  print "--- maths assignment ---"
  print "66/3"
  user=raw_input("ans: ")
  if user == (66/3):
    print "good"
  else:
    print "wrong answer..",username
    print "answer",66/3
  print "254368*23"
  user=input("ans: ")
  if user == (254368*23):
    print "nice good job",username 
  else:
    print "wrong answer..",username
    print "ans: ",254368*23 

def computer():
  print "what is computer system? "  
  user=raw_input("ans: ")
  print  "good"
  print "1MB = ? "
  user == input("ans: ")
  if user == "1024" :
    print "nice"
  else:
    print "wrong answer,answer is  :1024"
    print "1kb = ?"
    user = input("ans:")   
    if user == "1024":
      print "good "
    else:
      print "wrong answer"
      print "answer :1024"
   
       
def physics():
  print " what is physics? "
  user = raw_input("ans: ")
  print "nice ..."
  print "forces dimention formula .."
  user = raw_input ("ans: ")
  if user == [MLT^-2]:
    print "nice ..",username
  else:
    print "wrong ans",username 
    print "[MLT^-2]"
  print "what is unit ?"
  user = raw_input("ans: ")
  print "good.. "
  
def chemistry():
  print "what mole?"
  user = raw_input("ans: ")
  print "good "
  print "what  is matter?"
  user=raw_input("ans: ")
  print "good"
  print "what is mass number?"
  user=raw_input("ans: ")
  print " ..nice.. "
  
def menu():
   #print what option you have 
   print "[----welcome to e-assignment----]"
   print "[--your option--]"
   print ""
   print "1)maths.."
   print "2)computer.."
   print "3)physics.."
   print "4)chemistry.."
   print "5)quit e-assignment "
   print ""
   return input("choose your option: ")
    
#NOW THE PROGRAM REALLY START,AS CODE IS RUN 
loop = 1
choice = 0   
while loop == 1:
  choice = menu()
  if choice == 1:
    maths()
  elif choice == 2:
    computer()
  elif choice == 3:
    physics()
  elif choice == 4:
    chemistry()
  elif choice == 5:
    loop = 0  
    
print "[---thank u star plz---]"
#NOW THE PROGRAM REALLY FINISHES  
