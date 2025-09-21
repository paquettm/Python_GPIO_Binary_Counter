#this is a comment, we will usually talk of code near the comment

#text to speech library
import pyttsx3

#this is a function to print and use text to speech
def say(obj, sound = False):
	something = str(obj) #convert anything to a string because the TTS engine expects a string

	print(something)

	engine = pyttsx3.init() # object creation

	# VOICE
	voices = engine.getProperty('voices')       # getting details of current voice
	engine.setProperty('voice', voices[1].id)   # changing index, changes voices. 1 for female

	engine.say(something)
	engine.runAndWait()

def sayStats():
	say(f"index counter = {example.i} and count = {example.count}")

#this is a class which we use to demonstrate class variables, instance variables, and magic functions
class example:
	count = 0
	i = 0

	#magic functions get invoked automatically when specific events occur
	#their names are always the same and start and end with two underscore (_) characters

	#magic function invoked at object initialisation (constructor)
	def __init__(self):
		example.count+=1
		example.i+=1
		self.id = example.i
		say(f"{self} created")
		sayStats()

	#magic function invoked when trying to convert the object to a string
	def __str__(self):
		return f"Item #{self.id}"

	#magic function invoked when deleting the existing object
	def __del__(self):
		say(f"Deleting {self}")
		example.count-=1
		sayStats()

ex_list = []
say("Creating 3 example objects")
for i in range (0,3):
	ex_list.append(example())


print("\n".join(map(str, ex_list)))

say(f"list length = {len(ex_list)}")

del(ex_list[1])
del(ex_list[1])

say(f"list length = {len(ex_list)}")

say("Creating 2 new objects")
ex_list.append(example())
ex_list.append(example())

say(f"list length = {len(ex_list)}")

del(ex_list[0])
del(ex_list[0])
del(ex_list[0])

say(f"list length = {len(ex_list)}")


