import smtplib
import ssl
from tkinter import *
from tkinter import ttk

from PIL import Image, ImageTk
from ttkthemes import ThemedTk

import os

prev_len = 1


# --- Begin Program --- #
def start():

    def step():
        count_down['value'] += 20

    def step_down():
        if float(count_down['value']) > 0:
            count_down['value'] -= 20

    def pop_up(text):

        def restart():
            popup.destroy()
            start()

        def email_pad():

            # content = text
            # port = 465
            # context = ssl.create_default_context()
            # user_email = email_input.get('1.0', END)
            #
            # with smtplib.SMTP_SSL("smtp.gmail.com", port=port, context=context) as server:
            #     server.login("dangernotepad@gmail.com", os.environ['password'])
            #     server.sendmail(from_addr="dangernotepad@gmail.com", to_addrs=user_email, msg=content)

            popup.destroy()
            root.destroy()

        popup = Toplevel(root)
        popup.geometry("400x100")
        popup.config(padx=10, pady=20)
        popup.grid()

        email_label = Label(popup, text="Email:")
        email_label.grid(row=0, column=0)

        email_input = Text(popup)
        email_input.config(height=1, width=40, font=('Kalinga', 10))
        email_input.grid(row=0, column=1, columnspan=2)

        email_button = ttk.Button(popup, text="Email Notepad", width=20, command=email_pad)
        email_button.grid(row=1, column=1, pady=10)

        restart_button = ttk.Button(popup, text='Restart', width=20, command=restart)
        restart_button.grid(row=1, column=2)

    def check_len():
        global prev_len

        pad_len = len(notepad.get('1.0', END))
        if pad_len == prev_len:
            step()
            if float(count_down['value']) == 100:
                text = notepad.get('1.0', END)
                pop_up(text)
                notepad.delete('1.0', END)
            else:
                root.after(1000, check_len)
        else:
            prev_len = pad_len
            step_down()
            root.after(1000, check_len)

    start_button.grid_forget()
    logo_bg.grid_forget()

    notepad = Text(root)
    notepad.config(width=50, height=15, bg='white', font=('Kalinga', 20))
    notepad.grid(row=0, column=1, padx=30, pady=20)
    notepad.focus()

    count_down = ttk.Progressbar(root, orient='vertical', mode='determinate', length=500)
    count_down.grid(row=0, column=2, padx=30, pady=50)

    root.after(1000, check_len)

    root.mainloop()


# --- Set-up main window --- #
root = ThemedTk(theme='Equilux')
root.title('DangerPad')
root.geometry("1000x700")
root.config(pady=10, padx=60, bg='#f7f7f7')

# --- Start Page --- #
logo = ImageTk.PhotoImage(Image.open('explosion.png'))
logo_bg = Label(root, image=logo, borderwidth=0, highlightthickness=0)
logo_bg.grid(row=0, column=1)

start_button = ttk.Button(text='START', width=20, command=start)
start_button.grid(row=0, column=1, padx=260, pady=350, ipady=10)

root.mainloop()
