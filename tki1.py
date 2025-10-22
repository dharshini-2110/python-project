import tkinter as tk
from tkinter import messagebox
import random
import time

class TypingGame:
    def __init__(self, master):
        self.master = master
        master.title("Typing Speed Test")
        master.geometry("800x500")
        master.config(bg="#ADD8E6")  

        self.words = ["python", "tkinter", "programming", "challenge", "keyboard", 
                      "application", "interface", "developer", "coding", "accuracy"]
        self.current_word = ""
        self.score = 0
        self.time_left = 60  
        self.game_started = False

    
        self.title_label = tk.Label(master, text="Typing Speed Test", font=("Arial", 30, "bold"), bg="#ADD8E6")
        self.title_label.pack(pady=20)

        self.word_label = tk.Label(master, text="", font=("Arial", 28), bg="#ADD8E6")
        self.word_label.pack(pady=20)

        self.entry_box = tk.Entry(master, font=("Arial", 24), width=30, justify="center")
        self.entry_box.pack(pady=10)
        self.entry_box.bind("<Return>", self.check_word) 

        self.score_label = tk.Label(master, text=f"Score: {self.score}", font=("Arial", 20), bg="#ADD8E6")
        self.score_label.pack(pady=5)

        self.timer_label = tk.Label(master, text=f"Time: {self.time_left}", font=("Arial", 20), bg="#ADD8E6")
        self.timer_label.pack(pady=5)

        self.start_button = tk.Button(master, text="Start Game", font=("Arial", 18), command=self.start_game)
        self.start_button.pack(pady=20)

        self.reset_button = tk.Button(master, text="Reset Game", font=("Arial", 18), command=self.reset_game, state=tk.DISABLED)
        self.reset_button.pack(pady=10)

    def start_game(self):
        if not self.game_started:
            self.game_started = True
            self.score = 0
            self.time_left = 60
            self.score_label.config(text=f"Score: {self.score}")
            self.timer_label.config(text=f"Time: {self.time_left}")
            self.entry_box.config(state=tk.NORMAL)
            self.entry_box.focus_set()
            self.start_button.config(state=tk.DISABLED)
            self.reset_button.config(state=tk.NORMAL)
            self.next_word()
            self.countdown()

    def next_word(self):
        self.current_word = random.choice(self.words)
        self.word_label.config(text=self.current_word)
        self.entry_box.delete(0, tk.END)

    def check_word(self, event=None):
        if self.game_started:
            typed_word = self.entry_box.get().strip()
            if typed_word == self.current_word:
                self.score += 1
                self.score_label.config(text=f"Score: {self.score}")
            self.next_word()

    def countdown(self):
        if self.time_left > 0 and self.game_started:
            self.time_left -= 1
            self.timer_label.config(text=f"Time: {self.time_left}")
            self.master.after(1000, self.countdown)
        elif self.game_started:
            self.end_game()

    def end_game(self):
        self.game_started = False
        self.word_label.config(text="Game Over!")
        self.entry_box.config(state=tk.DISABLED)
        self.start_button.config(state=tk.NORMAL)
        self.reset_button.config(state=tk.DISABLED)
        tk.messagebox.showinfo("Game Over", f"Your final score is: {self.score}")

    def reset_game(self):
        self.game_started = False
        self.score = 0
        self.time_left = 60
        self.score_label.config(text=f"Score: {self.score}")
        self.timer_label.config(text=f"Time: {self.time_left}")
        self.word_label.config(text="")
        self.entry_box.delete(0, tk.END)
        self.entry_box.config(state=tk.NORMAL)
        self.start_button.config(state=tk.NORMAL)
        self.reset_button.config(state=tk.DISABLED)


if __name__ == "__main__":
    root = tk.Tk()
    game = TypingGame(root)
    root.mainloop()
