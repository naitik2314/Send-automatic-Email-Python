import os
import random
import smtplib


def automatic_email():
    user = input("Enter Your Name >>: ")
    email = input("Enter Your Email >>: ")
    message = (f"Dear {user}, You are on Naitik's mailing list")
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("Your email here", "email password here")
    s.sendmail('&&&&&&&&&&&', email, message)
    print("Email Sent!")
    
automatic_email()