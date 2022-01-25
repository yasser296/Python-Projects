from tkinter import messagebox




show_info = messagebox.showinfo(title = "Info" , message = "Certain information")
print(show_info)


show_warning = messagebox.showwarning(title = "Warning!" , message = "Warning, errors may occur"  ) 
print(show_warning)


show_error = messagebox.showerror(title = "Error!" , message = "An Error has occurred, aborting" )
print(show_error)


ask_question = messagebox.askquestion(title = "New file" , message = "Save changes?" )
print(ask_question)


ask_yes_no = messagebox.askyesno(title = "Confirm" , message = "Do you wish to continue")
print(ask_yes_no)


ask_yes_no_cancel = messagebox.askyesnocancel(title = "Confirm" , message = "Do you wish to continue")
print(ask_yes_no_cancel)


ask_retry_cancel = messagebox.askretrycancel(title = "Confirm" , message = "Do you wish to try again")
print(ask_retry_cancel)











