# Element Hair – Website

One-Page-Website für den Friseursalon **Element Hair**, Schloßstraße 7, 87527 Sonthofen.
Ziel-Domain: `https://elementhair-sonthofen.de/`

## Ordner

| Pfad | Inhalt |
|---|---|
| `website/` | **Die fertige Website.** Genau dieser Ordnerinhalt kommt auf den Server. |
| `index.html` | Quelle der Seite (Vorschau-Fassung, wird bearbeitet) |
| `bilder/` | Salon-, Team- und Arbeitsfotos (WebP) |
| `og-image.jpg` | Vorschaubild für Google, WhatsApp und Facebook (1200 × 630) |
| `llms.txt` | Steckbrief für KI-Assistenten (ChatGPT, Perplexity …) |
| `build.py` | Erzeugt `website/` aus den Quelldateien |

Die Seite ist reines HTML/CSS/JavaScript. Es gibt keine Datenbank, kein PHP und kein CMS, daher passt sie auf jedes Webhosting.

## Änderungen machen

1. `index.html` bearbeiten (Texte, Bilder, Öffnungszeiten …).
2. Live-Fassung neu erzeugen:

   ```bash
   python3 build.py
   ```

3. Den Inhalt von `website/` hochladen (siehe unten).

Neue Fotos für die Diashow kommen in `bilder/` und werden in `index.html` in der Liste `SLIDES` eingetragen.

---

## Live stellen bei IONOS

Es gibt zwei Wege. **Weg A** ist der einfachste, wenn du bereits ein IONOS-Webhosting-Paket hast.
**Weg B** veröffentlicht automatisch bei jeder Änderung in diesem GitHub-Repository.

> IONOS ändert gelegentlich Menünamen. Wenn ein Punkt anders heißt, such im Kundenbereich nach dem Begriff in Klammern.

### Weg A – Webhosting-Paket (Dateien hochladen)

**1. Zugang zum Webspace**
- Auf <https://login.ionos.de> anmelden.
- **Hosting** → dein Paket → **Webspace** öffnen.
- Für den Upload per Programm unter **SFTP & SSH** (Zugänge) einen SFTP-Benutzer mit Passwort anlegen und den **Server-Namen** notieren.

**2. Dateien hochladen**
- *Im Browser:* Im **Webspace Explorer** einen Ordner anlegen, z. B. `elementhair`, und den **Inhalt** von `website/` hineinziehen: `index.html`, `robots.txt`, `sitemap.xml`, `llms.txt`, `og-image.jpg` und die Ordner `bilder/` und `fonts/`.
- *Oder mit FileZilla:* Server = Server-Name aus Schritt 1, Protokoll **SFTP**, Port **22**, dein SFTP-Benutzer und Passwort. Den Inhalt von `website/` in den Ordner `elementhair` kopieren.
- Wichtig: Hochgeladen wird der **Inhalt** von `website/`, nicht der Ordner selbst. `index.html` muss direkt im Zielordner liegen.

**3. Domain verbinden**
- **Domains & SSL** → `elementhair-sonthofen.de` → **Ziel/Verwendungsart anpassen** → **Webspace** → Ordner `elementhair` auswählen.
- Das Gleiche für `www.elementhair-sonthofen.de` (oder eine Weiterleitung von `www` auf die Hauptdomain einrichten).

**4. SSL (https) einschalten**
- Unter **Domains & SSL** → **SSL-Zertifikat** das im Paket enthaltene Zertifikat der Domain zuweisen.
- Prüfen, dass `http://` automatisch auf `https://` weitergeleitet wird (Einstellung „HTTPS-Weiterleitung“ bzw. „SSL erzwingen“).

**5. Warten und testen**
- DNS-Änderungen brauchen meist Minuten, manchmal bis zu 24 Stunden.
- Danach `https://elementhair-sonthofen.de` öffnen und prüfen: Fotos, Schriften, Karte (nach Zustimmung) und Anruf-Button auf dem Handy.

### Weg B – IONOS Deploy Now (automatisch aus GitHub)

1. <https://www.ionos.de/hosting/deploy-now> öffnen, anmelden und **GitHub verbinden**.
2. Dieses Repository auswählen.
3. Als Projektart **statische Seite ohne Framework** wählen und als Veröffentlichungsordner (Publish/Dist-Verzeichnis) **`website`** angeben. Einen Build-Befehl braucht es nicht.
4. Deploy Now legt einen GitHub-Workflow im Repository an und veröffentlicht die Seite zuerst unter einer Test-Adresse. Diese prüfen.
5. Im Deploy-Now-Projekt unter **Domain** `elementhair-sonthofen.de` verbinden. SSL wird automatisch eingerichtet.
6. Ab jetzt wird jede Änderung, die auf GitHub landet, automatisch veröffentlicht. Vorher immer `python3 build.py` ausführen.

---

## Domain von Lovable umziehen

`elementhair-sonthofen.de` zeigt im Moment auf die Lovable-Seite.

- **Ist die Domain bei IONOS registriert:** Schritt 3 oben stellt sie automatisch um.
- **Ist sie bei einem anderen Anbieter:** Dort die DNS-Einträge (A-Record und `www`-CNAME) auf die Werte setzen, die IONOS beim Verbinden der Domain anzeigt. Oder die Domain zu IONOS umziehen (Auth-Code beim alten Anbieter anfordern).
- In Lovable die eigene Domain erst entfernen, **wenn die neue Seite unter der Domain läuft**. Das Lovable-Projekt als Sicherung behalten.

## Nach dem Livegang

- [ ] **Bewerbungsformular verbinden:** Auf <https://web3forms.com> mit `eda.elementhair@gmail.com` einen kostenlosen Zugangsschlüssel holen und in `index.html` bei `WEB3FORMS_KEY = ""` eintragen. Danach `python3 build.py` ausführen und neu hochladen. Ohne Schlüssel verschickt das Formular nichts.
- [ ] **Datenschutzerklärung ergänzen:** IONOS als Hosting-Anbieter nennen (IONOS SE, Elgendorfer Str. 57, 56410 Montabaur) und Web3Forms als Formular-Dienst. Den Auftragsverarbeitungsvertrag (AVV) mit IONOS im Kundenbereich unter **Datenschutz** abschließen.
- [ ] **Google Search Console:** Domain bestätigen und `https://elementhair-sonthofen.de/sitemap.xml` einreichen.
- [ ] **Google-Unternehmensprofil:** Website-Adresse eintragen. Adresse, Telefon und Öffnungszeiten müssen genau wie auf der Website stehen.
- [ ] **Tempo messen:** <https://pagespeed.web.dev> mit der Live-Adresse.
- [ ] **Impressum und Datenschutz** öffnen sich als Fenster. Rechtlich sicherer sind eigene Unterseiten (wie bisher bei Lovable).
- [ ] **Stellenanzeigen:** Sind die Stellen besetzt, die beiden `JobPosting`-Einträge in `index.html` löschen (Google-Jobsuche).
