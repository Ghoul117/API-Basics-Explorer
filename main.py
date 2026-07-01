import tkinter as tk

from pages import (
    show_home,
    show_api_page,
    show_request_page,
    show_json_page,
    show_key_page,
)

from demo import open_demo
from quiz import open_quiz


# ==========================================
# Main Window
# ==========================================

root = tk.Tk()
root.title("🌐 API Basics Explorer")
root.geometry("1100x700")
root.minsize(1100, 700)
root.configure(bg="#202124")


# ==========================================
# Header
# ==========================================

header = tk.Frame(root, bg="#1B1C1D", height=60)
header.pack(fill="x")

title = tk.Label(
    header,
    text="🌐 API Basics Explorer",
    bg="#1B1C1D",
    fg="white",
    font=("Segoe UI", 22, "bold")
)
title.pack(side="left", padx=20)

version = tk.Label(
    header,
    text="Version 1.0",
    bg="#1B1C1D",
    fg="#BBBBBB",
    font=("Segoe UI", 10)
)
version.pack(side="right", padx=20)


# ==========================================
# Main Layout
# ==========================================

main = tk.Frame(root, bg="#202124")
main.pack(fill="both", expand=True)


# ==========================================
# Sidebar
# ==========================================

sidebar = tk.Frame(
    main,
    bg="#2B2B2B",
    width=260
)

sidebar.pack(side="left", fill="y")
sidebar.pack_propagate(False)


# ==========================================
# Scrollable Content Area
# ==========================================

content_container = tk.Frame(main, bg="#303134")
content_container.pack(side="right", fill="both", expand=True)

canvas = tk.Canvas(
    content_container,
    bg="#303134",
    highlightthickness=0
)

scrollbar = tk.Scrollbar(
    content_container,
    orient="vertical",
    command=canvas.yview
)

content = tk.Frame(
    canvas,
    bg="#303134"
)

content.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window(
    (0, 0),
    window=content,
    anchor="nw"
)

canvas.configure(
    yscrollcommand=scrollbar.set
)

canvas.pack(
    side="left",
    fill="both",
    expand=True
)

scrollbar.pack(
    side="right",
    fill="y"
)


# Windows / Wayland
def on_mousewheel(event):
    if event.delta:
        canvas.yview_scroll(int(-event.delta / 120), "units")

# Linux X11
def on_linux_scroll(event):
    if event.num == 4:
        canvas.yview_scroll(-1, "units")
    elif event.num == 5:
        canvas.yview_scroll(1, "units")


canvas.bind_all("<MouseWheel>", on_mousewheel)
canvas.bind_all("<Button-4>", on_linux_scroll)
canvas.bind_all("<Button-5>", on_linux_scroll)

# ==========================================
# Footer
# ==========================================

footer = tk.Frame(root, bg="#1B1C1D", height=28)
footer.pack(fill="x")

status = tk.Label(
    footer,
    text="Made with ❤️ using Python & Tkinter",
    bg="#1B1C1D",
    fg="#BBBBBB",
    font=("Segoe UI", 9)
)

status.pack(side="left", padx=10)


# ==========================================
# Navigation Button
# ==========================================

current_button = None


def nav_button(text, command):

    btn = tk.Button(
        sidebar,
        text=text,
        bg="#2B2B2B",
        fg="white",
        activebackground="#4F8EF7",
        activeforeground="white",
        relief="flat",
        bd=0,
        anchor="w",
        padx=20,
        pady=12,
        font=("Segoe UI", 11),
        cursor="hand2"
    )

    def on_click():
        global current_button

        if current_button:
            current_button.config(bg="#2B2B2B")

        btn.config(bg="#4F8EF7")
        current_button = btn

        command(content)

    btn.config(command=on_click)

    def enter(e):
        if btn != current_button:
            btn.config(bg="#3C4043")

    def leave(e):
        if btn != current_button:
            btn.config(bg="#2B2B2B")

    btn.bind("<Enter>", enter)
    btn.bind("<Leave>", leave)

    return btn


# ==========================================
# Sidebar Buttons
# ==========================================

home_btn = nav_button("🏠  Home", show_home)
home_btn.pack(fill="x")

api_btn = nav_button("📡  What is an API?", show_api_page)
api_btn.pack(fill="x")

request_btn = nav_button("🔄  Request & Response", show_request_page)
request_btn.pack(fill="x")

json_btn = nav_button("📦  JSON Basics", show_json_page)
json_btn.pack(fill="x")

key_btn = nav_button("🔑  API Keys", show_key_page)
key_btn.pack(fill="x")

demo_btn = nav_button("🌍  Live API Demo", open_demo)
demo_btn.pack(fill="x")

quiz_btn = nav_button("❓  Quiz", open_quiz)
quiz_btn.pack(fill="x")


# ==========================================
# Default Page
# ==========================================

current_button = home_btn
home_btn.config(bg="#4F8EF7")

show_home(content)


# ==========================================
# Run App
# ==========================================

root.mainloop()