# Element Hair – Website

One-Page-Website für den Friseursalon **Element Hair**, Schloßstraße 7, 87527 Sonthofen.
Adresse: **https://elementhair-sonthofen.de**

- **Domain:** IONOS
- **Hosting:** GitHub Pages (kostenlos)
- **Veröffentlichung:** automatisch bei jedem Upload auf den Branch `main`

---

## Anleitung: Website live stellen

Insgesamt etwa **20 Minuten Arbeit** und danach **bis zu 24 Stunden Wartezeit**, meist geht es in unter einer Stunde.

> **Wichtig:** Die Lovable-Seite erst ganz am Ende abmelden (Teil 4). Sonst ist die Website zwischendurch offline.

### Teil 1 – GitHub Pages einschalten (ca. 3 Minuten)

1. Öffne <https://github.com/selcuk27s/ElementHair> und melde dich an.
2. Klicke oben in der Leiste des Repositorys auf **⚙ Settings**. Das ist der letzte Reiter rechts neben „Code“, „Issues“, „Actions“ …
3. Klicke links in der Seitenleiste unter „Code and automation“ auf **Pages**.
4. Unter **Build and deployment** → **Source** im Auswahlfeld **GitHub Actions** wählen. Nicht „Deploy from a branch“.
5. Oben auf **Actions** klicken. Links **Website veröffentlichen** wählen, dann rechts auf **Run workflow** → grüner Button **Run workflow** klicken.
6. Etwa 1 Minute warten, bis der Lauf einen **grünen Haken** ✅ hat.
   - Bei rotem ✖: den Lauf anklicken → oben rechts **Re-run all jobs**.
7. Zurück zu **Settings → Pages**. Oben steht jetzt **„Your site is live at https://selcuk27s.github.io/ElementHair/“**.
8. **Test:** Die Adresse öffnen und prüfen, ob Fotos, Kevin-Murphy-Produkte und Bewertungen erscheinen.

### Teil 2 – Domain bei GitHub bestätigen (empfohlen, ca. 5 Minuten)

Das schützt die Domain davor, dass jemand anderes sie auf GitHub für sich einträgt.

1. Bei GitHub oben rechts auf dein **Profilbild** → **Settings**. Das sind die Einstellungen deines Kontos, nicht die des Repositorys.
2. Links unter „Code, planning, and automation“ auf **Pages** klicken.
3. **Add a domain** → `elementhair-sonthofen.de` eingeben → **Add domain**.
4. GitHub zeigt jetzt einen **TXT-Eintrag** mit zwei Werten an:
   - einen **Namen** wie `_github-pages-challenge-selcuk27s`
   - einen **Wert**, eine lange Zeichenfolge
   Dieses Fenster offen lassen.
5. In einem neuen Tab bei IONOS einen TXT-Eintrag anlegen (so geht es, siehe Teil 3, Schritte 1–3):
   - **Typ:** TXT
   - **Hostname:** der Name von GitHub **ohne** die Domain, also `_github-pages-challenge-selcuk27s`
   - **Wert:** die Zeichenfolge von GitHub
6. Speichern, 5–10 Minuten warten, dann bei GitHub auf **Verify** klicken.

### Teil 3 – DNS bei IONOS umstellen (ca. 10 Minuten)

1. Auf <https://login.ionos.de> anmelden. Achtung: nicht der Website-Baukasten unter `presence.ionos.de`.
2. Oben im Menü auf **Domains & SSL**, dann in der Liste auf **elementhair-sonthofen.de** klicken.
3. Den Reiter **DNS** öffnen. Du siehst eine Tabelle mit Einträgen (Typ, Hostname, Wert).
4. **Lovable-Einträge löschen** (Mülleimer-Symbol bzw. ⋮ → Löschen):
   - **A**-Einträge mit Hostname `@` und `www`, die auf Lovable zeigen, z. B. Wert `185.158.133.1`
   - **AAAA**-Einträge mit Hostname `@` oder `www`
   - **TXT**-Einträge, die mit `_lovable` beginnen oder `lovable` im Wert haben
   - **CNAME**-Eintrag für `www`, falls vorhanden
   - **Nicht anfassen:** Einträge vom Typ **MX** und TXT-Einträge mit `spf`. Die gehören zu E-Mail-Postfächern.
5. **Neue Einträge anlegen** mit **Eintrag hinzufügen** (bzw. **Record hinzufügen**). Jeden Eintrag einzeln speichern.

   | Typ | Hostname | Zeigt auf / Wert | TTL |
   |---|---|---|---|
   | A | `@` | `185.199.108.153` | 1 Stunde |
   | A | `@` | `185.199.109.153` | 1 Stunde |
   | A | `@` | `185.199.110.153` | 1 Stunde |
   | A | `@` | `185.199.111.153` | 1 Stunde |
   | CNAME | `www` | `selcuk27s.github.io` | 1 Stunde |

   - Fragt IONOS beim Speichern, ob die **Verwendungsart** bzw. das **Ziel der Domain** geändert werden soll, mit **Ja** bestätigen.
   - Hat die Domain eine **Weiterleitung** eingestellt, diese unter **Verwendungsart anpassen** aufheben, sonst greifen die Einträge nicht.
6. **Domain bei GitHub eintragen:**
   - GitHub → Repository **ElementHair** → **Settings** → **Pages**.
   - Unter **Custom domain** `elementhair-sonthofen.de` eingeben (ohne `https://` und ohne `www`) und **Save** klicken.
   - Es erscheint „DNS check in progress“. Sobald **„DNS check successful“** dasteht, geht es weiter. Das dauert Minuten bis Stunden. Die Seite ab und zu neu laden.
7. **Haken bei „Enforce HTTPS“ setzen.**
   - Ist der Haken grau, ist das Sicherheitszertifikat noch nicht fertig.
   - Bis zu 24 Stunden warten und dann erneut versuchen.

### Teil 4 – Prüfen und Lovable abmelden

1. **Test im Inkognito-Fenster:**
   - `https://elementhair-sonthofen.de` öffnen. Es muss die neue Seite erscheinen.
   - `https://www.elementhair-sonthofen.de` muss auf dieselbe Seite führen.
   - Das Schloss-Symbol in der Adresszeile muss da sein.
2. **Test auf dem Handy:** Seite aufrufen, „Anrufen“ antippen, Diashow wischen.
3. **Erst jetzt** in Lovable unter **Settings → Domains** die Domain entfernen und das Projekt auf „nicht veröffentlicht“ stellen. Das Projekt selbst als Sicherung behalten.

### Wenn etwas nicht klappt

| Problem | Lösung |
|---|---|
| Es erscheint noch die alte Lovable-Seite | Der Browser hat die alte Seite gespeichert. Im Inkognito-Fenster öffnen oder 1–2 Stunden warten. In Teil 3 prüfen, ob wirklich alle Lovable-Einträge gelöscht sind. |
| „DNS check unsuccessful“ bei GitHub | In Teil 3 Schritt 5 prüfen: genau 4 A-Einträge für `@` und **kein** AAAA-Eintrag für `@`. Dann 1 Stunde warten und bei GitHub auf **Check again** klicken. |
| „404 – There isn't a GitHub Pages site here“ | Unter **Actions** prüfen, ob der letzte Lauf grün ist. Sonst **Re-run all jobs**. Unter **Settings → Pages** muss die Custom domain eingetragen sein. |
| Fotos oder Schriften fehlen | Unter **Actions** prüfen, ob der letzte Lauf grün ist. Der Inhalt kommt immer aus dem Ordner `website/`. |
| „Enforce HTTPS“ ist grau | Bis zu 24 Stunden warten. Danach die Custom domain einmal entfernen, neu eintragen und speichern. |

---

## Nach dem Livegang

- [ ] **Bewerbungsformular verbinden:**
  1. Auf <https://web3forms.com> mit `eda.elementhair@gmail.com` einen kostenlosen Zugangsschlüssel anfordern.
  2. In `index.html` bei `WEB3FORMS_KEY = ""` eintragen.
  3. `python3 build.py` ausführen und hochladen.
  Ohne Schlüssel verschickt das Formular nichts.
- [ ] **Google Search Console:**
  1. Auf <https://search.google.com/search-console> eine Property vom Typ **Domain** für `elementhair-sonthofen.de` anlegen.
  2. Den angezeigten TXT-Eintrag bei IONOS anlegen (wie in Teil 2).
  3. Unter **Sitemaps** `sitemap.xml` einreichen.
- [ ] **Google-Unternehmensprofil:** Die Website `https://elementhair-sonthofen.de` eintragen.
- [ ] **Tempo messen:** Auf <https://pagespeed.web.dev> die Adresse eingeben.
- [ ] **Datenschutz:** Die Datenschutzerklärung nennt bereits GitHub Pages als Hosting und Web3Forms für Bewerbungen. Bei einem Wechsel des Hostings diesen Absatz anpassen.
- [ ] **Stellen besetzt?** Die beiden `JobPosting`-Einträge in `index.html` löschen (Google-Jobsuche).

---

## Änderungen machen

1. `index.html` bearbeiten.
2. Im Ordner dieses Projekts ausführen:

   ```bash
   python3 build.py
   ```

3. Änderungen auf GitHub hochladen (`git add -A`, `git commit`, `git push`). GitHub veröffentlicht automatisch in 1–2 Minuten.

| Pfad | Inhalt |
|---|---|
| `website/` | **Die veröffentlichte Website.** Wird von `build.py` erzeugt. |
| `index.html` | Quelle der Seite |
| `bilder/` | Salon-, Team- und Arbeitsfotos |
| `og-image.jpg` | Vorschaubild für Google, WhatsApp und Facebook |
| `llms.txt` | Steckbrief für KI-Assistenten |
| `build.py` | Erzeugt `website/` |
| `.github/workflows/pages.yml` | Automatische Veröffentlichung auf GitHub Pages |

### Alternative: IONOS-Webhosting statt GitHub Pages

Wer die Seite auf Servern in Deutschland haben möchte, bucht ein IONOS-Webhosting-Paket. Dann:

1. Den Inhalt von `website/` per **Webspace Explorer** oder **SFTP** in einen Ordner laden.
2. Unter **Domains & SSL** die Domain auf diesen Ordner zeigen lassen und das SSL-Zertifikat zuweisen.
3. Die GitHub-DNS-Einträge aus Teil 3 wieder entfernen.
4. In der Datenschutzerklärung GitHub durch IONOS ersetzen.
