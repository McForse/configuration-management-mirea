from tkinter import *
import interpreter


def generate():
    output.configure(state='normal')
    output.delete('1.0', END)
    output.insert(1.0, interpreter.toJson(code.get("1.0",END)))


root = Tk()
root.title('Code interpreter')

button = Button(text='Interpreter', command=generate)
button.pack()

code = Text(width=60, height=40, font=('Menlo', 14), bg='grey25', fg='white', wrap=WORD)
code.pack(side="left", fill="y")

output = Text(width=60, height=40, font=('Menlo', 14), bg='grey25', fg='white', wrap=WORD)
output.configure(state='disabled')
output.pack(side="right", fill="both", expand=True)

root.mainloop()