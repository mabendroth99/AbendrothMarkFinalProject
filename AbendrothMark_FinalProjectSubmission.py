#Mark Abendroth Final Project Submission
#The purpose of this program is to generate a random password for the user, based on how long the user would like for it to be, and to display it in a seperate pop-up window

#imports neccesary modules for generating password, GUI, and images
import random
import string
import tkinter as tk
from tkinter import PhotoImage
from tkinter import messagebox

#defines a function for generating the password
def generate_password(length):
  # generate a random password with the given length
  password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))
  return password

#function that opens a window for the user to enter the desired length
def open_password_window():
  # create a new window for generating a password
  password_window = tk.Toplevel()
  password_window.title("Generate Password")
  password_window.geometry("300x300")

  # create a label and entry field for the password length
  length_label = tk.Label(password_window, text="Password length:")
  length_entry = tk.Entry(password_window)

  # create a button to call the function to generate the password
  generate_button = tk.Button(password_window, text="Generate", command=lambda: generate_password_callback(length_entry))

  # add the widgets to the window
  length_label.pack()
  length_entry.pack()
  generate_button.pack()
  
#defines a function that
def generate_password_callback(length_entry):
  try:
    # get the password length from the entry field
    length = int(length_entry.get())
  except ValueError:
    # display an error message if the user enters a string
    tk.messagebox.showerror("Error", "Please enter a number")
    return

  # generate the password
  password = generate_password(length)

  # create a new window to display the password
  password_popup = tk.Toplevel()
  password_popup.title("Password")
  password_popup.geometry("200x200")

  # display the text "Your password is: "
  password_text = tk.Label(password_popup, text="Your password is: ")
  password_text.pack()

  # display the password in a label
  password_label = tk.Label(password_popup, text=password)
  password_label.pack()

  # create a button to generate a new password
  new_password_button = tk.Button(password_popup, text="New password", command=lambda: update_password_label(password_label, length))
  new_password_button.pack()


#defines a function that allows the user to click a button that will automatically display a new password
def update_password_label(label, length):
  # generate a new password
  new_password = generate_password(length)

  # update the label text
  label.config(text=new_password)


#defines the main module
def main():
  # create the main window
  root = tk.Tk()
  root.title("Password Generator")
  root.geometry("500x300")

  # Creates a PhotoImage object for the picture
  image = PhotoImage(file="HelloPanda.png")
  label = tk.Label(root, image=image)
  label.pack()

  # create a button to open the password window
  password_button = tk.Button(root, text="Generate Password", command=open_password_window)
  password_button.pack()

  # create a button to exit the program
  exit_button = tk.Button(root, text="Exit", command=root.destroy)
  exit_button.pack()

  # start the main loop
  tk.mainloop()

if __name__ == "__main__":
  main()
