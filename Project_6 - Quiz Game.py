from tkinter import *

#Define the questions dictionary
question = {
    'Q1-Total keywords in Python?' : ['33', '35', '31', '32'],
    'Q2-Output of 2**3?' : ['8', '6', '9', 'Syntax Error'],
    'Q3-Output of np.arange(1,5)?' : ['[0,1,2,3,4]', '[1,2,3,4,5]', '[1,2,3,4]', 'Error'],
    'Q4-Keywords are use to declare a function?' : ['define', 'Def', 'fun', 'def'],
    'Q5-Output of 121//5 and 121%5?' : ['24.2 and 0', '1 and 24', '24 and 1', '24.0 and 1.0']
}

ans = ['35', '8', '[1,2,3,4]', 'def', '24 and 1']

current_question = 0

def start_quiz():
    start_button.forget()
    next_button.pack()
    next_question()
    
    


def next_question():
    global current_question
    if current_question<len(question):
        check_ans()
        user_ans.set('None')
        c_question = list(question.keys())[current_question]
        clear_frame()

        Label(frame_1, text=f'{c_question}', padx=15, font=('Arial', 20, 'bold')).pack(anchor=NW)
        
        for option in question[c_question]:
            Radiobutton(frame_1, text=option, variable=user_ans, value=option, padx=28).pack(anchor=NW)

        current_question+=1

    else:
        next_button.forget()
        check_ans()
        clear_frame()

        output = f'Your Score is {user_score.get()} out of {len(question)}'
        Label(frame_1, text=output, font=('Arial', 30, 'bold')).pack()
        Label(frame_1, text='Thanks for Participating', font=('Arial', 30, 'bold'), background='light green', padx=10, pady=9).pack()
    
        

def check_ans():
    temp_ans = user_ans.get()
    if temp_ans != 'None' and temp_ans == ans[current_question-1]:
        user_score.set(user_score.get()+1)


def clear_frame():
    for widget in frame_1.winfo_children():
        widget.destroy()

    

    
    




#GUI Part
if __name__ == '__main__':
    root = Tk()

    root.title('QUIZ APP')
    root.geometry('850x520')

    user_ans = StringVar()
    user_ans.set('None')
    user_score = IntVar()
    user_score.set(0)

    Label(root, text='Quiz App', font=('Arial', 40, 'bold'), relief=SUNKEN, background='cyan', padx=10, pady=9).pack()
    Label(root, text='', font=('Arial', 30, 'bold')).pack()
    start_button = Button(root, text='Start Quiz',font=('Arial', 30, 'bold'), command=start_quiz)
    start_button.pack()

    frame_1 = Frame(root)
    frame_1.pack(side=TOP, fill=X)

    next_button = Button(root, text='Next Question', font=('Arial', 30, 'bold'), command=next_question)
    
    root.mainloop()