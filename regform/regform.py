import tkinter as tk
from tkinter import messagebox, ttk

# Function to submit form data
def submit_form():
    name = name_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    age = age_entry.get()
    gender = gender_var.get()
    event_type = event_type_var.get()
    
    if not name or not email or not phone or not age or gender == "Select" or event_type == "Select":
        messagebox.showwarning("Input Error", "Please fill out all fields!")
    else:
        messagebox.showinfo("Success", f"Registration successful for {name}!\n"
                                       f"Event: {event_type}\nGender: {gender}\nAge: {age}")
        # Here you can add code to save or process the data

# Create main window
root = tk.Tk()
root.title("Interactive Event Registration Form")
root.geometry("350x400")

# Create form fields
tk.Label(root, text="Event Registration", font=("Helvetica", 16)).pack(pady=10)

# Name field
tk.Label(root, text="Name").pack(pady=5)
name_entry = tk.Entry(root, width=35)
name_entry.pack()

# Email field
tk.Label(root, text="Email").pack(pady=5)
email_entry = tk.Entry(root, width=35)
email_entry.pack()

# Phone field
tk.Label(root, text="Phone").pack(pady=5)
phone_entry = tk.Entry(root, width=35)
phone_entry.pack()

# Age field
tk.Label(root, text="Age").pack(pady=5)
age_entry = tk.Entry(root, width=35)
age_entry.pack()

# Gender field (Dropdown)
tk.Label(root, text="Gender").pack(pady=5)
gender_var = tk.StringVar()
gender_var.set("Select")
gender_menu = ttk.Combobox(root, textvariable=gender_var, values=["Male", "Female", "Other"])
gender_menu.pack()

# Event Type field (Dropdown)
tk.Label(root, text="Event Type").pack(pady=5)
event_type_var = tk.StringVar()
event_type_var.set("Select")
event_type_menu = ttk.Combobox(root, textvariable=event_type_var, values=["Workshop", "Seminar", "Conference", "Meetup"])
event_type_menu.pack()

# Submit button
submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.pack(pady=20)

# Run the application
root.mainloop()
