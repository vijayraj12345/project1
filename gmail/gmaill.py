import tkinter as tk
from tkinter import messagebox

def validate_registration():
    # Get user input
    email = entry_email.get()
    password = entry_password.get()

    # Validate the input
    if not email or not password:
        messagebox.showerror("Error", "Please fill in all the required fields.")
        return


    # Validate email (simple validation for demonstration purposes)
    if '@' not in email or '.' not in email:
        messagebox.showerror("Error", "Invalid email format.")
        return

    # Validate password (simple validation for demonstration purposes)
    if len(password) < 6:
        messagebox.showerror("Error", "Password must be at least 6 characters long.")
        return

    # Display registration information (you can modify this part as needed)
    messagebox.showinfo("Registration Successful", f"Email: {email}")

# Create the main window
root = tk.Tk()
root.title("Registration Form")

# Create labels and entry widgets
label_email = tk.Label(root, text="Email:")
label_password = tk.Label(root, text="Password:")

entry_email = tk.Entry(root)
entry_password = tk.Entry(root, show="*")  # Show '*' for password characters

# Create the register button
register_button = tk.Button(root, text="Register", command=validate_registration)

# Organize widgets using grid layout
label_email.grid(row=1, column=0, sticky=tk.E)
label_password.grid(row=2, column=0, sticky=tk.E)

entry_email.grid(row=1, column=1)
entry_password.grid(row=2, column=1)

register_button.grid(row=3, column=1, pady=10)

# Start the Tkinter event loop
root.mainloop()
