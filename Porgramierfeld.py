from MitarbeiterVerwaltung import Mitarbeiter

class Berechtigter(Mitarbeiter):
    def __init__(self, benutzername, passwort):
        super().__init__()
        self.benutzername = benutzername
        self.passwort = passwort

    def login(self):
        benutzername = input("Benutzername eingeben: ")
        passwort = input("Passwort eingeben: ")

        if benutzername == self.benutzername and passwort == self.passwort:
            print("Erfolgreich eingeloggt als berechtigter Benutzer.")
            self.berechtigter_menü()
        else:
            print("Falscher Benutzername oder Passwort. Zugriff verweigert.")

    def berechtigter_menü(self):
        while True:
            print("\nBerechtigter Menü:")
            print("1. Urlaubsanspruch berechnen")
            print("2. Mitarbeiter abrufen")
            print("3. Krankmeldung")
            print("4. Krankheitsstatus beenden")
            print("5. Prüfen ob Mitarbeiter krank ist")
            print("6. Krankheitstage abrufen")
            #print("7. Prüfen ob Mitarbeiter in Urlaub ist")
            print("7. Urlaubmeldung")
            print("8. Beenden")

            wahl = input("Wählen Sie eine Option (1-8): ")

            if wahl == '1':
                self.Uralubs_anspruch()
            elif wahl == '2':
                self.Mitarbeiter_abrufen()
            elif wahl == '3':
                self.ist_Krank()
            elif wahl == '4':
                self.krankheit_beendet()
            elif wahl == '5':
                self.ist_momentan_krank()
            elif wahl == '6':
                self.krankheitstage_abrufen()
           # elif wahl == '7':
            #    self.ist_Urlaub()
            elif wahl == '7':
                self.Urlaub_meldung()
            elif wahl == '8':
                print("Berechtigter-Modus beendet.")
                break
            else:
                print("Ungültige Auswahl. Bitte wählen Sie eine Option von 1 bis 8.")

class Admin(Berechtigter):
    def __init__(self):
        super().__init__("admin", "pass123")
        self.berechtigte_benutzer = {}

    def login(self):
        benutzername = input("Benutzername eingeben: ")
        passwort = input("Passwort eingeben: ")

        if benutzername == self.benutzername and passwort == self.passwort:
            print("Erfolgreich eingeloggt als Admin.")
            self.admin_menü()
        else:
            print("Falscher Benutzername oder Passwort. Zugriff verweigert.")

    def admin_menü(self):
        while True:
            print("\nAdmin Menü:")
            print("1. Mitarbeiter hinzufügen")
            print("2. Mitarbeiter löschen")
            print("3. Berechtigten Benutzer hinzufügen")
            print("4. Beenden")

            wahl = input("Wählen Sie eine Option (1-4): ")

            if wahl == '1':
                self.hinzufügen()
            elif wahl == '2':
                self.Mitarbeiter_löschen()
            elif wahl == '3':
                self.berechtigter_hinzufügen()
            elif wahl == '4':
                print("Admin-Modus beendet.")
                break
            else:
                print("Ungültige Auswahl. Bitte wählen Sie eine Option von 1 bis 4.")

    def berechtigter_hinzufügen(self):
        benutzername = input("Benutzername für den berechtigten Benutzer eingeben: ")
        passwort = input("Passwort für den berechtigten Benutzer eingeben: ")
        self.berechtigte_benutzer[benutzername] = passwort
        print("Berechtigter Benutzer hinzugefügt.")

if __name__ == "__main__":
    print("Willkommen! Sind Sie ein Admin oder ein berechtigter Benutzer?")
    rolle = input("Admin/Benutzer: ").lower()

    if rolle.lower() == 'admin':
        admin = Admin()
        admin.login()
    elif rolle.lower() == 'benutzer':
        benutzername = input("Benutzername eingeben: ")
        passwort = input("Passwort eingeben: ")
        berechtigter = Berechtigter(benutzername, passwort)
        berechtigter.login()
    else:
        print("Ungültige Eingabe. Bitte wählen Sie zwischen 'Admin' und 'Benutzer'.")