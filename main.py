import datetime as dt
import smtplib
import random

MY_EMAIL = 'mike.test.2424@gmail.com'
MY_PASSWORD = 'pxrt sqnz mqjq kaxc'
now = dt.datetime.now()
day_of_the_week = now.weekday()

if day_of_the_week == 3:
    with open('./quotes.txt') as data:
        content = data.readlines()

    with smtplib.SMTP(host='smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs='miketest2424@yahoo.com',
            msg=f'Subject: Monday Motivation Quote\n\n{random.choice(content)}')
