import pyautogui as pg
from time import sleep
from tkinter import messagebox as MessageBox

msg = input("Enter the message to be sent: ")
cant = int(input("Enter the number of times you want to send the message: "))
sleep(1)
print('\n\nPlease switch the window to WhatsApp. \nIn 10 seconds messages will start to be sent.')

sleep(10)

for i in range(cant):
    pg.write(msg)
    pg.press('enter')

MessageBox.showinfo("Atention!", "The sending of messages has been completed.")
