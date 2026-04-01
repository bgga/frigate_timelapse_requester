# Frigate Timelapse Requester

Prosta aplikacja desktopowa (GUI) do wysyłania żądań eksportu timelapse z systemu [Frigate NVR](https://frigate.video/) przez jego REST API.

## Wymagania

- Python 3.8+
- Działająca instancja Frigate NVR dostępna w sieci lokalnej

### Zależności

```bash
pip install requests
```

Moduły `tkinter` i `datetime` są częścią biblioteki standardowej Pythona.

## Uruchomienie

```bash
python main.py
```

## Użycie

1. Wpisz adres **IP** serwera Frigate
2. Wpisz **port** (domyślnie `5000`)
3. Wybierz **kamerę** z listy rozwijanej
4. Kliknij **Send!**

Aplikacja wyśle żądanie POST do API Frigate z parametrami eksportu timelapse i wyświetli odpowiedź serwera w konsoli.

## Dostępne kamery

| Nazwa    | Opis               |
| -------- | ------------------ |
| `droga`  | Kamera przy drodze |
| `brama`  | Kamera przy bramie |
| `strych` | Kamera na strychu  |
| `ezviz`  | Kamera EZVIZ       |

## Szczegóły żądania

Aplikacja wysyła żądanie `POST` na endpoint:

```
http://<ip>:<port>/api/export/<kamera>/start/<timestamp>/end/<timestamp>
```

Z payloadem:

```json
{
    "playback": "timelapse_25x",
    "name": "<kamera>_<data>"
}
```

Przedział czasowy eksportu jest aktualnie ustawiony na `15:00–16:00` dla daty `2026-04-01` i wymaga ręcznej zmiany w kodzie (`data`, `start`, `koniec`).

## Struktura projektu

```
.
└── main.py       # Główny plik aplikacji
```

## Znane ograniczenia

- Data i przedział godzinowy są zapisane na sztywno w kodzie
- Brak walidacji pól IP i Port przed wysłaniem żądania
- Brak obsługi błędów sieciowych (timeout, brak połączenia)
