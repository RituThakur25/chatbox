import tkinter as tk

def send_message():
    user_input = entry_var.get()
    display_chat(f'You: {user_input}')
    entry_var.set("")  # Clear the entry field after sending the message
    respond_to_user(user_input)

def display_chat(message):
    chat_history.config(state=tk.NORMAL)  # Set the text widget to be editable
    chat_history.insert(tk.END, message + '\n')
    chat_history.config(state=tk.DISABLED)  # Set the text widget to be read-only

def respond_to_user(user_input):
    # You can customize the chatbot responses based on user input
    response = f'ChatBot: I received "{user_input}"'
    display_chat(response)

def send():
    send = "You -> " + user_entry.get()
    user_entry(tk.END, "\n" + send)
 
    user = user_entry.get().lower()
 
    if (user == "hello"):
        user_entry(tk.END, "\n" + "Bot -> Hi there, how can I help?")
 
    elif (user == "hi" or user == "hii" or user == "hiiii"):
        user_entry(tk.END, "\n" + "Bot -> Hi there, what can I do for you?")
 
    elif (user == "how are you"):
        user_entry(tk.END, "\n" + "Bot -> fine! and you")
 
    elif (user == "fine" or user == "i am good" or user == "i am doing good"):
        user_entry(tk.END, "\n" + "Bot -> Great! how can I help you.")
 
    elif (user == "thanks" or user == "thank you" or user == "now its my time"):
        user_entry(tk.END, "\n" + "Bot -> My pleasure !")
 
    elif (user == "what do you sell" or user == "what kinds of items are there" or user == "have you something"):
       user_entry(tk.END, "\n" + "Bot -> We have coffee and tea")
 
    elif (user == "tell me a joke" or user == "tell me something funny" or user == "crack a funny line"):
       user_entry(tk.END, "\n" + "Bot -> What did the buffalo say when his son left for college? Bison.! ")
 
    elif (user == "goodbye" or user == "see you later" or user == "see yaa"):
        user_entry(tk.END, "\n" + "Bot -> Have a nice day!")
 
    else:
       user_entry(tk.END, "\n" + "Bot -> Sorry! I didn't understand that")
 
    user_entry.delete(0,tk.END)

# Create the main window
window = tk.Tk()
window.title("Simple Chatbot")

# Create a text widget for chat history
chat_history = tk.Text(window, height=10, width=40, state=tk.DISABLED)
chat_history.pack(pady=10)

# Create an entry widget for user input
entry_var = tk.StringVar()
user_entry = tk.Entry(window, textvariable=entry_var, width=30)
user_entry.pack(pady=10)

# Create a button to send messages
send_button = tk.Button(window, text="Send", command=send_message)
send_button.pack()

# Start the main event loop
window.mainloop()