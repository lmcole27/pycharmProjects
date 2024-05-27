##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv
import pandas as pd
import datetime as dt
import random as r
import smtplib

now = dt.datetime.now()
letters = ["letter_templates/letter_1.txt", "letter_templates/letter_2.txt", "letter_templates/letter_3.txt"]
sender_email = "lindacolenl@gmail.com"
password = "njgiekjdhmmggklx"

#Add Birthdays to dataframe
saved_b_days = pd.read_csv("birthdays.csv")


birthdays = {
    "name": ["Sexy Man", "Yo Mama", "La Maman"],
    "email": ["lindacolenl@gmail.com", "lmcole27@yahoo.ca", "lmcole27@yahoo.ca"],
    "year": [2000, 1999, 1998],
    "month": [3, 3, 3],
    "day": [10, 5, 30]
}
df = pd.DataFrame(birthdays)
yo_b_day = pd.DataFrame([['LC', "lindacolenl@gmail.com", 1979, 12, 27]],
                        columns=['name', 'email', "year", "month", "day"])

all_birthdays = pd.concat([saved_b_days, df, yo_b_day])
all_birthdays.to_csv("birthdays.csv")

find_month = all_birthdays.loc[all_birthdays['month'] == now.month]
if not find_month.empty:
    find_day = find_month.loc[find_month["day"] == now.day]
    if not find_day.empty:
        for index, row in find_day.iterrows():
            letter = r.choice(letters)
            name = (row["name"])
            email = (row["email"])
            with open(letter, "r") as birthday_letter:
                your_letter = birthday_letter.read()
                new_letter = your_letter.replace("[NAME]", name)
                print(new_letter)
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=sender_email, password=password)
                connection.sendmail(
                    from_addr=sender_email,
                    to_addrs=email,
                    msg=(f"Subject: Birthday Message\n\n"
                         f"{new_letter}"))
    else:
        pass

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

# #FRENCHWORDS
# words = pd.read_csv("1000frenchwords.csv")
# #print(words)

# #could use randint or a counter
# print(words["French"][3])
# print(words["English"][3])