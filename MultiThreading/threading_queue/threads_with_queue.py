import time
import datetime
import threading
import queue

def log(message):
    now = datetime.datetime.now().strftime("%H:%M:%S")
    print(f'{now} {message}')

def oblicz(x):
    time.sleep(x)
    return x * x

# Watki w puli oczekujace na zadania w kolejce ``kolejka_zadan``
class WatekOblicz(threading.Thread):
    def __init__(self, id, kolejka_zadan):
        threading.Thread.__init__(self, name="WatekOblicz-%d" % (id,))
        self.kolejka_zadan = kolejka_zadan
    def run(self):
        while True:
            # watek sie blokuje w oczekiwaniu az cos trafi do kolejki
            req = self.kolejka_zadan.get()
            if req is None:
                # Nie ma nic wiecej do przetwarzania, wiec konczymy
                break
            result = oblicz(req)
            log("%s %s -> %s" % (self.getName(), req, result))

def main():
    log("uruchamiam watek glowny")
    kolejka_zadan = queue.Queue()
    # inicjalizujemy pule watkow z trzema watkami "obliczeniowymi"
    N_liczba_watkow = 3
    for i in range(N_liczba_watkow):
        WatekOblicz(i, kolejka_zadan).start()

    # wrzucamy 5 zadan
    kolejka_zadan.put(4)
    kolejka_zadan.put(5)
    kolejka_zadan.put(3)
    kolejka_zadan.put(1.5)
    kolejka_zadan.put(2.2)

    # wysylamy zadania zakonczenia przetwarzania do wszystkich watkow
    for i in range(N_liczba_watkow):
        kolejka_zadan.put(None)
    log("koniec watku glownego.")

if __name__ == "__main__":
    main()
