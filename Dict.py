import tkinter as tk
from tkinter import messagebox
from PyDictionary import PyDictionary

# Initialize PyDictionary
dictionary = PyDictionary()

def search_word():
    input_word = word.get().strip().capitalize()
    try:
        meaning = dictionary.meaning(input_word)
        if meaning:
            meaning_text.config(state=tk.NORMAL)
            meaning_text.delete(1.0, tk.END)
            for part_of_speech, definitions in meaning.items():
                meaning_text.insert(tk.END, f"{part_of_speech.capitalize()}: {'; '.join(definitions)}\n")
            meaning_text.config(state=tk.DISABLED)
        else:
            raise ValueError
    except (KeyError, ValueError):
        messagebox.showerror('Error', 'Word does not exist or no meaning found.')
        word_entry.delete(0, tk.END)

def clear_word():
    meaning_text.config(state=tk.NORMAL)
    word_entry.delete(0, tk.END)
    meaning_text.delete(1.0, tk.END)

def exit_app():
    res = messagebox.askyesno('Confirm', 'Do you want to exit?')
    if res:
        root.destroy()

# Main Tkinter window
root = tk.Tk()
root.geometry('1000x626')
root.title('Dictionary App')
root.resizable(0, 0)

# Background image
bg_image = tk.PhotoImage(file='bg.png')
background_label = tk.Label(root, image=bg_image)
background_label.place(x=0, y=0)

# Labels and Entry
word_label = tk.Label(root, text='Enter word:', font=('Gabriola', 35, 'bold'), fg='red3', bg='whitesmoke')
word_label.place(x=550, y=20)

meaning_label = tk.Label(root, text='Meaning:', font=('Gabriola', 35, 'bold'), fg='red3', bg='whitesmoke')
meaning_label.place(x=550, y=230)

word = tk.StringVar()
word_entry = tk.Entry(root, font=('Gabriola', 23, 'bold'), bd=8, relief=tk.GROOVE, justify=tk.CENTER, textvariable=word)
word_entry.place(x=530, y=100)

# Text area for displaying meaning
meaning_text = tk.Text(root, font=('Gabriola', 18), width=34, height=6, relief=tk.GROOVE, bd=8)
meaning_text.place(x=500, y=310)
meaning_text.config(state=tk.DISABLED)

# Buttons
search_button = tk.Button(root, text='Search', font=('Georgia', 11), bg='pink2', relief=tk.RIDGE, bd=2, command=search_word)
search_button.place(x=625, y=180)

clear_image = tk.PhotoImage(file='clear.png')
clear_button = tk.Button(root, image=clear_image, bd=0, bg='whitesmoke', command=clear_word)
clear_button.place(x=810, y=100)

exit_image = tk.PhotoImage(file='exit.png')
exit_button = tk.Button(root, image=exit_image, bd=0, bg='whitesmoke', command=exit_app)
exit_button.place(x=790, y=555)

root.mainloop()
