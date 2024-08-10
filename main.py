 import tkinter as tk
from tkinter import messagebox

# Function to calculate average and GPA
def calculate_results():
    try:
        grades = []
        for entry in grade_entries:
            grade = float(entry.get())
            if grade < 0 or grade > 100:
                raise ValueError("Grades must be between 0 and 100")
            grades.append(grade)

        if not grades:
            raise ValueError("No grades entered")

        average = sum(grades) / len(grades)
        gpa = average / 20  # Assuming GPA is on a 4.0 scale
        remarks = get_remarks(gpa)

        # Update results in the GUI
        avg_label.config(text=f"Average Grade: {average:.2f}")
        gpa_label.config(text=f"GPA: {gpa:.2f}")
        remarks_label.config(text=f"Remarks: {remarks}")

    except ValueError as e:
        messagebox.showerror("Input Error", str(e))
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Function to determine remarks based on GPA
def get_remarks(gpa):
    if gpa >= 3.7:
        return "Excellent"
    elif gpa >= 3.0:
        return "Good"
    elif gpa >= 2.0:
        return "Average"
    else:
        return "Needs Improvement"

# Create the main window
root = tk.Tk()
root.title("Student Grade Tracker")
root.geometry("400x400")  # Set a fixed size to make the window square
root.configure(bg="white")

# Create and place widgets
tk.Label(root, text="Enter Grades (0-100):", bg="white", font=("Arial", 16)).grid(row=0, column=0, columnspan=2, pady=10)

# List of subjects
subjects = ["Maths", "Physics", "Biology", "Chemistry", "Geography"]

grade_entries = []
for i, subject in enumerate(subjects):
    tk.Label(root, text=f"{subject}:", bg="white", font=("Arial", 14)).grid(row=i+1, column=0, padx=10, pady=5, sticky='e')
    entry = tk.Entry(root, width=15, font=("Arial", 14))
    entry.grid(row=i+1, column=1, padx=10, pady=5)
    grade_entries.append(entry)

calculate_button = tk.Button(root, text="Calculate", command=calculate_results, bg="black", fg="white", font=("Arial", 14))
calculate_button.grid(row=len(subjects)+1, column=0, columnspan=2, pady=15)

avg_label = tk.Label(root, text="Average Grade: ", bg="white", font=("Arial", 14))
avg_label.grid(row=len(subjects)+2, column=0, columnspan=2, pady=5)

gpa_label = tk.Label(root, text="GPA: ", bg="white", font=("Arial", 14))
gpa_label.grid(row=len(subjects)+3, column=0, columnspan=2, pady=5)

remarks_label = tk.Label(root, text="Remarks: ", bg="white", font=("Arial", 14))
remarks_label.grid(row=len(subjects)+4, column=0, columnspan=2, pady=15)

# Run the main loop
root.mainloop()
