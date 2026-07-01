import tkinter as tk


def open_quiz(content):

    # ------------------------------
    # Clear Previous Page
    # ------------------------------

    for widget in content.winfo_children():
        widget.destroy()

    # ------------------------------
    # Quiz Questions
    # ------------------------------

    questions = [

        {
            "question": "1. What does API stand for?",
            "options": [
                "Application Programming Interface",
                "Automatic Program Internet",
                "Application Private Internet",
                "Advanced Programming Input"
            ],
            "answer": 0
        },

        {
            "question": "2. Which component acts as the messenger between an app and a server?",
            "options": [
                "Database",
                "API",
                "Python",
                "Browser"
            ],
            "answer": 1
        },

        {
            "question": "3. Which HTTP method is usually used to retrieve data?",
            "options": [
                "POST",
                "PUT",
                "GET",
                "DELETE"
            ],
            "answer": 2
        },

        {
            "question": "4. JSON is mainly used for...",
            "options": [
                "Editing videos",
                "Sharing structured data",
                "Creating images",
                "Playing games"
            ],
            "answer": 1
        },

        {
            "question": "5. Should you upload your API Key to GitHub?",
            "options": [
                "Yes",
                "Only sometimes",
                "No",
                "Only if the repository is public"
            ],
            "answer": 2
        }

    ]

    current_question = 0
    score = 0

    # ------------------------------
    # Title
    # ------------------------------

    title = tk.Label(
        content,
        text="❓ API Basics Quiz",
        font=("Segoe UI", 24, "bold"),
        bg="#303134",
        fg="white"
    )

    title.pack(pady=20)

    progress = tk.Label(
        content,
        text="",
        font=("Segoe UI", 11),
        bg="#303134",
        fg="#BBBBBB"
    )

    progress.pack()

    question_label = tk.Label(
        content,
        text="",
        font=("Segoe UI", 16, "bold"),
        wraplength=700,
        justify="left",
        bg="#303134",
        fg="white"
    )

    question_label.pack(pady=25)

    choice = tk.IntVar(value=-1)

    radio_buttons = []

    for i in range(4):

        rb = tk.Radiobutton(
            content,
            text="",
            variable=choice,
            value=i,
            bg="#303134",
            fg="white",
            activebackground="#303134",
            activeforeground="white",
            selectcolor="#3C4043",
            font=("Segoe UI", 12),
            justify="left"
        )

        rb.pack(anchor="w", padx=120, pady=6)

        radio_buttons.append(rb)

    feedback = tk.Label(
        content,
        text="",
        bg="#303134",
        fg="yellow",
        font=("Segoe UI", 11)
    )

    feedback.pack(pady=15)

    # ------------------------------
    # Functions
    # ------------------------------

    def load_question():

        q = questions[current_question]

        progress.config(
            text=f"Question {current_question + 1} of {len(questions)}"
        )

        question_label.config(
            text=q["question"]
        )

        choice.set(-1)

        feedback.config(text="")

        for i in range(4):
            radio_buttons[i].config(
                text=q["options"][i]
            )

    def next_question():

        nonlocal current_question
        nonlocal score

        if choice.get() == -1:

            feedback.config(
                text="Please select an answer before continuing."
            )

            return

        if choice.get() == questions[current_question]["answer"]:
            score += 1

        current_question += 1

        if current_question == len(questions):
            show_result()
        else:
            load_question()

    def show_result():

        for widget in content.winfo_children():
            widget.destroy()

        percentage = int((score / len(questions)) * 100)

        tk.Label(
            content,
            text="🎉 Quiz Completed!",
            font=("Segoe UI", 26, "bold"),
            bg="#303134",
            fg="white"
        ).pack(pady=30)

        tk.Label(
            content,
            text=f"You scored\n\n{score} / {len(questions)}",
            font=("Segoe UI", 22),
            bg="#303134",
            fg="#61AFEF"
        ).pack(pady=20)

        tk.Label(
            content,
            text=f"{percentage}% Correct",
            font=("Segoe UI", 18),
            bg="#303134",
            fg="#98C379"
        ).pack()

        if percentage == 100:
            message = "Excellent! You understood all the basics."
        elif percentage >= 80:
            message = "Great job! You have a solid understanding."
        elif percentage >= 60:
            message = "Good! A quick revision will make it perfect."
        else:
            message = "Don't worry. Read the lessons once more and try again."

        tk.Label(
            content,
            text=message,
            wraplength=650,
            justify="center",
            font=("Segoe UI", 13),
            bg="#303134",
            fg="white"
        ).pack(pady=30)

        tk.Button(
            content,
            text="🔄 Restart Quiz",
            command=lambda: open_quiz(content),
            bg="#4F8EF7",
            fg="white",
            relief="flat",
            padx=20,
            pady=10,
            font=("Segoe UI", 11, "bold"),
            cursor="hand2"
        ).pack()

    # ------------------------------
    # Next Button
    # ------------------------------

    tk.Button(
        content,
        text="Next ➜",
        command=next_question,
        bg="#4F8EF7",
        fg="white",
        relief="flat",
        padx=25,
        pady=10,
        font=("Segoe UI", 11, "bold"),
        cursor="hand2"
    ).pack(pady=20)

    load_question()