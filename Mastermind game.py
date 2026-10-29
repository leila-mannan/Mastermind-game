import random
def generate_code():
    random_code=""
    letters = ["A", "B", "C", "D", "E", "F"]
    for i in range(4):
        random_char = random.choice(letters)
        random_code+=random_char
    return random_code
    
def count_exact_and_inexact_matches(secret_code, guessed_code):
  exact_matches=0
  inexact_matches=0
  guessed_code = list(guessed_code)
  for i in range(len(secret_code)):
      if guessed_code[i]==secret_code[i]:
          exact_matches+=1
          guessed_code.pop(i)
          guessed_code.insert(i,"")
      elif guessed_code[i] in secret_code:
          inexact_matches+=1
  return (exact_matches, inexact_matches)

#Main game starts here
secret_code=generate_code()
print("DEBUG MESSAGE: secret_code=",secret_code)
tries=1
while True:
    print("Attempt number:",tries)    
    guess=input("What is your guess? ")
    if len(guess)==4:
        exact_matches, inexact_matches = count_exact_and_inexact_matches(secret_code, guess)
        feedback="Num correct exactly: "+str(exact_matches)+".  Num correct inexactly: "+str(inexact_matches)
        if exact_matches == 4:
            print("Feedback:",feedback)
            print(f"Congratulations. That took {tries} tries.")
            break
        else:
            tries+=1
            print("Feedback:",feedback)
    else:
        print("Please enter a string of length 4.")
