from tkinter import *
from PIL import ImageTk, Image

root =Tk()
root.title('Hangman Pog')
root.geometry("260x260")

letters_guessed = " "

win =False

counter =0

#turn list into a string
def listToString(list):
    str1 = ""
    return(str1.join(list))
#set a word as the answer for the game
def submit_word():
    #get input from screen
    global answer
    answer = Screen.get()
    global answer_letters
    #set input as key
    answer_letters = list(answer.lower())
    #update page to play game
    global blank
    blank = ["_"] * len(answer_letters)
    #better for printing on the gui with a space
    global blank_str
    blank_str= ["_ "] * len(answer_letters)
    str_blank = listToString(blank_str)
    #put blank letters on screen
    global blank_label
    blank_label = Label(root, text=str_blank)
    #clear screen for new input
    Screen.delete(0,END)
    start_button.grid_forget()
    #update the label with instructions and update buttons and locations
    title_label.config(text= "Guess a letter, or the Word")
    title_label.grid(row= 6, column= 1, columnspan=1)
    blank_label.grid(row=7,columnspan=1, column = 1)

    Guess_button.grid(row=3, pady=10, column=1, columnspan=1, ipadx=10)
    Guess_word_Button.grid (row=3, column =2, columnspan=1, ipadx=7 )
    #put up hangman image on screen
    my_label.grid(row=9, column=1, pady=20)
    Error_label.grid(row=1, column =1)


def guess_letter():
    update_letter_guessed()
    guess_with_key()
    Screen.delete(0,END)
    check_word()



def update_letter_guessed():
    letters_guessed = has_letter_been_used()
    if letters_guessed == False:
        return
    else:
        letters_guessed_label.config(text = str(letters_guessed.rstrip(", ")))
        letters_guessed_title_label.grid(row=6, column=2)
        letters_guessed_label.grid(row=7, column=2)


def counter_func():
    global counter
    counter += 1
    check_counter()
    Error_label.config(text= "That is not correct. You have " + str(5- int(counter)) + " guesses left" )
    Error_label.grid(row=0, column=1, columnspan=2)
    return counter

def guess_with_key():
    letter_guessed =reconfig_input()
    if letter_guessed in answer_letters:
        letter_location = [i for i, x in enumerate(answer_letters) if x == letter_guessed]
        for i in letter_location:
            blank_str[int(i)] = letter_guessed
            blank_label.config(text= listToString(blank_str))
            return blank_str
    else:
            counter_func()

def has_letter_been_used():
    letter_guessed = reconfig_input()
    global letters_guessed
    if letter_guessed in letters_guessed:
        Error_label.config(text="you have already guessed that letter")
        Error_label.grid(row=0, column= 1, columnspan=2)
        return False
    else:
        letters_guessed += letter_guessed + ", "
        return letters_guessed

def reconfig_input():
    if check_letter_length() == True:
        guess = Screen.get()
        global letter_guessed
        letter_guessed = guess[0]
        letter_guessed = letter_guessed.lower()
        return letter_guessed
    else:
        Screen.delete(0,END)


def check_letter_length():
    guess= Screen.get()
    if len(guess)!=1:
        Error_label.config(text="Guess one letter at a time")
        Error_label.grid(row=0, column=1, columnspan=2)
        Screen.delete(0, END)
    else:
        return True


def guess_word():
    guess = Screen.get()
    if (guess).lower() == answer.lower():
        check_word()
    else:
        global counter
        counter += 1
        Error_label.config(text="Wrong Word, You have " + str(5 - counter) + " many more tries!")
        Error_label.grid(row=0, column=1, columnspan =2)
        check_counter()
        Screen.delete(0, END)




def check_counter():
    if counter == 5:
        Error_label.config(text="You lose :( The word was " + answer + "!")
        clear_page()


def check_word():
    guess= Screen.get()
    if listToString(blank_str) == answer.lower() or guess.lower() == answer.lower():
        Error_label.config(text="You guessed it!, The word was " + answer + "!")
        Error_label.grid(row=0, column=1, columnspan=2)
        clear_page()

def clear_page():
    Guess_button.grid_forget()
    Screen.grid_forget()
    title_label.grid_forget()
    blank_label.grid_forget()
    letters_guessed_label.grid_forget()
    Guess_word_Button.grid_forget()
    my_label.grid_forget()
    letters_guessed_title_label.grid_forget()

   # letters_guessed_label.grid_forget


title_label = Label(root,text = "Enter your word" )
#title_label.grid(row=5, column = 1)


Screen = Entry(root, width = 35, borderwidth=5, bg="#dcdcdc")
Screen.grid(row=2, column=0, columnspan=5,rowspan= 1, padx=10, pady=10,stick=W+E+N+S)


start_button = Button(root,text = "Submit a word", command = submit_word)
start_button.grid(row=3,pady=10, rowspan=2, column=1, columnspan= 3)

Guess_button = Button(root, text= "Guess a letter!", command = guess_letter)
Guess_word_Button = Button(root, text = "Guess The Word!", command = guess_word)

Error_label = Label(root, text="Guess a Letter or a word ")

letters_guessed_label= Label(root,text="")
letters_guessed_title_label =Label( root, text =" Letters guessed:")

my_pic=Image.open(r'C:\Users\Daniel\PycharmProjects\pythonProject\Hangman_game\TikiMan1HB.png')

resized =my_pic.resize((50, 80),Image.ANTIALIAS)

new_pic = ImageTk.PhotoImage(resized)

my_label =Label(root, image=new_pic)


#play_again_button = Button(root, text= "play again", command= page_reset)




root.mainloop()
