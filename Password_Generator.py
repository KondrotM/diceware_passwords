import random

def LoadAllowedWords():
  AllowedWords = []
  try:
    WordsFile = open("eff_large_wordlist.txt", "r")
    for Word in WordsFile:
      AllowedWords.append(Word.strip().lower())
    WordsFile.close()
  except:
    pass
  return AllowedWords
Word_List = LoadAllowedWords()

print("Password generator based off of diceware passphrases. Uses the eff wordlist. As an added caveat each character has 10% chance of being a symbol for added security.")
print()
print("Pick how many words your password is to be based off 6 should be enough but go for more if you want to stay ahead of future computing power." )
print()
print()
Quit = False
while Quit != True:
    Iterations = None
    while True:
        try:
            Iterations = int(input("How many words? \n>"))
            break
        except ValueError:
            print("Enter an integer pal")
    Password = ""
    for i in range(Iterations):
        Password = Password + Word_List[random.randint(0, len(Word_List))] + " "
    Password = Password[:-1]
    Password_Temp = []
    for i in range(len(Password)):
        if random.randint(0,100) < 10:
            Password_Temp.append(chr(random.randint(33,64)))
        else:
            Password_Temp.append(Password[i])
    Password = "".join(Password_Temp)

    print()    
    print(Password)
    if input("\n\nType enter to create another \nType x to quit") == "x":
        Quit = True
