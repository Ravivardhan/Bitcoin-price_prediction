import tkinter as tk
from tkinter import *
import sqlite3
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as pl
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import webbrowser
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.layers import Dense,Dropout,LSTM
from tensorflow.keras.models import Sequential
database = sqlite3.connect("user_data")
cursor = database.cursor()
cursor.execute("create table if not exists user_db(username varchar(40),password varchar(50))")

########################################################  A  L  G  O  ########################################################
def code(symbol):
    from sklearn.linear_model import LinearRegression
    import datetime as dt
    import pandas as pd
    # pandas and numpy are used for data manipulation
    import pandas as pd
    import numpy as np

    # matplotlib and seaborn are used for plotting graphs
    import matplotlib.pyplot as plt
    plt.style.use('seaborn-darkgrid')

    # yahoo finance is used to fetch data
    import yfinance as yf

    Df = yf.download(symbol, '2021-01-01', '2021-06-01', auto_adjust=True)

    # Only keep close columns
    Df = Df[['Close']]

    Df = Df.dropna()

    old = yf.download(symbol, '2021-01-01', '2021-06-01', auto_adjust=True)

    # Only keep close columns
    old = Df[['Close']]

    # Drop rows with missing values
    old = Df.dropna()

    # Plot the closing price of GLD


    old.Close.plot(figsize=(10, 7), color='r')
    plt.ylabel("{}  Prices".format(symbol))
    plt.title("{} Price Series".format(symbol))

    plt.show()
    
    Df['S_3'] = Df['Close'].rolling(window=3).mean()
    Df['S_9'] = Df['Close'].rolling(window=9).mean()
    Df['next_day_price'] = Df['Close'].shift(-1)

    Df = Df.dropna()
    X = Df[['S_3', 'S_9']]

    # Define dependent variable
    y = Df['next_day_price']

    t = .4
    t = int(t * len(Df))

    # Train dataset
    X_train = X[:t]
    y_train = y[:t]

    # Test dataset
    X_test = X[t:]
    y_test = y[t:]

    linear = LinearRegression().fit(X_train, y_train)

    predicted_price = linear.predict(X_test)

    ##################################################################################################

    import pandas as pd
    import numpy as np
    from datetime import datetime, timedelta

    date_today = datetime.now()
    days = pd.date_range(date_today, date_today + timedelta(85), freq='D')

    np.random.seed(seed=1111)
    data = np.random.randint(1, high=100, size=len(days))
    df = pd.DataFrame({'test': days, 'col2': data})
    df = df.set_index('test')

    ##################################################################################################

    predicted_price = pd.DataFrame(
        predicted_price, index=df.index, columns=['price'])
    predicted_price.plot(figsize=(10, 7))

    plt.legend(['predicted_price'])
    plt.ylabel("{} Price".format(symbol))
    plt.show()


























def sign_new():
    window.destroy()
    signup_frame = tk.Tk()
    signup_frame.geometry('700x700')
    label_sig = Label(signup_frame, text="SIGN UP", font=('Helvatice', 44)).place(x=270, y=50)

    sign_label_username = Label(signup_frame, text="Username :", font=('Helvatica', 22)).place(x=200, y=220)
    sign_input_username = Entry(signup_frame, width=30)
    sign_input_username.place(x=360, y=219, height=39)

    sign_pass_label = Label(signup_frame, text="Password :", font=("Helvatica", 22)).place(x=200, y=320)
    sign_pass_entry = Entry(signup_frame, width=30, show="*")
    sign_pass_entry.place(x=360, y=319, height=39)

    Login = Button(signup_frame, text="signup", command=lambda: signin()).place(x=370, y=420, height=50, width=100)

    def signin():
        with sqlite3.connect("user_data") as db:
            cur = db.cursor()
            name = sign_input_username.get()
            password = sign_pass_entry.get()

            query = "insert into user_db(username,password) values('{}','{}')".format(name, password)
            cur.execute(query)
            db.commit()
            messagebox.showinfo('sign up', 'signup successfull.. login to continue')
            signup_frame.destroy()
            main_app()


window = tk.Tk()
window.geometry('700x700')

log_title = Label(window, text="LOGIN", font=("Helvatica", 40)).place(x=300, y=50)

username_label = Label(window, text="Username:", font=("Helvatica", 22)).place(x=200, y=220)
username_entry = Entry(window, width=30)
# ,
username_entry.place(x=360, y=219, height=39)

password_label = Label(window, text="Password:", font=("Helvatica", 22)).place(x=200, y=320)
password_entry = Entry(window, width=30, show="*")
password_entry.place(x=360, y=319, height=39)


# ,
def login(name='', password=''):
    with sqlite3.connect("user_data") as db:
        cur = db.cursor()
        name = username_entry.get()
        password = password_entry.get()
        user_login = "select * from user_db where username='{}' and password='{}'".format(name, password)
        cur.execute(user_login)
        data = cur.fetchone()
        print(data)
        db.commit()
        if data!=None:
                messagebox.showinfo('logged in', 'login successful')

                window.destroy()
                main_app()

        elif data==None:
                print("not a user")
                messagebox.showerror('failed', 'invalid username or password')

        ################################################-----M  A  I  N    A  P  P  L  I  C  A  T  I  O  N-----#######################################




Login = Button(window, text="Login", command=lambda: login()).place(x=370, y=420, height=50, width=100)
#

sign = Label(window, text="already have an account?").place(y=520, x=270)

sign_up = Button(window, text="signup here", command=lambda: sign_new()).place(x=430, y=515, height=40, width=120)
# ,


forget = Button(window, text="forget password?").place(x=470, y=359, height=30, width=130)







def main_app():

    root = Tk()
    root.title("Python: Bitcoin price prediction")

    width = 500
    height = 500


    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.geometry("%dx%d+%d+%d" % (width, height, x, y))
    root.resizable(0, 0)

    choices = ['BTC-USD', 'DOGE-USD', 'ETH-USD','USDT-USD','VET-USD']
    variable = StringVar(root)
    variable.set('BTC-USD')

    def prdt():
        coin=variable.get()
        code(str(coin))

    w = OptionMenu(root, variable, *choices)
    w.pack(pady=100)
    def open_url():
        webbrowser.open("https://en.wikipedia.org/wiki/Cryptocurrency")
    predict=Button(root,text="predict" ,command=prdt).pack()
    crypto = Button(root, text="about crypto currency!", command=open_url).pack()
    root.mainloop()

window.mainloop()
