import smtplib
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()

s.login("ayushkumar.tiwari@gmail.com", "burningdesire")


    # message
message1 = "accuracy is less than 90%"
    

    # sending the mail 
s.sendmail("ayushkumar.tiwari@gmail.com", "1706309@kiit.ac.in", message1)
    

    # terminating the session 
s.quit()