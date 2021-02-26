from Megatlon import Megatlon
import time
import schedule

# ATENCION: Abrir Read Me para ver las distintas opciones de este codigo
user = Megatlon("user@mail.com", "password")

schedule.every().monday.at("9").do(user.reserve_class, "Megatlon Sede", "dia", "clase", "hora")     # Lunes
schedule.every().tuesday.at("9").do(user.reserve_class, "Megatlon Sede", "dia", "clase", "hora")     # Martes
schedule.every().wednesday.at("9").do(user.reserve_class, "Megatlon Sede", "dia", "clase", "hora")     # Miercoles
schedule.every().thursday.at("9").do(user.reserve_class, "Megatlon Sede", "dia", "clase", "hora")     # Jueves
schedule.every().friday.at("9").do(user.reserve_class, "Megatlon Sede", "dia", "clase", "hora")     # Viernes
schedule.every().saturday.at("9").do(user.reserve_class, "Megatlon Sede", "dia", "clase", "hora")     # Sabado
schedule.every().sunday.at("9").do(user.reserve_class, "Megatlon Sede", "dia", "clase", "hora")     # Domingo

while True:
    schedule.run_pending()
    time.sleep(1)
