import tkinter as tk
from tkinter import messagebox, ttk
from ttkbootstrap import Style
from quiz_data import quiz_data

# Function to display the current pergunta and choices
def show_questao():
    # Get the current pergunta from the quiz_data list
    pergunta = quiz_data[current_questao]
    qs_label.config(text=pergunta["pergunta"])

    # Display the choices on the buttons
    choices = pergunta["choices"]
    for i in range(4):
        choice_btns[i].config(text=choices[i], state="normal") # Reset button state

    # Clear the feedback label and disable the next button
    feedback_label.config(text="")
    next_btn.config(state="disabled")

# Function to check the selected answer and provide feedback
def check_answer(choice):
    # Get the current pergunta from the quiz_data list
    pergunta = quiz_data[current_questao]
    selected_choice = choice_btns[choice].cget("text")

    # Check if the selected choice matches the correct answer
    if selected_choice == pergunta["answer"]:
        # Update the score and display it
        global score
        score += 1
        score_label.config(text="Score: {}/{}".format(score, len(quiz_data)))
        feedback_label.config(text="Correct!", foreground="green")
    else:
        feedback_label.config(text="Incorrect!", foreground="red")
    
    # Disable all choice buttons and enable the next button
    for button in choice_btns:
        button.config(state="disabled")
    next_btn.config(state="normal")

# Function to move to the next pergunta
def next_questao():
    global current_questao
    current_questao +=1

    if current_questao < len(quiz_data):
        # If there are more questaos, show the next pergunta
        show_questao()
    else:
        # If all questaos have been answered, display the final score and end the quiz
        messagebox.showinfo("Quiz Completed",
                            "Quiz Completed! Final score: {}/{}".format(score, len(quiz_data)))
        root.destroy()

# Create the main window
root = tk.Tk()
root.title("Quiz App")
root.geometry("600x500")
style = Style(theme="flatly")

# Configure the font size for the pergunta and choice buttons
style.configure("TLabel", font=("Helvetica", 20))
style.configure("TButton", font=("Helvetica", 16))

# Create the pergunta label
qs_label = ttk.Label(
    root,
    anchor="center",
    wraplength=500,
    padding=10
)
qs_label.pack(pady=10)

# Create the choice buttons
choice_btns = []
for i in range(4):
    button = ttk.Button(
        root,
        command=lambda i=i: check_answer(i)
    )
    button.pack(pady=5)
    choice_btns.append(button)

# Create the feedback label
feedback_label = ttk.Label(
    root,
    anchor="center",
    padding=10
)
feedback_label.pack(pady=10)

# Initialize the score
score = 0

# Create the score label
score_label = ttk.Label(
    root,
    text="Score: 0/{}".format(len(quiz_data)),
    anchor="center",
    padding=10
)
score_label.pack(pady=10)

# Create the next button
next_btn = ttk.Button(
    root,
    text="Next",
    command=next_questao,
    state="disabled"
)
next_btn.pack(pady=10)

# Initialize the current pergunta index
current_questao = 0

# Show the first pergunta
show_questao()

# Start the main event loop
root.mainloop()