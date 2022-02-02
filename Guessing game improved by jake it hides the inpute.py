import getpass
secret_word = getpass.getpass("Choose you secret word: ")
guess = ""
guess_count = 0
guess_limit = 3
guess_limit2 = 2
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter your guess here:")
        guess_count += 1
    else:
        out_of_guesses = True    
    if guess_count == guess_limit2:
        print("The hint is it starts with")



if out_of_guesses:
    print("Out of Guesses, YOU LOSE!")
else:
    print("You win Yes the name is")   
  