import tkinter as tk
import requests


def open_demo(content):

    # ---------------------------------------
    # Clear existing page
    # ---------------------------------------

    for widget in content.winfo_children():
        widget.destroy()

    # ---------------------------------------
    # Title
    # ---------------------------------------

    tk.Label(
        content,
        text="🌍 Live API Demonstration",
        font=("Segoe UI", 24, "bold"),
        bg="#303134",
        fg="white"
    ).pack(pady=20)

    tk.Label(
        content,
        text="This page makes a REAL request to GitHub's public API.",
        font=("Segoe UI", 12),
        bg="#303134",
        fg="#DDDDDD"
    ).pack(pady=5)

    # ---------------------------------------
    # Card
    # ---------------------------------------

    card = tk.Frame(
        content,
        bg="#3C4043",
        padx=25,
        pady=20
    )

    card.pack(fill="x", padx=30, pady=20)

    # ---------------------------------------
    # Username Entry
    # ---------------------------------------

    tk.Label(
        card,
        text="GitHub Username",
        bg="#3C4043",
        fg="white",
        font=("Segoe UI", 12, "bold")
    ).pack(anchor="w")

    username = tk.Entry(
        card,
        font=("Segoe UI", 12),
        width=30
    )

    username.insert(0, "octocat")
    username.pack(anchor="w", pady=10)

    # ---------------------------------------
    # Output Box
    # ---------------------------------------

    output = tk.Text(
        content,
        width=90,
        height=18,
        bg="#202124",
        fg="white",
        font=("Consolas", 11)
    )

    output.pack(padx=20, pady=15)

    # ---------------------------------------
    # API Function
    # ---------------------------------------

    def fetch():

        output.delete("1.0", tk.END)

        user = username.get().strip()

        if user == "":
            output.insert(tk.END, "Please enter a GitHub username.")
            return

        url = f"https://api.github.com/users/{user}"

        output.insert(
            tk.END,
            "Sending GET Request...\n\n"
        )

        try:

            response = requests.get(url)

            output.insert(
                tk.END,
                f"Request URL:\n{url}\n\n"
            )

            output.insert(
                tk.END,
                f"Status Code : {response.status_code}\n\n"
            )

            if response.status_code != 200:

                output.insert(
                    tk.END,
                    "User not found."
                )

                return

            data = response.json()

            output.insert(
                tk.END,
                "Response Received Successfully!\n\n"
            )

            output.insert(
                tk.END,
                f"Username      : {data['login']}\n"
            )

            output.insert(
                tk.END,
                f"Name          : {data['name']}\n"
            )

            output.insert(
                tk.END,
                f"Followers     : {data['followers']}\n"
            )

            output.insert(
                tk.END,
                f"Following     : {data['following']}\n"
            )

            output.insert(
                tk.END,
                f"Public Repos  : {data['public_repos']}\n"
            )

            output.insert(
                tk.END,
                f"Location      : {data['location']}\n"
            )

            output.insert(
                tk.END,
                f"Company       : {data['company']}\n"
            )

            output.insert(
                tk.END,
                f"Profile URL   : {data['html_url']}\n"
            )

            output.insert(
                tk.END,
                "\n\n--------------------------------------\n"
            )

            output.insert(
                tk.END,
                "What just happened?\n\n"
            )

            output.insert(
                tk.END,
                "1. Your application created a GET request.\n"
            )

            output.insert(
                tk.END,
                "2. GitHub's API received it.\n"
            )

            output.insert(
                tk.END,
                "3. GitHub searched its database.\n"
            )

            output.insert(
                tk.END,
                "4. GitHub returned data in JSON format.\n"
            )

            output.insert(
                tk.END,
                "5. Python converted that JSON into a dictionary.\n"
            )

            output.insert(
                tk.END,
                "6. The application displayed the information.\n"
            )

        except Exception as e:

            output.insert(
                tk.END,
                f"Error:\n{e}"
            )

    # ---------------------------------------
    # Button
    # ---------------------------------------

    tk.Button(
        card,
        text="🚀 Send API Request",
        command=fetch,
        bg="#4F8EF7",
        fg="white",
        relief="flat",
        padx=20,
        pady=8,
        font=("Segoe UI", 11, "bold"),
        cursor="hand2"
    ).pack(anchor="w", pady=10)