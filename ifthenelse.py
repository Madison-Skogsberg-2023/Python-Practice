#define function
#add parameteres
def greaterThan10(x):
#if then else
    if x > 10:
        return "x is greater than 10."
    elif x == 10:
        return "x is equal to 10."
    else:
        return "x is less than 10."
print(greaterThan10(10))

#define function
def equalsTen(x):
#if then else
    if x == 10:
        return "x equals 10"
    elif x > 10:
        return "No, x is greater than 10"
    elif x < 10:
        return "No, x is less than 10"
    else:
        return "Invalid input. Please enter a numerical value for 'x'"
#run function
print(equalsTen(10))

#define function
#add parameters
def favColor(color):
    if color == "red":
        return "Your favorite color is red."
    else:
        return "Your favorite color is not red."
#run function
print(favColor("red"))

#define function
#add parameters
def define(word):
    if word.lower() == "bruh":
        return "Interjection, Something an individual says when they have nothing to contribute to the conversation."
    elif word.lower() == "somebody":
        return "Noun, The first word of All-Star, the song that plays in 'Shrek'."
    elif word.lower() == "cat":
        return "Noun, A small ball of indignation that brings joy."
    elif word.lower() == "minecraft":
        return "Noun, The best game of all time, created in 2010 by an absolute genius."
    elif word.lower() == "cornobble":
        return "Verb, The act of slapping an individual with a fish, usually across the face."
    elif word.lower() == "defenestrate":
        return "Verb, The act of throwing an individual out of a window."
    elif word.lower() == "lingable":
        return "Adjective, Whether something is able to be licked or not."
    elif word.lower() == "combustable":
        return "Adjective, Whether something is explosive."
    elif word.lower() == "mosquito":
        return "Noun (unfortunately), A small devil, an idiot, a nuisance, a plague upon the earth, nothing more than food for bats and birds. May they die a fiery death."
    elif word.lower() == "internet":
        return "Noun, A virtual community where everyone without anything to do resides for extended periods of time to deny their own existance. I am one of these people."
    else:
        return "Cannot define this word. Please pick another."
#run function
print(define("BRuH"))
