import tkinter as tk
import openai

openai.api_key = "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"

def generate_response(prompt, history):
    try:
        model = "text-davinci-002"
        response = openai.Completion.create(
            engine=model,
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
            context=history,
        )
        return response.choices[0].text.strip()
    except Exception as e:
        print("An error occurred: ", e)
        return None

def get_user_input():
    return input_box.get().strip().lower()

def is_goodbye(user_input):
    return user_input in ['bye', 'goodbye']

def update_chat():
    user_input = get_user_input()

    if is_goodbye(user_input):
        response_box.insert(tk.END, "Aivius: Goodbye! Have a great day.")
        input_box.delete(0, tk.END)
        input_box.configure(state=tk.DISABLED)
        send_button.configure(state=tk.DISABLED)
        return

    if not user_input:
        response_box.insert(tk.END, "Aivius: Please say something.")
    else:
        history.append(f"You: {user_input}")
        prompt = "\n".join(history + [f"Aivius: "])
        response = generate_response(prompt, history)
        if not response:
            response_box.insert(tk.END, "Aivius: Sorry, I couldn't process your request.")
        else:
            response_box.insert(tk.END, f"Aivius: {response}")
            history.append(f"Aivius: {response}")
    response_box.see(tk.END)
    input_box.delete(0, tk.END)

# Create a window
root = tk.Tk()
root.title("Aivius Chatbot")

# Add a label to the window
label = tk.Label(root, text="Aivius Chatbot", font=("Arial Bold", 20))
label.grid(column=0, row=0, columnspan=2)

# Add a response box to the window
response_box = tk.Text(root, wrap=tk.WORD, width=50, height=20, state=tk.DISABLED)
response_box.grid(column=0, row=1, padx=10, pady=10)

# Add an input box to the window
input_box = tk.Entry(root, width=50)
input_box.grid(column=0, row=2, padx=10, pady=10)

# Add a send button to the window
send_button = tk.Button(root, text="Send", command=update_chat)
send_button.grid(column=1, row=2, padx=10, pady=10)

# Initialize the chatbot
history = []
response_box.configure(state=tk.NORMAL)
response_box.insert(tk.END, "Aivius: Greetings! I'm Aivius, an AI that you can ask anything! So what would you like to know?")
response_box.configure(state=tk.DISABLED)

# Start the event loop
root.mainloop()
