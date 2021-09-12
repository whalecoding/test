from tkinter import *
from tkinter import ttk
 
operation = ''  #연산자 저장 변수
temp_number = 0  #이전값 저장 변수
 
# 숫자버튼 처리 함수
def button_pressed(value):
    # 입력값이 'AC'일때
    if value=='AC':
        number_entry.delete(0,'end')
        print("AC pressed")
    else: # 그외에 0부터 9까지 숫자일때
        number_entry.insert("end",value)
        print(value,"pressed")
 
# 사칙연산 처리
def math_button_pressed(value):
    global operation  #함수 바깥의 글로벌 변수사용
    global temp_number
    if not number_entry.get() == '': #기존에 입력한 숫자가 있을때만 연산버튼 인식
        operation = value
        temp_number = int(number_entry.get()) #입력된 숫자를 임시변수로 옮기고,
        number_entry.delete(0,'end')  #입력칸을 비우고, 다음숫자를 입력받을 준비.
        print(temp_number,operation)
 
# 결과 버튼 처리
def equal_button_pressed():
    global operation
    global temp_number
    #연산자나 숫자가 입력되지 않으면, 실행하지 않음.
    if not (operation =='' and number_entry.get()==''):
        number = int(number_entry.get())
        if operation == '/':
            solution = temp_number/number
        elif operation == '*':
            solution = temp_number*number
        elif operation == '+':
            solution = temp_number+number
        else :
            solution = temp_number-number
        # 계산후, 숫자표시칸을 비우고, 계산결과를 표시.
        number_entry.delete(0,'end')
        number_entry.insert(0,solution)
        print(temp_number,operation,number,"=",solution)
        operation = ''
        temp_number = 0
         
     
root = Tk()
root.title("Calculator")
root.geometry("400x200")
 
entry_value = StringVar(root, value='')
 
number_entry = ttk.Entry(root, textvariable = entry_value, width=20)
number_entry.grid(row=0, columnspan=3) 
 
 
button7 = ttk.Button(root, text="7", command = lambda:button_pressed('7'))
button7.grid(row=1, column=0)
button8 = ttk.Button(root, text="8", command = lambda:button_pressed('8'))
button8.grid(row=1, column=1)
button9 = ttk.Button(root, text="9", command = lambda:button_pressed('9'))
button9.grid(row=1, column=2)
button_div = ttk.Button(root, text="/", command = lambda:math_button_pressed('/'))
button_div.grid(row=1, column=3)
 
button4 = ttk.Button(root, text="4", command = lambda:button_pressed('4'))
button4.grid(row=2, column=0)
button5 = ttk.Button(root, text="5", command = lambda:button_pressed('5'))
button5.grid(row=2, column=1)
button6 = ttk.Button(root, text="6", command = lambda:button_pressed('6'))
button6.grid(row=2, column=2)
button_mult = ttk.Button(root, text="*", command = lambda:math_button_pressed('*'))
button_mult.grid(row=2, column=3)
 
button1 = ttk.Button(root, text="1", command = lambda:button_pressed('1'))
button1.grid(row=3, column=0)
button2 = ttk.Button(root, text="2", command = lambda:button_pressed('2'))
button2.grid(row=3, column=1)
button3 = ttk.Button(root, text="3", command = lambda:button_pressed('3'))
button3.grid(row=3, column=2)
button_add = ttk.Button(root, text="+", command = lambda:math_button_pressed('+'))
button_add.grid(row=3, column=3)
 
button_ac = ttk.Button(root, text="AC", command = lambda:button_pressed('AC'))
button_ac.grid(row=4, column=0)
button0 = ttk.Button(root, text="0", command = lambda:button_pressed('0'))
button0.grid(row=4, column=1)
button_equal = ttk.Button(root, text="=", command = lambda:equal_button_pressed())
button_equal.grid(row=4, column=2)
button_sub = ttk.Button(root, text="-", command = lambda:math_button_pressed('-'))
button_sub.grid(row=4, column=3)
 
root.mainloop()