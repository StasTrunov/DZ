def check_phone(phone):
   if len(phone) == 10: 
      return True
   else: 
      return False

def mobile_operator(phone):
   Kievstar = ('068', '067', '097')
   Vodafone = ('050', '066', '099')
   Lifesel = ('063', '093')
   code = phone[0:3]
   if code in Kievstar:
     return 'Kievstar'
   elif code in Vodafone:
     return 'Vodafone'
   elif code in Lifesel:
     return 'Lifesel'
   else:
      return 'None'

fh = open(r'C:\Users\PC\Desktop\Python\Part1\Homework\hw-10\phones1.txt') 
lines = fh.readlines()

#K_file = open(r'C:\Users\PC\Desktop\Python\Homework\hw-10\phones-K.txt')
#V_file = open(r'C:\Users\PC\Desktop\Python\Homework\hw-10\phones-V.txt')
#L_file = open(r'C:\Users\PC\Desktop\Python\Homework\hw-10\phones-L.txt')

K_file = open('phones-K.txt','a')
V_file = open('phones-V.txt','a')
L_file = open('phones-L.txt','a')


for i in lines:
   if check_phone(i[:-1]):
      if mobile_operator(i)=='Kievstar':
         K_file.write(i)
      elif mobile_operator(i)=='Vodafone':
         V_file.write(i)
      elif mobile_operator(i)=='Lifesel':
         L_file.write(i)
      else:
         print ('Phone number', i[:-1], 'is not mobile')
   else:
      print ('Phone number', i[:-1], 'is incorrect')


fh.close()
K_file.close()
V_file.close()
L_file.close()

#K_file = 'Python\Homework\hw-10\phones-K.txt'
#V_file = 'Python\Homework\hw-10\phones-V.txt'
#L_file = 'Python\Homework\hw-10\phones-L.txt'

#K_file = open('K_file', 'a')
#V_file = open('V_file', 'a')
#L_file = open('L_file', 'a')

#K_file.write(mobile_operator['Kievstar'])
