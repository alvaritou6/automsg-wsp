import pyautogui as pg
from time import sleep
from tkinter import messagebox as MessageBox

print('It is of utmost importance that you read the README.MD file before proceeding.\n\n\n')

msg = input("Enter the message to be sent: ")
cant = input("Enter the number of times you want to send the message: ")

if cant.isdigit():
    cant = int(cant)
    sleep(1)
    print('\n\nPlease switch the window to WhatsApp. \nIn 10 seconds messages will start to be sent.')

    sleep(10)

    for i in range(cant):
        pg.write(msg)
        pg.press('enter')

    MessageBox.showinfo("Atention!", "The sending of messages has been completed.")
else:
    print('\n\nWhat you have entered is not a number! You must enter ONLY a number.\nTry again.')


