import tkinter as tk
from tkinter import messagebox
import random
import time

questions_1 = [
    {"question": "125 - (36 × 2) + 17 = ?", "answer": "70", "points": 2},
    {"question": "(8 × 7) - (56 ÷ 8) + 12 = ?", "answer": "61", "points": 2},
    {"question":"Izračunaj razliku broja 385 i zbira brojeva 67 i 42.", "answer":"276", "points":2},
    {"question":"4 × (5 + 3) - 18 ÷ 2 = ?", "answer":"23", "points":2},
    {"question":"(12 × 4) - (8 × 5) + (6 × 3)? ", "answer":"26", "points":2},
    {"question":"Ako saberemo 45 i 78, a zatim oduzmemo 32, koliki je rezultat?", "answer":"91", "points":2},
    {"question":"Koliki je zbir prvih pet prirodnih brojeva?", "answer":"15", "points":2},
]

questions_2 = [
    {"question": "(5² + 4²) ÷ √81 = ?", "answer": "41/9", "points": 3},
    {"question": "Koji broj treba kvadrirati da bi se dobilo 225?", "answer": "15", "points": 3},
    {"question":"Ako je √196 = x, izračunaj vrijednost izraza 3x - 2.", "answer":"40", "points":3},
    {"question":"Koji je kvadrat broja √50 izražen u decimalnom obliku sa 2 decimale?", "answer":"50.00", "points":3},
    {"question":"Riješi: √(x + 16) = 6. Koji je broj x?", "answer":"20", "points":3},
    {"question":"Ako je (3x)² = 144, kolika je vrijednost x?", "answer":"4", "points":3},
    {"question":"Koji je rezultat izraza: √(49 × 16) + 2³?", "answer":"36", "points":3},
]

questions_3 = [
    {"question": "cos(60°) = ?", "answer": "1/2", "points": 4},
    {"question": "tan(45°) + cos(360°) = ?", "answer": "2", "points": 4},
    {"question":"sin(180°) : cos(30°) = ?", "answer":"0", "points":4},
    {"question":"sin(90°) × cos(360°) = ?", "answer":"1", "points":4},
    {"question":"Nađi vrijednost izraza sin(30°) × cos(60°) + 1.25 ", "answer":"1.5", "points":4},
]

questions_4 = [
    {"question": "Riješi jednačinu: 3x - 5 = -2x", "answer": "1", "points": 5},
    {"question": "Riješi jednačinu: x² + 2x – 35 = 0", "answer": "-7,5", "points": 5},
    {"question":"Riješi jednačinu: 3x**4 + 2x**3 + x**2 + 2x – 35 = 3x**4 + 2x**3  ", "answer":"-7,5", "points":5},
]

all_questions = questions_1 + questions_2 + questions_3 + questions_4

root = tk.Tk()
root.title("Matematički Kviz")
root.geometry("400x300")
root.configure(bg="brown")

score = 0
question_index = 0
time_limit = 45
attempts = 0 

questions = random.sample(all_questions, 11)

def start_screen():
    global title_label, start_button
    title_label = tk.Label(root, text="Matematički kviz :)", font=("Courier New", 20), bg="brown", fg="yellow")
    title_label.place(relx=0.5, rely=0.3, anchor="center")

    start_button = tk.Button(root, text="START", font=("Courier New", 16), bg="white", fg="green", command=start_quiz)
    start_button.place(relx=0.5, rely=0.5, anchor="center")

def start_quiz():
    global start_time
    start_time = time.time()
    show_question()

def show_question():
    global question_index, start_time, attempts, score

    for widget in root.winfo_children():
        widget.destroy()

    if question_index >= len(questions):
        end_screen() 
        return

    question = questions[question_index]

    timer_label = tk.Label(root, text=f"PREOSTALO VRIJEME: {time_limit}s", font=("Courier New", 12), bg="brown", fg="white")
    timer_label.place(relx=0.05, rely=0.05, anchor="w")

    difficulty_label = tk.Label(root, text=f"TEŽINA: {question['points']}", font=("Courier New", 12), bg="brown", fg="white")
    difficulty_label.place(relx=0.95, rely=0.05, anchor="e")

    question_label = tk.Label(root, text=question["question"], font=("Courier New", 16), bg="brown", fg="yellow")
    question_label.place(relx=0.5, rely=0.3, anchor="center")

    feedback_label = tk.Label(root, text="", font=("Courier New", 12), bg="brown", fg="white")
    feedback_label.place(relx=0.5, rely=0.4, anchor="center")

    answer_entry = tk.Entry(root, font=("Courier New", 14))
    answer_entry.place(relx=0.5, rely=0.5, anchor="center")

    submit_button = tk.Button(root, text="SUBMIT", font=("Courier New", 12), command=lambda: check_answer(answer_entry, question, feedback_label))
    submit_button.place(relx=0.5, rely=0.6, anchor="center")

    update_timer(timer_label, feedback_label)

def update_timer(timer_label, feedback_label):
    global start_time, time_limit

    elapsed_time = int(time.time() - start_time)
    remaining_time = time_limit - elapsed_time

    if remaining_time <= 0:
        feedback_label.config(text="Time's up!", fg="red")
        root.after(2000, next_question)
    else:
        timer_label.config(text=f"PREOSTALO VRIJEME: {remaining_time}s")
        root.after(1000, lambda: update_timer(timer_label, feedback_label))

def check_answer(answer_entry, question, feedback_label):
    global attempts, score, time_limit

    user_answer = answer_entry.get().strip()

    if attempts < 3:
        if user_answer == question["answer"]:
            feedback_label.config(text="Correct answer!", fg="green")
            score += question["points"]
            attempts = 0 
            root.after(2000, next_question)
        else:
            feedback_label.config(text="Wrong answer. Try again!", fg="red")
            attempts += 1
            time_limit = 45  
    else:
        feedback_label.config(text=f"The correct answer is {question['answer']}", fg="red")
        if attempts == 3:
            score -= 1  
        root.after(2000, next_question)

def next_question():
    global question_index, attempts, start_time
    question_index += 1
    attempts = 0  
    start_time = time.time()
    show_question()

def end_screen():
    for widget in root.winfo_children():
        widget.destroy()  

    end_label = tk.Label(root, text="KRAJ!", font=("Courier New", 24), bg="brown", fg="yellow")
    end_label.place(relx=0.5, rely=0.3, anchor="center")

    score_label = tk.Label(root, text=f"UKUPNO OSVOJENIH BODOVA: {score}", font=("Courier New", 16), bg="brown", fg="white")
    score_label.place(relx=0.5, rely=0.5, anchor="center")

start_screen()

root.mainloop()
