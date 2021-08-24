import imaplib    # Module that allows us to open our inbox
import xlrd   # Module that allows us to work with XLSX files (version 1.2.0)
import os    # Module that allows us to work with directories dynamically

n=0
host = 'imap.gmail.com'    # Define the gmail imap server

fileName = input("Please enter the exact name of the corresponding excel file: ")     # Open the corresponding excel file
sheetName = input("Please enter the exact name of the worksheet: ")
dir = os.getcwd()
filePath = dir+"\\"+fileName+".xlsx"
sheet = xlrd.open_workbook(filePath)
hoja = sheet.sheet_by_name(sheetName)

for i in range(1, hoja.nrows):
    username = hoja.cell_value(i, 0)    # Get the necessary values from the determined cells
    password = hoja.cell_value(i, 1)
    mail = imaplib.IMAP4_SSL(host)    # Establish the connection with the server
    mail.login(username, password)    # Log in and access the inbox
    mail.select("inbox")
    result, search_data = mail.search(None, 'UNSEEN')    # Get only unread messages
    for num in search_data[0].split():    # Show how many unread messages are in each email account
        n+=1
    if n>10:
        print("\n- You have "+str(n)+" unread message/s in your email ▶️  "+username+":"+" 📧"*n+" ❗")
    elif n!=0:
        print("\n- You have "+str(n)+" unread message/s in your email ▶️  "+username+":"+" 📧"*n)
    else:
        print("\n- You have any unread messages in your email ▶️  "+username)
    n=0