# Arbeitsblatt 1 — Think-Pair-Share: „Das erwartet dich 2028“ (gekürzte Original-AP1-Aufgabe)

**Klasse:** IFA6B · **Datum:** 15.09.26 · **Name:** Bohdan Klymov · **Team (Pair):** Daniel Popazu

**Doppelstunde:** KW 37 · **Lernfeld:** LF5 · **Zeit:** Think 10 min → Pair 12 min → Share 25 min

---

## ⚡ Kurzinfo: Deine Abschlussprüfung Teil 1 (AP1)

| Größe | Wert |
|---|---|
| Prüfungsbereich | **Einrichten eines IT-gestützten Arbeitsplatzes** (alle FI-Fachrichtungen) |
| Format | **4 ungebundene Aufgaben** (je 20–30 P), offene Antworten, Stichpunkte erlaubt |
| Zeit / Punkte | **90 Minuten / 100 Punkte** |
| Gewichtung | **20 %** der Gesamtprüfung |
| Dein Termin | **Frühjahr 2028** |
| Regeln | Nur die **ersten X geforderten Angaben** werden bewertet · Taschenrechner erlaubt |

---

## Ausgangssituation (gekürzt aus: IHK-ZPA Nord-West, AP1 Frühjahr 2026, Aufgabe 4 „Versandsoftware“)

> Du bist Auszubildender/Auszubildende im IT-Systemhaus **1234-IT OHG**. Für den Paketdienst **KurierKönig GmbH** soll eine **Versandsoftware** entwickelt werden, die die Versandkosten für Pakete berechnet. (In der Originalprüfung hieß das Systemhaus Novo.Sys.Tech OHG — der Aufgabenkern ist identisch.)

---

## Teilaufgabe a) — Kurzantwort (2 Punkte)

Die Versandsoftware kann **objektorientiert** oder **prozedural** programmiert werden.

**Nennen Sie zwei Vorteile objektorientierter Programmiersprachen gegenüber prozeduralen Programmiersprachen.**

> Hinweis (wie in der echten Prüfung): Es werden nur die **ersten zwei** genannten Vorteile bewertet.

1. Bessere Struktur und dadurch einfaches Verständnis/Lessbarer 
2. Man kann die Programme leichter erweitern

---

## Teilaufgabe b) — Versandkosten berechnen (10 Punkte)

Es soll eine Klasse **`ShippingCalculator`** erstellt werden, die die Berechnung der Versandkosten übernimmt. Im **Konstruktor** werden die Attribute mit folgenden Werten initialisiert:

| Attribut | Bedeutung | Wert |
|---|---|---|
| `maxWeight` | Maximales Gewicht eines Pakets (kg) | **31,5 ** |
| `expressSurcharge` | Zuschlag für Express-Sendung (€) | **12,95** |
| `upTo10kg` | Preis für ein Paket bis 10 kg (€) | **13,98** |
| `above10kg` | Preis für ein Paket über 10 kg (€) | **18,95** |

Die Frachtkosten werden mit folgender Funktion berechnet:

```
FUNCTION calculateShippingCost(packages)
    totalCost = 0
    FOR EACH package IN packages
        weight    = package["weight"]
        isExpress = package["isExpress"]

        IF weight > maxWeight THEN
            PRINT "Error: Package exceeds the maximum weight"
        ELSE
            IF weight <= 10 THEN
                cost = upTo10kg
            ELSE
                cost = above10kg
            END IF

            IF isExpress THEN
                cost = cost + expressSurcharge
            END IF

            totalCost = totalCost + cost
        END IF
    END FOR

    IF totalCost >= 40 THEN              // Rabatt ab 40 €
        totalCost = totalCost * 0.875    // entspricht 12,5 % Rabatt
    END IF

    RETURN totalCost
END FUNCTION
```

**Gegeben sind folgende Pakete:**

| Paket | Gewicht (kg) | isExpress |
|---|---|---|
| Paket 1 | 3,2 | TRUE |
| Paket 2 | 8,0 | FALSE |
| Paket 3 | 12,0 | TRUE |

**Berechnen Sie die Preise der 3 Pakete und den Gesamtpreis mit der Funktion `calculateShippingCost`. Geben Sie Ihren Rechenweg an.**

            Wie soll der Rechenweg aussehen?

| | Rechenweg | Preis (€) |
|---|---|---|
| **Paket 1** (3,2 kg, Express) |? |26 ,93 € |
| **Paket 2** (8,0 kg) |? |13,98 € |
| **Paket 3** (12,0 kg, Express) |? |31,90 € |
| **Zwischensumme** |? |72,81 € |
| **Rabatt?** (≥ 40 €? ja/nein) |? |Ja |
| **Gesamtpreis** | | **63,71                                                €** |

---

## Teilaufgabe c) — ER-Diagramm (8 Punkte)

Die Versandinformationen sollen in einer **Datenbank** gespeichert werden. Dafür wird ein **Entity-Relationship-Diagramm (ER-Diagramm)** erstellt. Folgende Annahmen gelten:

- Artikel werden auf **mehreren LKW** verladen.
- Gespeichert werden: eine **Artikelnummer (AID)**, der **Artikelname**, das **Einzelgewicht pro Artikel**, eine **Fahrzeugnummer (LID)**, das **LKW-Kennzeichen**, der **LKW-Typ**, die **Verladezeit** und die **Menge pro Artikel**.

**Ergänzen Sie das ER-Diagramm für diese Anforderungen. Kennzeichnen Sie die Primärschlüssel in geeigneter Weise (z. B. mit PK / Unterstreichen).**

```
                ┌────────────────────┐                 ┌────────────────────┐
                │     ARTIKEL        │                 │       LKW          │
                ├────────────────────┤                 ├────────────────────┤
                │  AID  (PK)         │                 │  LID  (PK)         │
                │  Artikelname       │                 │  LKW-Kennzeichen   │
                │  Einzelgewicht     │                 │  LKW-Typ           │
                └────────────────────┘                 └────────────────────┘
                        │                                       │
                        └──────────────  ?  ────────────────────┘
                           (Beziehung benennen + Attribute
                            der Beziehung eintragen)
```

**Skizzenfläche** (eigene Zeichnung):

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                                                                             │
│                                                                             │
│                                                                             │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## ⭐ Zusatzaufgabe für schnelle Teams (5 Punkte, nicht Pflicht)

Die Klasse `ShippingCalculator` soll folgende Attribute besitzen (alle `private`, Datentyp `double`): `maxWeight`, `expressSurcharge`, `upTo10kg`, `above10kg`. Die öffentliche Methode `+ calculateShippingCost(packages: List<Package>): double` ist bereits eingetragen.

**Ergänzen Sie das UML-Klassendiagramm mit Klassennamen, Attributen und Datentypen (Sichtbarkeit `private`).**

```
┌──────────────────────────────────────────┐
│                                          │
│   «Klasse»  ________________________     │
│                                          │
│   - ________________ : ________________  │
│   - ________________ : ________________  │
│   - ________________ : ________________  │
│   - ________________ : ________________  │
│                                          │
│   + calculateShippingCost(packages:      │
│       List<Package>): double             │
│                                          │
└──────────────────────────────────────────┘
```

---

## Reflexion (Portfolio — nach dem Erwartungshorizont-Abgleich ausfüllen)

| Frage | Meine Antwort |
|---|---|
| Das konnte ich schon ohne Hilfe | |
| Das habe ich von meinem Partner/meiner Partnerin gelernt | |
| Das will ich in diesem Halbjahr lernen/üben | |

**Portfolio-Hinweis:** Dieses Blatt ist dein **erstes Arbeitsprodukt** im LF5-Portfolio. Hefte es ab — am Ende des Halbjahres zeigst du damit, wie du dich entwickelt hast.
