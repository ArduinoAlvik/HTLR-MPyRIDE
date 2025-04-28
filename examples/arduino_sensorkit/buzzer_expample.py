from machine import Pin, PWM
import time

# --- Konfiguration ---
BUZZER_PIN = 12       # GPIO 12 (A5 auf Nano ESP32)
buzzer = PWM(Pin(BUZZER_PIN), duty=0)

# Notenfrequenzen (Hz)
NOTE_G4  = 392
NOTE_A4  = 440
NOTE_B4  = 494   # im Deutschen H4
NOTE_C5  = 523
NOTE_D5  = 587
NOTE_E5  = 659
NOTE_FS5 = 740   # Fis
NOTE_G5  = 784

# Melodie von "Alle meine Entchen"
melody = [
    NOTE_G4, NOTE_A4, NOTE_B4, NOTE_C5, NOTE_D5, NOTE_D5,   # Alle   mei-ne   Ent-chen
    NOTE_C5, NOTE_B4, NOTE_A4, NOTE_G4, NOTE_G4,            # schwim-men auf dem See
    NOTE_D5, NOTE_E5, NOTE_FS5, NOTE_G5, NOTE_G5,           # Kopf-chen in das Was-ser
    NOTE_FS5, NOTE_E5, NOTE_D5, NOTE_C5, NOTE_C5            # Schwanz-chen in die Höh
]

# Zeit-Teiler: 4 = Viertelnote (1000 ms / 4 = 250 ms pro Note)
time_dividers = [4] * len(melody)

def play_entchen():
    for note, div in zip(melody, time_dividers):
        duration = 1000 // div  # Dauer in ms

        if note:
            buzzer.freq(note)
            buzzer.duty(512)    # 100 % Duty für maximale Lautstärke
            time.sleep_ms(duration)
            buzzer.duty(0)
        else:
            # für den Fall, dass du mal eine Pause einfügen willst
            time.sleep_ms(duration)

        # kurze Verbindungspause (~30 % der Notendauer)
        time.sleep_ms(duration // 3)

# Endlosschleife
while True:
    play_entchen()
    time.sleep(2)  # 2 s Pause vor Wiederholung
