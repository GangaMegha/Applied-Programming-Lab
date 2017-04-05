#################    Dealing with files   #############

file_obj=open('test_file.csv','r')
file_contents=file_obj.read()	#read is a method on the file object

print file_obj
print file_contents
type(file_contents)	#Outputs 'str' when run in python

lines_from_file=file_contents.split('\n')
print lines_from_file
type(lines_from_file) #Outputs 'list' when run in python
type(lines_from_file[0]) #Outputs 'str' when run in python

file_contents=file_obj.readlines()	#readlines is a method on file objects
print file_contents

file_obj.seek(0)	#start from beginning of the file. Ie,move file pointer to beginning of file  , seek is a method on the file objects
file_contents=file_obj.readlines()
print file_contents

type(lines_from_file) #Outputs 'list' when run in python; add print in front if we want it to be printed onto the outputscreen while running as a file.
type(lines_from_file[0]) #Outputs 'str' when run in python

first_line=lines_from_file[0]
print first_line

repr(first_line)
first_line.strip("\n")	#method on string

dir(file_obj)	#gives the methods or attributes defined on the file object

file_obj.closed #gives False in python

dir(file_contents)	#gives the methods or attributes defined on the list

dir(first_line)	#gives the methods or attributes defined on the string

dir()
len(dir(__builtins__))



#####################   LOOPS   ###########################
file_obj.seek(0)
list_of_file_lines=file_obj.readlines()

no_of_lines=len(list_of_file_lines)	#Method 1
for i in range(no_of_lines) :		
	print list_of_file_lines[i]

for line in list_of_file_lines :	#Method 2 -> BETTER
	print line

file_obj.__iter__	#iter in file object
list_of_ints = range(10)
list_of_ints.__iter__	#iter in list

for char in 'a new beginning' :	#iterate per character in the string : it has its own iter
	print char

# for char in 100 :	#gives error : canot iterate over an integer
# 	print char

#for key, value in dictonary : #this is also valid.

file_obj.seek(0)
for index, line in enumerate(file_obj) :	#enumerate also gives the index of each line, starting from 0. line stores the item in the container
	if index>0 :	#to avoid say column headers
		print line

# string = 'hey!,I,added,a,new,line!'
# file_obj=open('test_file.csv','w+')
# file_obj.write(string)
# file_obj.close()

# with open('test_file.csv','w+') as file_obj:	#w+ for appending
# 	file_obj.write(string)

"{}".format(1)	#create string dynamically
"{}and,{}say,{}".format([1,2,3],4,5)
variable="arrey"
"{}".format(variable)
"variable : {}".format(variable)
str(variable)	#not preferred

column_1=[]		#remove comma and put space in the input csv file eg : a,1->a 2
column_2=[]
with open('test_file.csv','r') as file_obj:
	for line in file_obj :
		variables=line.split(',')
		print variables
		try :
			column_1.append(variables[0])
			column_2.append(variables[1])
		except IndexError:
			print "there is something wrong this is the line{}".format(line)
print column_1,column_2

column_1=[]		#remove comma and put space in the input csv file eg : a,1->a 2
column_2=[]
with open('test_file.csv','r') as file_obj:
	for line in file_obj :
		try :
			first_var,second_var=line.split(',')
			#print first_var,second_var
			column_1.append(first_var)
			column_2.append(second_var)
		except ValueError:
			print "bad line : {}".format(line)
print column_1,column_2

column_1=[]		#remove comma and put space in the input csv file eg : a,1->a 2
column_2=[]
with open('test_file.csv','r') as file_obj:
	for line in file_obj :
		try :
			first_var,second_var=line.split(',')
			#print first_var,second_var
			column_1.append(first_var)
			column_2.append(second_var)
		except Exception as e:
			print "bad line : {} with error : {} - with message {}".format(line,e,type(e)) #or use repr(type(e))
e.__repr__()	#prints the error in python
e.__str__()

an_integer=1
type(an_integer) #python returns 'int'

a_string="a string"
type(a_string) #python returns str

a_list=[1,2,3]
type(a_list)	#python returns list

a_dict = {"a" : 1,"b" :2}
type(a_dict)	#python returns dict

iterator=iter(a_list)
next(iterator)	#gives 1 		For loop implicitly calls the next(), iter() function used to iter over the list
next(iterator)	#gives 2
next(iterator)	#gives 3
next(iterator)	#gives error ->stop iteration ->for loop catches this and stops

a_list.__iter__()

def func(a,b) :
	print a,b
	return (a+b)*(a-b)

func(1,2)	#position arguments
func(1,b=2)
func(a=1,b=2)	#keyword arguments
func(a=1,2)	#->wont work
func(*[1,2])
func(**{'a':1,'b':2})
a_dict={'a':1,'b':2}
func(**a_dict)

def fun(a,b=None) :
	print a,b
	return (a+b)*(a-b)
fun(1)	#error, but if b was given as default, then this would have worked
fun(1,2)	#works

def fun1(a,b,*args) :
	print "a={},b={},{}".format(a,b,args)
	print type(args)	#args is a touple
	return (a+b)*(a-b)

fun1(1,2,*[1,2,3,4])
fun1(1,2,3,4)

print type(fun1)	#everything is an object in python
print dir(fun1)

fun1.__call__(1,2)

def generate_functions(a) :
	def function() :
		return a
	return function

generate_functions(1)	#functions returning functions

Generated_function=generate_functions(1)
Generated_function()

def fun2(a,b,c):
	return(a,b,c)

print fun2(1,2,3)
a,b,c=fun2(2,3,4)
print a,b,c

#####################  CLASS   ##########################

class CustomClass(object):	#object is a python object. It inherits all the fancy things
	def __init__(self,a,b):	#first argument is always 'self'
		self.a=a 	#a is an attribute on the instance and set the value of b to the position argument u passed, which is b
		self.b=b 	#self refers to the instance
		return None

	def update_a(self,value):
		self.a +=value
		return None

instance = CustomClass(10,11)

print instance.a
instance.b

dir(instance)


class CustomClass():	#object is a python object. It inherits all the fancy things
	def __init__(self,a,b):	#first argument is always 'self' -> called when we try to initialise the instance
		self.a=a 	#a is an attribute on the instance and set the value of b to the position argument u passed, which is b(passed to class)
		self.b=b 	#self refers to the instance
		return None

	def update_a(self,value):
		self.a +=value
		return None

instance = CustomClass(10,11)

print instance.a
instance.b

dir(instance)

CustomClass.update_a
instance.update_a
instance.update_a(30)
instance.a

class CustomClass(object):	#object is a python object. It inherits all the fancy things
	def __init__(self,initial_pos,initial_vel):	#first argument is always 'self'
		self.initial_pos=initial_pos 	#a is an attribute on the instance and set the value of b to the position argument u passed, which is b
		self.initial_vel=initial_vel 	#self refers to the instance
		return None

	def update_a(self,vel):
		self.initial_vel +=vel
		return None

#########################  GENERATORS  #################################,meta-classes in python

def custom_generator(*args,**kwargs) :
	#do something
	yield *args,**kwargs
