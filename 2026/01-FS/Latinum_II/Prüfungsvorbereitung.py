from datetime import datetime, timedelta

def lernziele ():
  task1 = "Sie können einen oder zwei einfachere lateinischen Originaltexte in korrektes Deutsch übersetzen."
  task2 = "Sie können die Satzteile und Aufbau von lateinischen Sätzen analysieren und erklären."
  task3 = "Sie beherrschen die lateinischen Nominal- und Verbalformen und können diese Formen analysieren und mit Fachausdrücken genau bestimmen."
  task4 = "Sie sind fähig, verschiedene Übersetzungen miteinander zu vergleichen und Übersetzungsfehler zu erkennen."
  print(f" Lernziele\n1. {task1}\n2. {task2}\n3. {task3}\n4. {task4}")

lernziele()

def erstelle_lernplan():
  # 1. Parameter definieren
  heute = datetime.today()
  prüfungs_datum = datetime(2026, 6, 8)
  lernthemen = ["Formenlehre", "Satzbau"]

  # 2. Zeit berechnen
  verbleibende_Tage = (prüfungs_datum - heute).days
  print(f"Du hast noch {verbleibende_Tage} Tage bis zur Prüfung.")

  # 3. Lernplan erstellen (Themen gleichmässig aufteilen)
  if verbleibende_Tage > 0 and len(lernthemen) > 0:
    tage_pro_thema = verbleibende_Tage / len(lernthemen)
    print(f"\nJedes Thema kann ca. {tage_pro_thema:.1f} Tage bearbeitet werden.")
    print(f"\n--- Dein Lernplan ---")

    aktuelles_datum = heute
    for i, thema in enumerate(lernthemen):
      lerntage = max(1, round(tage_pro_thema))
      print(f"Phase {i+1}: '{thema}'")
      print(f"  -> Vom {aktuelles_datum.strftime('%d.%m.%Y')}", end="")

      aktuelles_datum += timedelta(days=lerntage)
      print(f" bis zum {(aktuelles_datum - timedelta(days=1)).strftime('%d.%m.%Y')}\n")

  elif verbleibende_Tage <= 0:
    print("Das Prüfungsdatum liegt in der Vergangenheit oder ist heute.")

erstelle_lernplan()