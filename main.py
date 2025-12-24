import tkinter as tk
import math
from tkinter import messagebox

#GAME VARIABLES
lower=0
upper=0
guess=0
attempts=0
max_attempts=0

#COLORS
BG = "#1e1e1e"
FG = "#ffffff"
BTN = "#3a3a3a"
ACCENT = "#4CAF50"

window=tk.Tk()
window.title("Computer Guessing Game")
window.geometry("400x300")
window.configure(bg=BG)



title=tk.Label(window,text="Computer Guessing Game",font="Helvetica 16 bold")
title.config(bg=BG,fg=ACCENT)
title.pack(pady=10)

top_frame=tk.Frame(window , bd=2, relief="solid")
top_frame.configure(bg=BG)
top_frame.pack(pady=10)

middle_frame=tk.Frame(window)
middle_frame.configure(bg=BG)
middle_frame.pack(pady=10)

bottom_frame=tk.Frame(window)
bottom_frame.configure(bg=BG)
bottom_frame.pack(pady=10)

#TOP FRAME
tk.Label(top_frame,text="Lower:").grid(row=0,column=0,padx=5)
entry_lower=tk.Entry(top_frame,width=10)
entry_lower.configure(bg=BTN,fg=FG,insertbackground=FG)
entry_lower.grid(row=0,column=1)

tk.Label(top_frame,text="Upper:").grid(row=0,column=2,padx=5)
entry_upper=tk.Entry(top_frame,width=10)
entry_upper.configure(bg=BTN,fg=FG,insertbackground=FG)
entry_upper.grid(row=0,column=3)

#MIDDLE FRAME(INFO)
info_label=tk.Label(middle_frame,text="Enter rage and start the game!",font="helvetica 12",fg="white")
info_label.config(bg=BG,fg=FG)
info_label.pack()

attempt_label=tk.Label(middle_frame,text="Attempts: 0 / -",font="helvetica 11",fg="white",bg=BG)
attempt_label.pack(pady=5)

#FUNCTIONS
def start_game():
    global lower,upper,attempts,max_attempts,guess
    try:
        if not entry_lower.get() or not entry_upper.get():
            info_label.config(text="❌ Please fill both fields")
            return
        
        lower=int(entry_lower.get())
        upper=int(entry_upper.get())

        if lower>=upper:
            info_label.config(text="❌ Invalid range! Lower must be less than Upper.",fg="red")
            return
        info_label.config(text="✅ Started successfully")
        print("Range:", lower, upper)

        attempts=0
        max_attempts=math.ceil(math.log2(upper-lower+1))

        guess=(lower+upper)//2
        info_label.config(text=f"My guess is: {guess}",fg="white")

        attempt_label.config(text=f"Attempts:{attempts}/{max_attempts}",fg="white")

    except ValueError:
        info_label.config(text="❌ Please enter valid numbers",fg="red")    
 

def give_feedback(feedback):
    global lower, upper,guess,attempts

    attempts+=1
    attempt_label.config(text=f"Attempts:{attempts}/{max_attempts}",fg="white")
    if attempts>max_attempts:
        info_label.config(text="❌ Exceeded maximum attempts!",fg="red")
        return
    
    if feedback=='c':
        info_label.config(text=f"🎉 I found it in {attempts} attempts!",fg="green")
        return
    elif feedback=='l':
        lower=guess+1
    elif feedback=='h':
        upper=guess-1

    if attempts>=max_attempts-1:
        attempt_label.config(fg="orange")
    else:
        attempt_label.config(fg="white")      

    if lower>upper:
        messagebox.showerror("Cheating Detected!",
        "Inconsistent answers detected.\nWere you honest?")
        restart_game()
        return
    
    guess=(lower+upper)//2
    info_label.config(text=f"My guess is:{guess}",fg="white")   

def restart_game():
    global upper, lower, guess,attempts,max_attempts
    lower=0
    upper=0
    guess=0
    attempts=0
    max_attempts=0   

    entry_lower.delete(0,tk.END)
    entry_upper.delete(0,tk.END)


    info_label.config(text="Game reset!Enter new range.",fg="white")
    attempt_label.config(text="Attempts: 0/ -")


#BUTTONS

tk.Button(bottom_frame,text="Start",bg=BTN,fg=FG,activebackground=ACCENT,command=start_game,width=12).grid(row=0,column=0,padx=5)
tk.Button(bottom_frame,text="Too Low",bg=BTN,fg=FG,activebackground=ACCENT,command=lambda:give_feedback('l'),width=12).grid(row=0,column=1,padx=5)
tk.Button(bottom_frame,text="Too High",bg=BTN,fg=FG,activebackground=ACCENT,command=lambda:give_feedback('h'),width=12).grid(row=0,column=2,padx=5)
tk.Button(bottom_frame,text="Correct",bg=BTN,fg=FG,activebackground=ACCENT,command=lambda:give_feedback('c'),width=12).grid(row=0,column=3,padx=5)
tk.Button(bottom_frame,text="Restart",bg=BTN,fg=FG,activebackground=ACCENT,command=restart_game,width=12).grid(row=1,column=0,columnspan=4,pady=5)

#main loop
window.mainloop()