Tutorial: https://www.youtube.com/watch?v=fg-JfZBetpM&list=PLXmMXHVSvS-DvYrjHcZOg7262I9sGBLFR




1. Uruchomienie celery:  celery -A tasks worker --loglevel=info

    Parametr -A oznacza nazwę aplikacji. Można podać filename.instancja_celery

    ps. gdy np. mamy zmienną tak jak w pliku celery_example.py, to uruchamiamy przez polecenie:
    celery -A celery_example.celery worker --loglever=info
    

2. Sprawdzenie statusu rabbitmq: sudo rabbitmqctl status
3. Wysłanie zadania do tasku: nazwa_tasku.delay(parametry)
4. Gdy ustawimy backend np. na bd postgres, to możemy otrzymać wynik pracy workera.
    x = task_name.delay(parametry)
    x.get() - tu dostajemy rezultat

5. Aktualny status wyniku otrzymujem przez odpytanie:
   x = task_name.delay(parametry)
   x.status - możemy mieć PENDING lub SUCCESS i wiele innych - dokumentacja

   także
   x.ready() - zwraca True gdy zakończy zadania i False gdy ono trwa


 
