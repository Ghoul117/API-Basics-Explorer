import tkinter as tk


# ==========================================================
# Helper Functions
# ==========================================================

def clear(content):
    """Remove everything from the content frame."""
    for widget in content.winfo_children():
        widget.destroy()


def page_title(content, text):
    tk.Label(
        content,
        text=text,
        font=("Segoe UI", 24, "bold"),
        bg="#303134",
        fg="white"
    ).pack(pady=(20, 10))


def subtitle(content, text):
    tk.Label(
        content,
        text=text,
        font=("Segoe UI", 12),
        bg="#303134",
        fg="#CFCFCF",
        wraplength=780,
        justify="center"
    ).pack(pady=(0, 20))


def create_card(content):

    card = tk.Frame(
        content,
        bg="#3C4043",
        padx=25,
        pady=20,
        highlightbackground="#555555",
        highlightthickness=1
    )

    card.pack(
        fill="x",
        padx=30,
        pady=10
    )

    return card


def card_heading(card, text):

    tk.Label(
        card,
        text=text,
        font=("Segoe UI", 16, "bold"),
        bg="#3C4043",
        fg="white",
        anchor="w"
    ).pack(anchor="w", pady=(0, 10))


def card_text(card, text):

    tk.Label(
        card,
        text=text,
        font=("Segoe UI", 11),
        bg="#3C4043",
        fg="#DDDDDD",
        justify="left",
        wraplength=720,
        anchor="w"
    ).pack(anchor="w")


# ==========================================================
# HOME PAGE
# ==========================================================

def show_home(content):

    clear(content)

    page_title(content, "🌐 Welcome to API Basics Explorer")

    subtitle(
        content,
        "Understand APIs visually using simple examples and interactive lessons."
    )

    card = create_card(content)

    card_heading(card, "📚 What you'll learn")

    lessons = [
        "📡  What is an API?",
        "🔄  Request & Response",
        "📦  JSON Basics",
        "🔑  API Keys",
        "🌍  Live API Demonstration",
        "❓  Quiz Yourself"
    ]

    for lesson in lessons:

        tk.Label(
            card,
            text="• " + lesson,
            font=("Segoe UI", 11),
            bg="#3C4043",
            fg="#DDDDDD",
            anchor="w"
        ).pack(anchor="w", pady=2)

    card2 = create_card(content)

    card_heading(card2, "💡 Fun Fact")

    card_text(
        card2,
        "Every day you use dozens of APIs without even realizing it.\n\n"
        "Instagram, YouTube, Spotify, Google Maps, Amazon, WhatsApp "
        "and even ChatGPT all communicate using APIs."
    )

    tk.Label(
        content,
        text="👈 Select a lesson from the sidebar to begin learning.",
        font=("Segoe UI", 12, "italic"),
        bg="#303134",
        fg="#AAAAAA"
    ).pack(pady=20)

    # ==========================================================
# LESSON 1 : WHAT IS AN API?
# ==========================================================

def show_api_page(content):

    clear(content)

    page_title(content, "📡 What is an API?")

    subtitle(
        content,
        "Let's understand APIs from the very beginning using simple real-life examples."
    )

    # ------------------------------------------------------

    card = create_card(content)

    card_heading(card, "❓ Imagine This")

    card_text(
        card,
        "Suppose you open a Weather App on your phone.\n\n"
        "Within a second, it shows:\n\n"
        "🌡 Temperature : 31°C\n"
        "☁ Weather : Cloudy\n\n"
        "Question:\n"
        "How did your phone know today's weather?"
    )

    # ------------------------------------------------------

    card = create_card(content)

    card_heading(card, "🖥 Where is the information stored?")

    card_text(
        card,
        "Your phone does NOT actually know the weather.\n\n"
        "The information is stored on another powerful computer called a SERVER.\n\n"
        "A server stores information and provides services to thousands or even millions of users at the same time."
    )

    # ------------------------------------------------------

    card = create_card(content)

    card_heading(card, "🤔 So how does your phone ask the server?")

    card_text(
        card,
        "Your Weather App needs a way to communicate with the server.\n\n"
        "It cannot directly access the server's database.\n\n"
        "Instead, it sends a REQUEST to something called an API."
    )

    # ------------------------------------------------------

    card = create_card(content)

    card_heading(card, "📚 Definition")

    card_text(
        card,
        "API stands for:\n\n"
        "Application Programming Interface\n\n"
        "In simple words,\n\n"
        "An API is a messenger between two software applications.\n\n"
        "It accepts a request from one application,\n"
        "takes it to another application or server,\n"
        "collects the response,\n"
        "and sends it back."
    )

    # ------------------------------------------------------

    card = create_card(content)

    card_heading(card, "🔄 Visual Flow")

    diagram = """
        👤 YOU

          │

          ▼

     📱 Weather App

          │
      Request

          ▼

      🌐 Weather API

          │

          ▼

     🖥 Weather Server

          │

          ▼

     Weather Data

          │

          ▼

      🌐 Weather API

          │
      Response

          ▼

     📱 Weather App

          │

          ▼

      🌡 31°C
"""

    tk.Label(
        card,
        text=diagram,
        bg="#3C4043",
        fg="#61AFEF",
        font=("Courier New", 12),
        justify="center"
    ).pack()

    # ------------------------------------------------------

    card = create_card(content)

    card_heading(card, "🌍 Real Example")

    card_text(
        card,
        "You search:\n\n"
        "\"Weather in Berlin\"\n\n"
        "↓\n\n"
        "Your Weather App creates a request.\n\n"
        "↓\n\n"
        "The API receives that request.\n\n"
        "↓\n\n"
        "The API asks the Weather Server.\n\n"
        "↓\n\n"
        "The server returns today's weather.\n\n"
        "↓\n\n"
        "The API sends the response back.\n\n"
        "↓\n\n"
        "Your Weather App displays the weather."
    )

    # ------------------------------------------------------

    card = create_card(content)

    card_heading(card, "🤖 Another Example")

    card_text(
        card,
        "Suppose you ask ChatGPT:\n\n"
        "\"Explain Newton's Laws\"\n\n"
        "Your question is sent to OpenAI's servers through an API.\n\n"
        "The AI generates an answer.\n\n"
        "The API sends that answer back to ChatGPT.\n\n"
        "Finally, ChatGPT displays the response on your screen."
    )

    # ------------------------------------------------------

    card = create_card(content)

    card_heading(card, "💡 Why do APIs exist?")

    card_text(
        card,
        "Without APIs:\n\n"
        "❌ Apps would directly access databases.\n"
        "❌ Security would become a huge problem.\n"
        "❌ Every application would communicate differently.\n\n"
        "With APIs:\n\n"
        "✅ Secure communication\n"
        "✅ Standard way to exchange information\n"
        "✅ Faster software development\n"
        "✅ Easier maintenance"
    )

    # ------------------------------------------------------

    card = create_card(content)

    card_heading(card, "⭐ Fun Fact")

    card_text(
        card,
        "Every single day you probably use hundreds of APIs.\n\n"
        "Examples include:\n\n"
        "📺 YouTube\n"
        "📸 Instagram\n"
        "🗺 Google Maps\n"
        "🎵 Spotify\n"
        "🛒 Amazon\n"
        "💳 UPI Apps\n"
        "🤖 ChatGPT\n\n"
        "Almost every modern application communicates with one or more APIs."
    )

    # ==========================================================
# LESSON 2 : REQUEST & RESPONSE
# ==========================================================

def show_request_page(content):

    clear(content)

    page_title(content, "🔄 Request & Response")

    subtitle(
        content,
        "Every API works because one application sends a request and receives a response."
    )

    # ------------------------------------------------------

    card = create_card(content)

    card_heading(card, "📤 What is a Request?")

    card_text(
        card,
        "A Request is simply asking for something.\n\n"
        "Think of it as sending a question.\n\n"
        "Example:\n"
        "\"What is today's weather?\"\n\n"
        "or\n\n"
        "\"Show me the profile of user octocat.\""
    )

    # ------------------------------------------------------

    card = create_card(content)

    card_heading(card, "📥 What is a Response?")

    card_text(
        card,
        "A Response is the answer sent back by the server.\n\n"
        "Example:\n\n"
        "Temperature = 31°C\n"
        "Humidity = 70%\n"
        "Condition = Cloudy"
    )

    # ------------------------------------------------------

    card = create_card(content)

    card_heading(card, "🔄 Complete Flow")

    diagram = """
      👤 User

        │

        ▼

     📱 Application

        │
     Request

        ▼

      🌐 API

        │

        ▼

     🖥 Server

        │

        ▼

   Processes Request

        │

        ▼

     🌐 API

        │
     Response

        ▼

     📱 Application

        │

        ▼

     👤 User
"""

    tk.Label(
        card,
        text=diagram,
        font=("Courier New", 12),
        bg="#3C4043",
        fg="#61AFEF",
        justify="center"
    ).pack()

    # ------------------------------------------------------

    card = create_card(content)

    card_heading(card, "🌍 Example")

    card_text(
        card,
        "Suppose you search:\n\n"
        "\"Virat Kohli\"\n\n"
        "The application sends a REQUEST.\n\n"
        "The server finds the information.\n\n"
        "It sends back a RESPONSE.\n\n"
        "Your application displays the information."
    )

    # ------------------------------------------------------

    card = create_card(content)

    card_heading(card, "💡 Remember")

    card_text(
        card,
        "Every API communication follows this pattern:\n\n"
        "Request ➜ Processing ➜ Response"
    )


# ==========================================================
# LESSON 3 : JSON
# ==========================================================

def show_json_page(content):

    clear(content)

    page_title(content, "📦 JSON Basics")

    subtitle(
        content,
        "Most APIs send information using a format called JSON."
    )

    # ------------------------------------------------------

    card = create_card(content)

    card_heading(card, "❓ What is JSON?")

    card_text(
        card,
        "JSON stands for:\n\n"
        "JavaScript Object Notation\n\n"
        "Despite its name, almost every programming language uses JSON.\n\n"
        "It is simply a neat way of storing and exchanging information."
    )

    # ------------------------------------------------------

    card = create_card(content)

    card_heading(card, "📖 Think of JSON as...")

    card_text(
        card,
        "A digital dictionary.\n\n"
        "Everything has a NAME and a VALUE."
    )

    # ------------------------------------------------------

    card = create_card(content)

    card_heading(card, "📄 Example JSON")

    example = """
{
    "name": "Dhairya",
    "country": "India",
    "age": 22,
    "student": true
}
"""

    tk.Label(
        card,
        text=example,
        font=("Courier New", 12),
        bg="#3C4043",
        fg="#98C379",
        justify="left"
    ).pack(anchor="w")

    # ------------------------------------------------------

    card = create_card(content)

    card_heading(card, "🧠 Understanding It")

    card_text(
        card,
        "name → Dhairya\n\n"
        "country → India\n\n"
        "age → 22\n\n"
        "student → True\n\n"
        "These are called key-value pairs."
    )

    # ------------------------------------------------------

    card = create_card(content)

    card_heading(card, "🌍 Why APIs Use JSON")

    card_text(
        card,
        "JSON is:\n\n"
        "✅ Lightweight\n"
        "✅ Easy to read\n"
        "✅ Easy to send over the internet\n"
        "✅ Supported by almost every programming language"
    )


# ==========================================================
# LESSON 4 : API KEYS
# ==========================================================

def show_key_page(content):

    clear(content)

    page_title(content, "🔑 API Keys")

    subtitle(
        content,
        "Some APIs require an API Key before they allow access."
    )

    # ------------------------------------------------------

    card = create_card(content)

    card_heading(card, "❓ Why do APIs need keys?")

    card_text(
        card,
        "Imagine a library.\n\n"
        "Anyone cannot simply enter restricted areas.\n\n"
        "You need an ID card.\n\n"
        "Similarly,\n"
        "many APIs require an API Key."
    )

    # ------------------------------------------------------

    card = create_card(content)

    card_heading(card, "🪪 What is an API Key?")

    card_text(
        card,
        "An API Key is a unique string of characters.\n\n"
        "It identifies who is making the request.\n\n"
        "It also allows companies to monitor usage."
    )

    # ------------------------------------------------------

    card = create_card(content)

    card_heading(card, "📄 Example")

    example = """
API Key

sk-demo123456789abcdef
"""

    tk.Label(
        card,
        text=example,
        bg="#3C4043",
        fg="#E5C07B",
        font=("Courier New", 12),
        justify="left"
    ).pack(anchor="w")

    # ------------------------------------------------------

    card = create_card(content)

    card_heading(card, "⚠ Never Share Your API Key")

    card_text(
        card,
        "Your API Key is like your ATM PIN.\n\n"
        "Never:\n\n"
        "❌ Upload it to GitHub\n"
        "❌ Share it publicly\n"
        "❌ Send screenshots showing it\n\n"
        "If someone gets your API Key, they may use your account."
    )

    # ------------------------------------------------------

    card = create_card(content)

    card_heading(card, "💡 Summary")

    card_text(
        card,
        "API Key = Digital Identity\n\n"
        "It tells the server:\n\n"
        "\"This request came from me.\""
    )