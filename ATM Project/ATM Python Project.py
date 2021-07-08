import tkinter as tk
import time

current_balance = 1000

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.shared_data = {'Balance':tk.IntVar()}
        
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, MainMenu, WithdrawPage, DepositPage, BalancePage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#5c5c8a')
        self.controller = controller

        self.controller.title('Alexander ATM')
        self.controller.state('zoomed')
        self.controller.iconphoto(False,
                         tk.PhotoImage(file='C:/Users/Alex/Desktop/ATM Project/atm.png'))

        heading_labe1=tk.Label(self,
                               text='ALEXANDER ATM',
                               font=('kredit',75,'bold'),
                               foreground='white',
                               background='#5c5c8a')

        heading_labe1.pack(pady=100)

        space_label=tk.Label(self,height=4,bg='#5c5c8a')
        space_label.pack()

        password_label = tk.Label(self,
                                  text='Enter your password',
                                  font=('kredit',14,'bold'),
                                  bg='#5c5c8a',
                                  fg='white')
        password_label.pack(pady=15)

        my_password = tk.StringVar()
        password_entry_box=tk.Entry(self,
                                    textvariable=my_password,
                                    font=('kredit',12),
                                    width=22)
        password_entry_box.focus_set()
        password_entry_box.pack(ipady=7)

        def handle_focus_in(_):
            password_entry_box.configure(fg='black',show='*')
        password_entry_box.bind('<FocusIn>',handle_focus_in)

        def check_password():
            if my_password.get() =='1234':
               my_password.set('')
               incorrect_password_label['text']=''
               controller.show_frame('MainMenu')
            else:
                incorrect_password_label['text']='Incorrect Password'
                
        enter_button = tk.Button(self,
                                text='Login',
                                command=check_password,
                                relief='raised',
                                borderwidth = 1,
                                width=28,
                                height=2)
        
        enter_button.pack(pady=15)

        incorrect_password_label = tk.Label(self,
                                            text='',
                                            font=('kredit',13),
                                            fg='white',
                                            bg='#52527a',
                                            anchor='n')
        
        incorrect_password_label.pack(fill='both',expand=True)

        bottom_frame = tk.Frame(self,relief='raised',borderwidth=3)
        bottom_frame.pack(fill='x',side='bottom')

        visa_photo = tk.PhotoImage(file='visa.png')
        visa_label = tk.Label(bottom_frame,image=visa_photo)
        visa_label.pack(side='left')
        visa_label.image=visa_photo

        amex_photo = tk.PhotoImage(file='amex.png')
        amex_label = tk.Label(bottom_frame,image=amex_photo)
        amex_label.pack(side='left')
        amex_label.image=amex_photo

        discover_photo = tk.PhotoImage(file='discover.png')
        discover_label = tk.Label(bottom_frame,image=discover_photo)
        discover_label.pack(side='left')
        discover_label.image=discover_photo

        def tick():
            current_time = time.strftime('%I:%M%p').lstrip('0').replace(' 0',' ')
            time_label.config(text=current_time)
            time_label.after(200,tick)
            
        time_label = tk.Label(bottom_frame,font=('kredit',14))
        time_label.pack(side='right')

        tick()

class MainMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#5c5c8a')
        self.controller = controller

        heading_label=tk.Label(self,
                               text='ALEXANDER ATM',
                               font=('kredit',75,'bold'),
                               foreground='white',
                               background='#5c5c8a')

        heading_label.pack(pady=100)

        main_menu_label = tk.Label(self,
                                   text='MAIN MENU',
                                   font=('kredit',14, 'bold'),
                                   fg='white',
                                   bg='#5c5c8a')
        
        main_menu_label.pack()

        selection_label = tk.Label(self,
                                   text='PLEASE MAKE A SELECTION',
                                   font=('kredit',14, 'bold'),
                                    fg='white',
                                    bg='#5c5c8a',
                                    anchor='w')
        
        selection_label.pack(fill='x', padx=15)

        button_frame = tk.Frame(self,bg='#52527a')
        button_frame.pack(fill='both',expand=True)

        def withdraw():
            controller.show_frame('WithdrawPage')
            
        withdraw_button = tk.Button(button_frame,
                                    text='Withdraw',
                                    command=withdraw,
                                    relief='raised',
                                    borderwidth=3,
                                    width=50,
                                    height=3)
        
        withdraw_button.grid(row=0,column=0,pady=5,padx=15)

        def deposit():
            controller.show_frame('DepositPage')
            
        deposit_button = tk.Button(button_frame,
                                    text='Deposit',
                                    command=deposit,
                                    relief='raised',
                                    borderwidth=3,
                                    width=50,
                                    height=3)
        
        deposit_button.grid(row=1,column=0,pady=5)

        def balance():
            controller.show_frame('BalancePage')
            
        balance_button = tk.Button(button_frame,
                                    text='Balance',
                                    command=balance,
                                    relief='raised',
                                    borderwidth=3,
                                    width=50,
                                    height=3)
        
        balance_button.grid(row=2,column=0,pady=5)

        def exit():
            controller.show_frame('StartPage')
            
        exit_button = tk.Button(button_frame,
                                    text='Exit',
                                    command=exit,
                                    relief='raised',
                                    borderwidth=3,
                                    width=50,
                                    height=3)
        
        exit_button.grid(row=3,column=0,pady=5)

        bottom_frame = tk.Frame(self,relief='raised',borderwidth=3)
        bottom_frame.pack(fill='x',side='bottom')

        visa_photo = tk.PhotoImage(file='visa.png')
        visa_label = tk.Label(bottom_frame,image=visa_photo)
        visa_label.pack(side='left')
        visa_label.image=visa_photo

        amex_photo = tk.PhotoImage(file='amex.png')
        amex_label = tk.Label(bottom_frame,image=amex_photo)
        amex_label.pack(side='left')
        amex_label.image=amex_photo

        discover_photo = tk.PhotoImage(file='discover.png')
        discover_label = tk.Label(bottom_frame,image=discover_photo)
        discover_label.pack(side='left')
        discover_label.image=discover_photo

        def tick():
            current_time = time.strftime('%I:%M%p').lstrip('0').replace(' 0',' ')
            time_label.config(text=current_time)
            time_label.after(200,tick)
            
        time_label = tk.Label(bottom_frame,font=('kredit',14))
        time_label.pack(side='right')

        tick()


class WithdrawPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#5c5c8a')
        self.controller = controller

        heading_label=tk.Label(self,
                               text='ALEXANDER ATM',
                               font=('kredit',75,'bold'),
                               foreground='white',
                               background='#5c5c8a')

        heading_label.pack(pady=100)

        choose_amount_label = tk.Label(self,
                                   text='PLEASE SELECT THE AMOUNT YOU WOULD LIKE TO WITHDRAW',
                                   font=('kredit',14, 'bold'),
                                   fg='white',
                                   bg='#5c5c8a')
        choose_amount_label.pack()

        button_frame = tk.Frame(self,bg='#52527a')
        button_frame.pack(fill='both',expand=True)

        def withdraw(amount):
            global current_balance
            current_balance -= amount
            controller.show_frame('MainMenu')
            
        twenty_button = tk.Button(button_frame,
                                  text='20',
                                  command=lambda:withdraw(20),
                                  relief='raised',
                                  borderwidth=3,
                                  width=50,
                                  height=3)
        
        twenty_button.grid(row=0,column=0,pady=5,padx=15)

        forty_button = tk.Button(button_frame,
                                  text='40',
                                  command=lambda:withdraw(40),
                                  relief='raised',
                                  borderwidth=3,
                                  width=50,
                                  height=3)
        
        forty_button.grid(row=1,column=0,pady=5)

        sixty_button = tk.Button(button_frame,
                                  text='60',
                                  command=lambda:withdraw(60),
                                  relief='raised',
                                  borderwidth=3,
                                  width=50,
                                  height=3)
        
        sixty_button.grid(row=2,column=0,pady=5)

        eighty_button = tk.Button(button_frame,
                                  text='80',
                                  command=lambda:withdraw(80),
                                  relief='raised',
                                  borderwidth=3,
                                  width=50,
                                  height=3)
        
        eighty_button.grid(row=3,column=0,pady=5)

        one_hundred_button = tk.Button(button_frame,
                                  text='100',
                                  command=lambda:withdraw(100),
                                  relief='raised',
                                  borderwidth=3,
                                  width=50,
                                  height=3)
        
        one_hundred_button.grid(row=0,column=1,pady=5,padx=1150)

        two_hundred_button = tk.Button(button_frame,
                                  text='200',
                                  command=lambda:withdraw(200),
                                  relief='raised',
                                  borderwidth=3,
                                  width=50,
                                  height=3)
        
        two_hundred_button.grid(row=1,column=1,pady=5)

        three_hundred_button = tk.Button(button_frame,
                                  text='300',
                                  command=lambda:withdraw(300),
                                  relief='raised',
                                  borderwidth=3,
                                  width=50,
                                  height=3)
        
        three_hundred_button.grid(row=2,column=1,pady=5)

        cash = tk.StringVar()
        other_amount_entry = tk.Entry(button_frame,
                                  textvariable=cash,
                                  width=60,
                                  justify='right')
        
        other_amount_entry.grid(row=3,column=1,pady=5,ipady=20)

        def other_amount(_):
            global current_balance
            current_balance -= int(cash.get())
            controller.shared_data['Balance'].set(current_balance)
            cash.set('')
            controller.show_frame('MainMenu')
            
        other_amount_entry.bind('<Return>',other_amount)

        bottom_frame = tk.Frame(self,relief='raised',borderwidth=3)
        bottom_frame.pack(fill='x',side='bottom')

        visa_photo = tk.PhotoImage(file='visa.png')
        visa_label = tk.Label(bottom_frame,image=visa_photo)
        visa_label.pack(side='left')
        visa_label.image=visa_photo

        amex_photo = tk.PhotoImage(file='amex.png')
        amex_label = tk.Label(bottom_frame,image=amex_photo)
        amex_label.pack(side='left')
        amex_label.image=amex_photo

        discover_photo = tk.PhotoImage(file='discover.png')
        discover_label = tk.Label(bottom_frame,image=discover_photo)
        discover_label.pack(side='left')
        discover_label.image=discover_photo

        def tick():
            current_time = time.strftime('%I:%M%p').lstrip('0').replace(' 0',' ')
            time_label.config(text=current_time)
            time_label.after(200,tick)
            
        time_label = tk.Label(bottom_frame,font=('kredit',14))
        time_label.pack(side='right')

        tick()

class DepositPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#5c5c8a')
        self.controller = controller

        heading_labe1=tk.Label(self,
                               text='ALEXANDER ATM',
                               font=('kredit',75,'bold'),
                               foreground='white',
                               background='#5c5c8a')

        heading_labe1.pack(pady=100)

        space_label=tk.Label(self,height=4,bg='#5c5c8a')
        space_label.pack()

        enter_amount_label = tk.Label(self,
                                  text='ENTER AMOUNT',
                                  font=('kredit',14, 'bold'),
                                  bg='#5c5c8a',
                                  fg='white')
        enter_amount_label.pack(ipady=7)

        cash = tk.StringVar()
        deposit_entry =tk.Entry(self,
                                textvariable=cash,
                                font=('kredit',12),
                                width=22)
        deposit_entry.pack(ipady=5)

        def deposit_cash():
            global current_balance
            current_balance +=int(cash.get())
            controller.shared_data['Balance'].set(current_balance)
            controller.show_frame('MainMenu')
            cash.set(' ')
            
        enter_button =tk.Button(self,
                                text='Enter',
                                command=deposit_cash,
                                relief='raised',
                                borderwidth=1,
                                width=28,
                                height=2)
        enter_button.pack(pady=15)

        two_tone_label = tk.Label(self,bg='#52527a')
        two_tone_label.pack(fill='both',expand=True)

        bottom_frame = tk.Frame(self,relief='raised',borderwidth=3)
        bottom_frame.pack(fill='x',side='bottom')

        visa_photo = tk.PhotoImage(file='visa.png')
        visa_label = tk.Label(bottom_frame,image=visa_photo)
        visa_label.pack(side='left')
        visa_label.image=visa_photo

        amex_photo = tk.PhotoImage(file='amex.png')
        amex_label = tk.Label(bottom_frame,image=amex_photo)
        amex_label.pack(side='left')
        amex_label.image=amex_photo

        discover_photo = tk.PhotoImage(file='discover.png')
        discover_label = tk.Label(bottom_frame,image=discover_photo)
        discover_label.pack(side='left')
        discover_label.image=discover_photo

        def tick():
            current_time = time.strftime('%I:%M%p').lstrip('0').replace(' 0',' ')
            time_label.config(text=current_time)
            time_label.after(200,tick)
            
        time_label = tk.Label(bottom_frame,font=('kredit',14))
        time_label.pack(side='right')

        tick()

class BalancePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#5c5c8a')
        self.controller = controller

        heading_labe1 = tk.Label(self,
                               text='ALEXANDER ATM',
                               font=('kredit',75,'bold'),
                               foreground='white',
                               background='#5c5c8a')

        heading_labe1.pack(pady=100)
        
        global current_balance
        controller.shared_data['Balance'].set(current_balance)
        balance_label = tk.Label(self,
                                 textvariable=controller.shared_data['Balance'],
                                 font=('kredit',14, 'bold'),
                                 fg='white',
                                 bg='#5c5c8a',
                                 anchor='w')
        
        balance_label.pack(fill='x', padx=15)

        button_frame = tk.Frame(self,bg='#52527a')
        button_frame.pack(fill='both',expand=True)

        def menu():
            controller.show_frame('MainMenu')

        menu_button = tk.Button(button_frame,
                                command=menu,
                                text='Menu',
                                relief='raised',
                                borderwidth=3,
                                width=50,
                                height=3)
                                  
        menu_button.grid(row=0,column=0,pady=5,padx=15)

        def exit():
            controller.show_frame('StartPage')
                                  
        exit_button = tk.Button(button_frame,
                                text='Exit',
                                command=exit,
                                relief='raised',
                                borderwidth=3,
                                width=50,
                                height=3)
                                  
        exit_button.grid(row=1,column=0,pady=5, padx=15)
                                

        bottom_frame = tk.Frame(self,relief='raised',borderwidth=3)
        bottom_frame.pack(fill='x',side='bottom')

        visa_photo = tk.PhotoImage(file='visa.png')
        visa_label = tk.Label(bottom_frame,image=visa_photo)
        visa_label.pack(side='left')
        visa_label.image=visa_photo

        amex_photo = tk.PhotoImage(file='amex.png')
        amex_label = tk.Label(bottom_frame,image=amex_photo)
        amex_label.pack(side='left')
        amex_label.image=amex_photo

        discover_photo = tk.PhotoImage(file='discover.png')
        discover_label = tk.Label(bottom_frame,image=discover_photo)
        discover_label.pack(side='left')
        discover_label.image=discover_photo

        def tick():
            current_time = time.strftime('%I:%M%p').lstrip('0').replace(' 0',' ')
            time_label.config(text=current_time)
            time_label.after(200,tick)
            
        time_label = tk.Label(bottom_frame,font=('kredit',14))
        time_label.pack(side='right')

        tick()

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
