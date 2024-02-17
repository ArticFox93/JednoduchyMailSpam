import smtplib

# https://github.com/ArticFox93
# ------------veci na doplneni------------------
MY_MAIL = "tvuj email"
# HESLO MUSI BYT VYGENEROVANO POMOCI APP PASSWORD, staci vygooglit "app password {tvuj mail}" a postupovat podle navodu
MY_PASSWORD = "tvoje heslo"
# ----------------------------------------------

mail_zprava_subject = input("Nazev zpravy: ")
mail_zprava = input("Zprava, kterou odesles: ")
komu = input("Mail, na ktery se to odesle: ")
kolikrat = int(input("Kolik mailu se ma poslat?: "))

try:
    poslano = 0
    for mail in range(kolikrat):
        poslano += 1
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(MY_MAIL, MY_PASSWORD)
            connection.sendmail(from_addr=MY_MAIL, to_addrs=komu, msg=f"Subject:{mail_zprava_subject}\n\n{mail_zprava}")
        print(f"{poslano}. mail poslan")
    print("Uspesne dokonceno")
except:
    print("nekde se vyskytnula chyba")