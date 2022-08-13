from tkinter import *
import requests
import html
import pandas as pd
import json

BACKGROUND = "#375362"
TITLE = "TriviaApp v1.0"
AMOUNT = 1
TYPE = "boolean"
WRONG_BUTTON = "./images/false.png"
TRUE_BUTTON = "./images/true.png"
BACK_BUTTON = "./images/back.png"
QUIT_BUTTON = "./images/quit.png"
DELAY = 1500


class QuizUI:
    def __init__(self):
        self.ani = None
        self.ani_button = None
        self.ani_label = None
        self.art_label = None
        self.art_button = None
        self.art = None
        self.geo_label = None
        self.geo_button = None
        self.geo = None
        self.hst_label = None
        self.hst = None
        self.hst_button = None
        self.snn_label = None
        self.snn_button = None
        self.snn = None
        self.gk_label = None
        self.gk_button = None
        self.gk = None
        self.choice_window_label = None
        self.choice_window = Tk()
        self.choice_window.config(padx=50, pady=50, background=BACKGROUND)
        self.choice_window.title(TITLE)
        self.canvas_choice = Canvas(width=50, height=50, bg=BACKGROUND, highlightthickness=0)
        self.main_menu()
        self.choice_window.mainloop()

    def main_menu(self):
        self.choice_window_label = Label(text="Please Select The Trivia Category", background=BACKGROUND,
                                         foreground="white")
        self.choice_window_label.config(font=("Times New Roman", 25, "bold"), padx=25, pady=25)
        self.choice_window_label.grid(row=0, column=1)

        self.gk = PhotoImage(file="./images/gk.png")
        self.gk_button = Button(image=self.gk, command=self.select_category_gk)
        self.gk_button.config(highlightthickness=0, background=BACKGROUND, pady=25, padx=25, width=100, height=100)
        self.gk_button.grid(row=1, column=0)
        self.gk_label = Label(text="General Knowledge", font=("Ariel", 10, "bold"), background=BACKGROUND,
                              foreground="white")
        self.gk_label.grid(row=2, column=0)

        self.snn = PhotoImage(file="./images/snn.png")
        self.snn_button = Button(image=self.snn, command=self.select_category_snn)
        self.snn_button.config(highlightthickness=0, background=BACKGROUND, pady=25, padx=25, height=100, width=100)
        self.snn_button.grid(row=1, column=1)
        self.snn_label = Label(text="Science & Nature", font=("Ariel", 10, "bold"), background=BACKGROUND,
                               foreground="white")
        self.snn_label.grid(row=2, column=1)

        self.hst = PhotoImage(file="./images/hst.png")
        self.hst_button = Button(image=self.hst, command=self.select_category_hst)
        self.hst_button.config(highlightthickness=0, background=BACKGROUND, pady=25, padx=25, height=100, width=100)
        self.hst_button.grid(row=1, column=2)
        self.hst_label = Label(text="History", font=("Ariel", 10, "bold"), background=BACKGROUND,
                               foreground="white")
        self.hst_label.grid(row=2, column=2)

        self.geo = PhotoImage(file="./images/geo.png")
        self.geo_button = Button(image=self.geo, command=self.select_category_geo)
        self.geo_button.config(highlightthickness=0, background=BACKGROUND, pady=25, padx=25, height=100, width=100)
        self.geo_button.grid(row=3, column=0)
        self.geo_label = Label(text="Geography", font=("Ariel", 10, "bold"), background=BACKGROUND,
                               foreground="white")
        self.geo_label.grid(row=4, column=0)

        self.art = PhotoImage(file="./images/art.png")
        self.art_button = Button(image=self.art, command=self.select_category_art)
        self.art_button.config(highlightthickness=0, background=BACKGROUND, pady=25, padx=25, height=100, width=100)
        self.art_button.grid(row=3, column=1)
        self.art_label = Label(text="Art", font=("Ariel", 10, "bold"), background=BACKGROUND,
                               foreground="white")
        self.art_label.grid(row=4, column=1)

        self.ani = PhotoImage(file="./images/animals.png")
        self.ani_button = Button(image=self.ani, command=self.select_category_ani)
        self.ani_button.config(highlightthickness=0, background=BACKGROUND, pady=25, padx=25, height=100, width=100)
        self.ani_button.grid(row=3, column=2)
        self.ani_label = Label(text="Animals", font=("Ariel", 10, "bold"), background=BACKGROUND,
                               foreground="white")
        self.ani_label.grid(row=4, column=2)

    def select_category_gk(self):
        self.choice_window.destroy()
        GetData(category=9)

    def select_category_snn(self):
        self.choice_window.destroy()
        GetData(category=17)

    def select_category_art(self):
        self.choice_window.destroy()
        GetData(category=25)

    def select_category_ani(self):
        self.choice_window.destroy()
        GetData(category=27)

    def select_category_hst(self):
        self.choice_window.destroy()
        GetData(category=23)

    def select_category_geo(self):
        self.choice_window.destroy()
        GetData(category=22)


class GetData:
    def __init__(self, category: int):
        self.parameters = None
        self.category = category
        self.data = self.get_questions(category)
        self.score = 0
        self.high_score = 0
        self.window = Tk()
        self.window.title(f"{TITLE} ({self.data[0]['category']})")
        self.window.config(background=BACKGROUND)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, text=self.data[0]['question'],
                                                     width=280,
                                                     fill=BACKGROUND,
                                                     font=("Ariel", 15, "italic"))
        self.canvas.grid(row=1, column=0, pady=25, padx=25, columnspan=3)

        self.score_label = Label(text=f"Score: {self.score}/{self.high_score}",
                                 font=("Ariel", 15, "bold"),
                                 background=BACKGROUND,
                                 foreground="white")
        self.score_label.grid(row=0, column=1)

        false_icon = PhotoImage(file=WRONG_BUTTON)
        false_button = Button(image=false_icon, command=self.false)
        false_button.config(highlightthickness=0, background=BACKGROUND)
        false_button.grid(row=2, column=0, pady=25, padx=25)

        true_icon = PhotoImage(file=TRUE_BUTTON)
        true_button = Button(image=true_icon, command=self.true)
        true_button.config(highlightthickness=0, background=BACKGROUND)
        true_button.grid(row=2, column=2, pady=25, padx=25)

        back_icon = PhotoImage(file=BACK_BUTTON)
        back_button = Button(image=back_icon, command=self.back)
        back_button.config(highlightthickness=0, background=BACKGROUND)
        back_button.grid(row=0, column=0, pady=25, padx=25)

        quit_icon = PhotoImage(file=QUIT_BUTTON)
        quit_button = Button(image=quit_icon, command=self.quit)
        quit_button.config(highlightthickness=0, background=BACKGROUND)
        quit_button.grid(row=0, column=2, pady=25, padx=25)

        self.window.mainloop()

    def false(self):
        if self.data[0]["correct_answer"] == "False":
            self.data = self.get_questions(self.category)
            self.canvas.config(bg="#DAF7A6")
            self.window.after(DELAY, self.change_question)
            self.score += 1
            if self.score > self.high_score:
                self.high_score = self.score
            self.score_label.config(text=f"Score: {self.score}/{self.high_score}")
        else:
            self.data = self.get_questions(self.category)
            self.canvas.config(bg="#D56262")
            self.score = 0
            self.score_label.config(text=f"Score: {self.score}/{self.high_score}")
            self.window.after(DELAY, self.change_question)

    def true(self):
        if self.data[0]["correct_answer"] == "True":
            self.data = self.get_questions(self.category)
            self.canvas.config(bg="#DAF7A6")
            self.window.after(DELAY, self.change_question)
            self.score += 1
            if self.score > self.high_score:
                self.high_score = self.score
            self.score_label.config(text=f"Score: {self.score}/{self.high_score}")
        else:
            self.data = self.get_questions(self.category)
            self.canvas.config(bg="#D56262")
            self.score = 0
            self.score_label.config(text=f"Score: {self.score}/{self.high_score}")
            self.window.after(DELAY, self.change_question)

    def back(self):
        self.window.destroy()
        QuizUI()

    def quit(self):
        self.window.quit()
        self.window.destroy()

    def get_questions(self, cat):
        self.parameters = {
            "amount": AMOUNT,
            "category": cat,
            "type": TYPE,
        }
        response = requests.get(f"https://opentdb.com/api.php", params=self.parameters)
        response.raise_for_status()
        data = response.json()['results']
        data[0]['question'] = html.unescape(data[0]['question'])
        return data

    def change_question(self):
        # print(self.data)
        self.canvas.config(bg="white")
        self.canvas.itemconfig(self.question_text, text=self.data[0]['question'])
