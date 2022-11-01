from Pages import *

# Main Class
class SmartFridgeApp(customtkinter.CTk):
    def __init__(self, *args, **kwargs):
        customtkinter.CTk.__init__(self, *args, **kwargs)
        window = customtkinter.CTkFrame(self)
        window.pack(side="top", fill="both", expand=True)
        window.grid_rowconfigure(0, weight=1)
        window.grid_columnconfigure(0, weight=1)

        # this data is shared among all the classes
        self.app_login_cred = {'email': StringVar(), 'idToken': StringVar(), 'localId': StringVar()}
        
        self.frames = {}
        for F in (Login,
                  Register,
                  MainMenu,
                  PantryList,
                  OptionsPantryList,
                  NonPantryList,
                  OptionsNonPantryList,
                  SuggestedShopping,
                  OptionsSuggestedShopping,
                  RecipeSuggestions,
                  Settings):
            page_name = F.__name__
            global frame
            frame = F(master=window, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Login")

        #Styling the treeviews/
        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview", font=("", 20), background="#2a2d2e", foreground="white", rowheight=35, fieldbackground="#343638", bordercolor="#343638", borderwidth=0)
        style.map('Treeview', background=[('selected', '#22559b')])
        style.configure("Treeview.Heading", font=('Arial', 20, 'bold'), background="#565b5e",
                                                    foreground="white", relief="flat",  rowheight=35, fieldbackground="#343638", bordercolor="#343638", borderwidth=0)
        style.map("Treeview.Heading", background=[('active', '#3484F0')])

        self.change_mode()

    # Switches between Pages
    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

    # Call Matchbox keyboard automatically
    def entry_callback(self, event): 
        #os.popen('matchbox-keyboard','r',4096)
        pass
    
    # Functions for Settings Page
    def Reset_prompt(self): # Popup confirming reset
        choice = messagebox.askquestion("Reset", "Are you sure you want to reset? \n Proceeding will sign you out")
        if choice == 'yes':
            self.show_frame("Login")

    def Shutdown_prompt(self): # Popup confirming shutdown
        choice = messagebox.askquestion("Shutdown", "Are you sure you want to shutdown the system?")
        if choice == 'yes':
            subprocess.call(['sudo', 'shutdown', '-h', '-t 5', 'now'])

    def Restart_prompt(self): # Popup confirming restart
        choice = messagebox.askquestion("Reboot", "Are you sure you want to reboot the system?")
        if choice == 'yes':
            subprocess.call(['sudo', 'shutdown', '-r', '-t 5', 'now'])

    def show_clock_date(self):
        date=dt.datetime.now()
        format_date=f"{date:%a, %b %d %Y}"
        global date_label
        date_label=customtkinter.CTkLabel(self, text=format_date, text_font=("Calibri", 25), text_color = ("#1e3d6d", "#ebe7e4"))
        date_label.place(x=1030, y = 20)

        def Clock():
            hour = time.strftime("%I")
            minute = time.strftime("%M")
            second = time.strftime("%S")
            period = time.strftime("%p")
            clock.configure(text = hour + ":" + minute + ":" + second + " " + period)
            clock.after(1000, Clock)
        global clock
        clock = customtkinter.CTkLabel(self, text = "", text_font=("Calibri", 25), text_color = ("#1e3d6d", "#ebe7e4"))
        clock.place(x=1095, y=60)
        Clock()

    def hide_clock_date(self):

        date_label=customtkinter.CTkLabel(self, text = "                                   ",
                                            text_font=("Calibri", 25), text_color = ("#1e3d6d", "#ebe7e4"))
        date_label.place(x=1030, y = 20)

        clock = customtkinter.CTkLabel(self, text = "                             ",
                                        text_font=("Calibri", 25), text_color = ("#1e3d6d", "#ebe7e4"))
        clock.place(x=1080, y=60)

    # Functions for changing theme
    def change_appearance_mode(self):
        if switch.get() == 1:
            customtkinter.set_appearance_mode("dark")
        else:
            customtkinter.set_appearance_mode("light")

    def change_mode(self):
        global switch
        switch = customtkinter.CTkSwitch(self, text="Dark Mode", text_color = ("#1e3d6d", "#ebe7e4"), command = self.change_appearance_mode)
        switch.place(relx=0.02, rely=0.97, anchor= "sw")
        switch.select(1)

    def test(self):
            Id = self.app_login_cred['localId'].get()
            print(Id)

############ Initiallize app ############
if __name__ == "__main__":
    root = SmartFridgeApp()
    photo = PhotoImage(file = "assets/images/WVU.png")
    root.iconphoto(False, photo)
    root.title("Smart Fridge 2.0")
    root.resizable(0, 0)
    root.attributes('-topmost', 0)
    # App is desgined for the touchscreen resolution (not responsive):
    width = 1280
    height = 720
    # Centering the app in the middle of the screen
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (width/2))
    y_cordinate = int((screen_height/2) - (height/2))
    root.geometry("{}x{}+{}+{}".format(width, height, x_cordinate, y_cordinate))
    #root.attributes('-fullscreen', 1)
    root.mainloop()