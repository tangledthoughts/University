import tkinter as tk
from tkinter import *
from tkinter import messagebox

def on_button_toggle():
  if var.get() == 1:
    print("Checkbutton is selected")
  else:
    print("Checkbutton is deselected")

# Create a Checkbutton
var = tk.IntVar()
checkbutton = tk.Checkbutton(root, text="Enable Feature", variable=var,
onvalue=1, offvalue=0, command=on_button_toggle)

# Setting options for the Checkbutton
checkbutton.config(bg="lightgrey", fg="blue", font=("Arial", 12), selectcolor="green", relief="raised", padx=10, pady=5)

tasks_list = checkbutton
counter = 1

def Input_Error():
  if enterTaskField.get() == "" :
    messagebox.showerror("Input Error")
    return 0
  else:
    return 1
  
def clear_taskNumberField():
  taskNumberField.delete(0.0, END)

def clear_taskField():
  enterTaskField.delete(0, END)

def insertTask():
  global counter
  value = Input_Error()
  if value == 0 :
    return
  
  content = enterTaskField.get() + "\n"
  tasks_list.append(content)
  TextArea.insert('end -1 chars', "[ " + str(counter) + " ] " + content)
  counter += 1 
  clear_TaskField()

def delete():
  global counter

  if len(tasks_list) == 0 :
    messagebox.showerror("No Tasks to Delete")
    return
  else:
    number = taskNumberField.get("1.0", END)
    if number == "\n" :
      messagebox.showerror("Input Error")
      return
    else:
      try:
        index = int(number.strip()) - 1
        if 0 <= index < len(tasks_list):
          del tasks_list[index]
          TextArea.delete('1.0', END)
          for i, task in enumerate(tasks_list):
            TextArea.insert('end -1 chars', "[ " + str(i + 1) + " ] " + tasks_list[i])
          counter -= 1
        else:
          messagebox.showerror("Invalid Task Number")
      except ValueError:
        messagebox.showerror("Input Error: Please enter a valid number")

if __name__ == "__main__":
  gui = Tk()
  gui.configure(bg="lightblue")
  gui.title("Task Manager")
  gui.geometry("400x400") 
  enterTaskField = Entry(gui, width=30)
  enterTaskField.pack(pady=10)
  Submit = Button(gui, text="Submit", fg="black", bg="red", command=insertTask)
  Submit.pack(pady=5)
  TextArea = Text(gui, height=10, width=40, font="lucida 13")
  TextArea.pack(pady=10)
  taskNumber = Label(gui, text="Delete Task Number", fg="white", bg="blue")
  taskNumber.pack(pady=5)
  taskNumberField = Text(gui, height=1, width=5, font="lucida 13")
  taskNumberField.pack(pady=5)
  Delete = Button(gui, text="Delete", fg="white", bg="red", command=delete)
  Delete.pack(pady=5)
  Exit = Button(gui, text="Exit", fg="white", bg="black", command=gui.quit)
  Exit.pack(pady=5)
  enterTaskField.grid(row=0, column=0, padx=10, pady=10)
  Submit.grid(row=0, column=1, padx=10, pady=10)
  TextArea.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
  taskNumber.grid(row=2, column=0, padx=10, pady=10)
  taskNumberField.grid(row=2, column=1, padx  =10, pady=10)
  Delete.grid(row=3, column=0, padx=10, pady=10)
  Exit.grid(row=3, column=1, padx=10, pady=10)
gui.mainloop()