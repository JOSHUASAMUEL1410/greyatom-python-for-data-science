# --------------
# Code starts here

# Create the lists 
class_1=['Geoffrey Hinton','Andrew Ng','Sebastian Raschka','Yoshua Bengio']
class_2=['Hilary Mason','Carla Gentry','Corinna Cortes']
new_class=class_1+class_2
print('new_class=',new_class)
# Concatenate both the strings
new_class.append('Peter warden')
print('new_class=',new_class)
new_class.remove('Carla Gentry')
print('new_class=',new_class)
# Create the Dictionary
courses={'math':65,'english':70,'history':80,'french':70,'science':60}
print('courses=',courses)
math=65
english=70
history=80
french=70
science=60
total = math+history+science+english+french
print('tatol=',total)
percentage=(total/500)*100
print('percentage=',percentage)
mathematics={'Geoffrey Hinton':78,'Andrew Ng':95,'Sebastian Raschka':65,'Yoshua Benjio':50,'Hilary Mason':70,'Corinna Cortes':66,'Peter Warden':75}
topper=max(mathematics, key=mathematics.get)
print('topper=',topper)
print(topper.split())
first_name=topper[:6]
print('first_name=',first_name)
last_name=topper[7:]
print('last_name=',last_name)
full_name=last_name+" "+first_name
print('full_name=',full_name)
certificate_name=full_name.upper()
print('certificate_name=',certificate_name)






