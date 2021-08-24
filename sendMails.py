# ---https://www.youtube.com/watch?v=6DD4IOHhNYo

import smtplib    # Module that allows us to send emails
from email.mime.text import MIMEText    # Module that allows us to modify the mail body
from email.mime.multipart import MIMEMultipart    # Module that allows us to modify the mail parameters
import xlrd   # Module that allows us to work with XLSX files (version 1.2.0)
import os    # Module that allows us to work with directories dynamically

to_emails = []

fileName = input("Please enter the exact name of the corresponding excel file: ")    # Ask for the necessary data
sheetName = input("Please enter the exact name of the worksheet: ")
header = input("Are you going to use a header in your excel file? (Y/N): ").lower()
if header.startswith("y"):
    header = 1
else:
    header = 0

dir = os.getcwd()
filePath = dir+"\\"+fileName+".xlsx"    # Open the corresponding excel file
sheet = xlrd.open_workbook(filePath)
hoja = sheet.sheet_by_name(sheetName)

username = hoja.cell_value(header, 0)    # Get the necessary values from the determined cells
password = hoja.cell_value(header, 1)
from_email = hoja.cell_value(header, 4)+" <"+username+">"
for i in range(header, hoja.nrows):
    to_emails.append(hoja.cell_value(i, 2))
subject = hoja.cell_value(header, 3)
text = hoja.cell_value(header, 5)

def send_mail():
    assert isinstance(to_emails, list)    # Check if the specified object is of the specified type
    msg = MIMEMultipart('alternative')    # Indicate a standard type to work with the parameters offered by the library
    msg['From'] = from_email
    msg['To'] = ", ".join(to_emails)
    msg['Subject'] = subject
    txt_part = MIMEText(text, 'plain')    # Indicate the content of the body of the email, both in plain format and HTML
    msg.attach(txt_part)
    if hoja.cell_value(1,6) != "":
        textHTML = hoja.cell_value(header, 6)
        html_part = MIMEText(textHTML, 'html')
        msg.attach(html_part)
    server = smtplib.SMTP(host='smtp.gmail.com', port=587)    # Connection with the SMTP mail server
    server.ehlo()
    server.starttls()    # Encrypt the connection with the server (necessary because it is port 587)
    server.login(username, password)    # Login to server
    try:
        server.sendmail(from_email, to_emails, msg.as_string())    # Send the predefined message as a string
        print("Mail sent successfully!")
    except:
        print("An error occurred while sending the mail!")
    server.quit()    # Disconnect from SMTP server

send_mail()    # Execute the main function