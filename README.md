Run_Code:

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













Zweite Code:
import datetime
import os

class Mitarbeiter:
    def __init__(self):
        self.krank = "Nein"
        self.in_Urlaub = "Nein"
        self.Karanktagekonto = 0
        self.genomenen_urlaub = 0
    
    def hinzufügen(self):
        self.Personallnummer = input("Geben Sie Ihrem neuen Mitarbeiter eine Personalnummer: ")
        self.vorname = input("Bitte geben Sie den Vornamen des Mitarbeiters ein: ")
        self.name = input("Bitte geben Sie den Namen des Mitarbeiters ein: ")
        self.geburtsdatum = input("Bitte geben Sie das Geburtsdatum des Mitarbeiters ein: ")
        self.eintrittsdatum = input("Bitte geben Sie das Eintrittsdatum des Mitarbeiters ein: ")
        dateiname = f"{self.Personallnummer}.txt"
      
        mitarbeiter_daten = {
            'Personalnummer': self.Personallnummer, 'Vorname': self.vorname, 'Name': self.name,
            'Geburtsdatum': self.geburtsdatum, 'Eintrittsdatum': self.eintrittsdatum, 
            'Krankentageskonto': self.Karanktagekonto, 'Krank': self.krank,
            'genomenen_urlaub': self.genomenen_urlaub, 'in_Urlaub': self.in_Urlaub
        }

        with open(dateiname, 'w+') as mitarbeiter_datei:
            aktuelles_datum = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            mitarbeiter_datei.write(f"Der Mitarbeiter wurde am {aktuelles_datum} hinzugefeugt \n")
            for attribut, wert in mitarbeiter_daten.items():
                mitarbeiter_datei.write(f"{attribut}: {wert}\n")

    def Uralubs_anspruch(self):
     Datei = input("geben Sie Personalnummer ein:")
     dateiname = f"{Datei}.txt"
     Schlüsselwort = "Eintrittsdatum:"
     vorname1 = "Vorname:"
     name1 = "Name:"
     Geburtsdatum1 = "Geburtsdatum:"

     with open(dateiname, 'r') as Data:
          for Zeile in Data:
            if vorname1 in Zeile:
                vorname = Zeile.split(vorname1)[1].strip()
            if name1 in Zeile:
                nachname = Zeile.split(name1)[1].strip()
            if Geburtsdatum1 in Zeile:
                Geburtsdatum = Zeile.split(Geburtsdatum1)[1].strip()
         
            if Schlüsselwort in Zeile:
                Eintrittsdatum = Zeile.split(Schlüsselwort)[1].strip()
                Startdatum_obj = datetime.datetime.strptime(Eintrittsdatum, "%Y.%m.%d")
                heutigesdatum = datetime.datetime.now()
                Tage = (heutigesdatum - Startdatum_obj).days
                print("Anzahl der Tage ist:", Tage)
                Urlaup_pro_Tag = 2.5 / 30
                Urlaupsanpruch = int(Urlaup_pro_Tag * Tage)
                with open(dateiname, 'r') as file:
                    for line in file:
                        if "genomenen_urlaub:" in line:
                            genommener_urlaub = int(line.split(":")[1].strip())
                            Urlaupsanpruch -= genommener_urlaub
                print(f"Der Mitarbeiter {vorname} {nachname} mit dem Geburtsdatum: {Geburtsdatum}")  
                print(f"hat {Urlaupsanpruch} Tage Urlaubsanspruch")
                 
    def Mitarbeiter_abrufen(self):
        Personallnummer = input("Geben Sie die Personalnummer des Mitarbeiters ein: ")
        dateiname = f"{Personallnummer}.txt"

        with open(dateiname, 'r') as Datei:
            for Daten in Datei:
                print(Daten)

    def Mitarbeiter_löschen(self):
        Dateiname1 = input("Geben Sie die Personalnummer des zu löschenden Mitarbeiters ein: ")
        Dateiname = f"{Dateiname1}.txt"
        if os.path.exists(Dateiname):
            Sicherheitsfrage = input(f"Sind Sie sicher, dass Sie den Mitarbeiter mit der Personalnummer {Dateiname1} löschen möchten? (ja/nein): ")
            if Sicherheitsfrage.lower() == 'ja':
                os.remove(Dateiname)
                print(f"Der Mitarbeiter mit der Personalnummer {Dateiname} wurde gelöscht")
            else:
                print("Löschvorgang abgebrochen.")
        else:
            print(f"Der Mitarbeiter mit der Personalnummer {Dateiname1} wurde nicht gefunden.")
 
    def ist_Krank(self):
     Erkrankte = input("Geben Sie die Personalnummer des erkrankten Mitarbeiters ein:")
     Erkrankte_mitarbeiter = f"{Erkrankte}.txt"
     Beginn_datum = input("Geben Sie das Beginn Datum in folgendem Format (YYYY.MM.DD) ein:")
     Krankbis = input("Geben Sie das Ende Datum in folgendem Format (YYYY.MM.DD) ein:")
     Kranktege_beginn = datetime.datetime.strptime(Beginn_datum, "%Y.%m.%d")
     Kranktege_ende = datetime.datetime.strptime(Krankbis, "%Y.%m.%d")
    
     try:
        Kranktege_beginn = datetime.datetime.strptime(Beginn_datum, "%Y.%m.%d")
        Kranktege_ende = datetime.datetime.strptime(Krankbis, "%Y.%m.%d")
     except ValueError:
        print("Falsches Datumsformat!")
        return
    
     krankentage = 0
     with open(Erkrankte_mitarbeiter, 'r') as file:
        lines = file.readlines()
        for index, line in enumerate(lines):
            if "Krankentageskonto:" in line:
                krankentage = int(line.split(":")[1].strip())
                lines[index] = f"Krankentageskonto: {krankentage + (Kranktege_ende - Kranktege_beginn).days}\n"

     with open(Erkrankte_mitarbeiter, 'w') as file:
        file.writelines(lines)
    
    def krankheit_beendet(self):
        Erkrankte = input("Geben Sie die Personalnummer des Mitarbeiters ein:")
        dateiname = f"{Erkrankte}.txt"

        if not os.path.exists(dateiname):
            print("Mitarbeiterdatei nicht gefunden.")
            return

        with open(dateiname, 'r') as file:
            lines = file.readlines()

        with open(dateiname, 'w') as file:
            for line in lines:
                if "Krank: Ja" in line:
                    line = line.replace("Krank: Ja", "Krank: Nein")
                file.write(line)
        
        print(f"Der Krankheitsstatus des Mitarbeiters mit der Personalnummer {Erkrankte} wurde auf 'Krank: Nein' geändert.")

    def ist_momentan_krank(self):
        Personallnummer = input("Geben Sie die Personalnummer des Mitarbeiters ein: ")
        dateiname = f"{Personallnummer}.txt"

        if not os.path.exists(dateiname):
            print("Mitarbeiterdatei nicht gefunden.")
            return

        with open(dateiname, 'r') as file:
            for line in file:
                if "Krank: Ja" in line:
                    print(f"Der Mitarbeiter mit der Personalnummer {Personallnummer} ist momentan krank.")
                    return
        
        print(f"Der Mitarbeiter mit der Personalnummer {Personallnummer} ist momentan nicht krank.")

    def krankheitstage_abrufen(self):
        Personallnummer = input("Geben Sie die Personalnummer des Mitarbeiters ein: ")
        dateiname = f"{Personallnummer}.txt"

        if not os.path.exists(dateiname):
            print("Mitarbeiterdatei nicht gefunden.")
            return

        krankentage = 0
        with open(dateiname, 'r') as file:
            for line in file:
                if "Krankentageskonto:" in line:
                    krankentage = int(line.split(":")[1].strip())
                    break
        
        print(f"Der Mitarbeiter mit der Personalnummer {Personallnummer} war insgesamt {krankentage} Tage krank.")
        return krankentage

    def ist_Urlaub(self):
        Beuralubt = input("Geben Sie die Personalnummer des erkrankten Mitarbeiters ein:")
        Beuralubt_mitarbeiter = f"{Beuralubt}.txt"
        Beginn_datum = input("Geben Sie das Beginn Datum in folgendem Format (YYYY.MM.DD) ein:")
        Urlab_bis = input("Geben Sie das Endedatum in folgendem Format (YYYY.MM.DD) ein:")
        Urlaub_beginn = datetime.datetime.strptime(Beginn_datum, "%Y.%m.%d")
        Urlaub_ende = datetime.datetime.strptime(Urlab_bis, "%Y.%m.%d")
        
        try:
            Urlaub_beginn = datetime.datetime.strptime(Beginn_datum, "%Y.%m.%d")
            Urlaub_ende = datetime.datetime.strptime(Urlab_bis, "%Y.%m.%d")
        except ValueError:
            print("Falsches Datumsformat!")
            return
        
        with open(Beuralubt_mitarbeiter, 'r') as file:
            lines = file.readlines()
        
        urlaubstage = 0
        with open(Beuralubt_mitarbeiter, 'w') as file:
            for line in lines:
                if "genomenen_urlaub:" in line:
                    urlaubstage = int(line.split(":")[1].strip())
                    urlaubstage_berechnung = (Urlaub_ende - Urlaub_beginn).days
                    genomenen_urlaub = urlaubstage + urlaubstage_berechnung
                    line = f"genomenen_urlaub: {genomenen_urlaub}\n"
                file.write(line)
        
        with open(Beuralubt_mitarbeiter, 'w') as file:
            for line in lines:
                if "in_Urlaub: Nein" in line:
                    line = line.replace("in_Urlaub: Nein", "in_Urlaub: Ja")
                    file.write(line)
    def Urlaub_meldung(self):
     Beurlaubt = input("Geben Sie die Personalnummer des erkrankten Mitarbeiters ein:")
     Beurlaubt_mitarbeiter = f"{Beurlaubt}.txt"
     Beginn_datum = input("Geben Sie das Beginn Datum in folgendem Format (YYYY.MM.DD) ein:")
     Urlaub_bis = input("Geben Sie das Ende Datum in folgendem Format (YYYY.MM.DD) ein:")
     Urlaub_beginn = datetime.datetime.strptime(Beginn_datum, "%Y.%m.%d")
     Urlaub_ende = datetime.datetime.strptime(Urlaub_bis, "%Y.%m.%d")
    
     try:
        Urlaub_beginn = datetime.datetime.strptime(Beginn_datum, "%Y.%m.%d")
        Urlaub_ende = datetime.datetime.strptime(Urlaub_bis, "%Y.%m.%d")
     except ValueError:
        print("Falsches Datumsformat!")
        return
    
     urlaubstage = 0
     with open(Beurlaubt_mitarbeiter, 'r') as file:
        lines = file.readlines()

     with open(Beurlaubt_mitarbeiter, 'w') as file:
        for line in lines:
            if "genomenen_urlaub:" in line:
                urlaubstage = int(line.split(":")[1].strip())
                urlaubstage_berechnung = (Urlaub_ende - Urlaub_beginn).days
                genommenen_urlaub = urlaubstage + urlaubstage_berechnung
                line = f"genomenen_urlaub: {genommenen_urlaub}\n"
            file.write(line)
    
        
if __name__ == "__main__":
    bearbeitung = Mitarbeiter()
    bearbeitung.hinzufügen()
    bearbeitung.Uralubs_anspruch()
    bearbeitung.Mitarbeiter_abrufen()
    bearbeitung.Mitarbeiter_löschen()
    bearbeitung.ist_Krank()
    bearbeitung.krankheit_beendet()
    bearbeitung.ist_momentan_krank()
    bearbeitung.krankheitstage_abrufen()
    bearbeitung.ist_Urlaub()
    bearbeitung.Urlaub_meldung()

        
