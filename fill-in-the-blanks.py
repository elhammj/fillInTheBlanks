# IPND Stage 2 Final Project
# Elham Jaffar
# It is a Fill-in-the-Blanks quiz.
# The quiz will prompt a user with a paragraph containing several blanks.
# The user should then be asked to fill in each blank appropriately to complete the paragraph.
# This can be used as a study tool to help us as a python programmer remember important vocabulary!
#This program can be run by command line or python IDEL
# To help you get started, we've provided a sample paragraph that you can use when testing your code.
# Your game should consist of 3 or more levels, so you should add your own paragraphs as well!

#according to user input, call the below quesitons and answers
firstQ = '''___1___ is completely object oriented programming language, and not "statically typed". You do not need to declare ___2___ before using it, or declare its ___3___. Every ___2___ in ___1___ is an ___4___.'''
secondQ = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary, tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''
thirdQ = ''''The ___1___ is a most versatile datatype available in Python which can be written as a ___1___ of comma-separated values (items) between ___2___ brackets. Important thing about a ___1___ is that items in a list need not be of the same ___3___. To access values in lists, use the ___2___ brackets along with the ___4___. The first element in the ___1___ has zero ___4___'''
#set of blanks to compare their index with answers and to replace if the user enters correct asnwer
blanks = ['___1___','___2___','___3___','___4___']
answer1= ['python','variable','type','object']
answer2= ['function','parameters','none','lists']
answer3= ['list','square','type','index']

#function that gets the level from user and call the game fnction by passing quesiton and answer numbers
#accroding to user choice
#there is 3 levels and an option for the user to quit in case the user changes his/her mind
def level(input):
	#check now the options, if user inputs (1)
	if(input=='1' or input.lower()=="easy"):
		game(firstQ,answer1)
	#check now the options, if user inputs (2)
	if(input=='2' or input.lower()=="medium"):
		game(secondQ,answer2)
	#check now the options, if user inputs (3)
	if(input=='3' or input.lower()=="hard"):
		#call Easy funciton
		game(thirdQ,answer3)
	#check now the options, if user inputs (4)
	if(input=='4' or input.lower()=="quit"):
		print "Thank you for playing the game, see you next time"
		return; #To stop

#function that takes question form level funciton and its answers.
#it displays the question, compare with answers and check number of attempts
#if user win, then ask for play again
#if user lose, give another chance until reaching 4 mistakes, start the game again 
def game(question,answer):
	print question
	index = 0 #to hold
	attemp = 0 #To limit number of mistakes
	maxAttempts=4 #although the limit, it is 4 but because we start with 1
	while len(blanks)>index:
		userAnswer = raw_input("What is " + blanks[index] +"?")
		#Case 1: When the user enter right answer
		if userAnswer.lower() == answer[index]:
			question = updateTheSentence(question,answer,index)
			index+=1 #increse the index by 1
		#Case 2: When the user enter wrong answer
		else:
			#ask user again
			attemp+=1
			print "Oops ! let's try again, you can do it! Note: Max number of mistakes is 4. You have made "+ str(attemp) +" mistake"
			#reaching max number of attempting 4 so when it becomes 5 this is max
			if attemp==maxAttempts:
				print "You need to study harder. Let's start the game all over again!"
				level(raw_input("Please, select the level: \n1-Easy 2-Medium 3-Hard 4-Quit\n"))

#win function that takes no input and print the winning message for the user
#it asks the user if he/she wants to play again
def win():
	done=False #flag if the user want to quit
	print "CONGRATS ! You win !!!!!!"
	playAgain = raw_input("Would you like to try another level ?").lower()
	while ((playAgain!='yes' or playAgain!='no') and done==False): #to handle other inputs
		if playAgain == 'yes':
			level(raw_input("Please, select the level: \n1-Easy 2-Medium 3-Hard 4-Quit\n"))
		elif playAgain == 'no':
			print "See you again"
			done=True
			return done #to stop the game
		else:
			playAgain = raw_input("Enter either yes or no?").lower()

#update the sentence with the correct answer
#it takes the question, answer and current index to perform the replacement task
#print the new sentance and if the user has filled all the blanks correctly, it call win() function
def updateTheSentence(question,answer,index):
	print "Right Answer! :)"
	question = question.replace(blanks[index],answer[index])
	print question
	index+=1 #increse the index by 1
	#means 4 right answers, User win
	numberOfBlanks=4
	if (index==numberOfBlanks):
		win();
	return question 


# Greetings
print "Welcome to Python Game!!"
#Welcoem msg & Prompt the user to choose the level, then start the game
gInput = raw_input("Please, select the level: \n1-Easy 2-Medium 3-Hard 4-Quit\n")
level(gInput)

