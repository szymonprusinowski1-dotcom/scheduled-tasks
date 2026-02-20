import pandas as pd
import random
import smtplib
import datetime as dt

MY_EMAIL = "szymosprusinos@gmail.com"
PASSWORD = "wgwvavxfmqgagygd"

NOW = dt.datetime.now()
CURRENT_MONTH = NOW.month
CURRENT_DAY = NOW.day

data = pd.read_csv("birthdays.csv")
data_dict = data.to_dict(orient="records")

letters = []
with open("letter_1.txt") as l_1:
    letter_1 = l_1.read()
    letters.append(letter_1)
with open("letter_2.txt") as l_2:
    letter_2 = l_2.read()
    letters.append(letter_2)
with open("letter_3.txt") as l_3:
    letter_3 = l_3.read()
    letters.append(letter_3)

for d in data_dict:
    if d["day"] == CURRENT_DAY and d["month"] == CURRENT_MONTH:
        pick_letter = random.choice(letters)
        converted_letter = pick_letter.replace("[NAME]", f"{d["name"]}")
        with smtplib.SMTP_SSL("smtp.gmail.com", port=465) as connection:
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=f"{d["email"]}",
                msg=f"Subject:Birthday wishes\n\n{converted_letter}")
        print("E-mail sent.")





