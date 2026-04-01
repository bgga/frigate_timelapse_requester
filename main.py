import tkinter as tk
from tkinter import ttk
from time import strftime
import requests
from datetime import datetime

actual_time = strftime("%H:%M:%S")


def btnPressed(event):
    ip_addr = entry_ip.get()
    port = entry_port.get()
    kamera = combo_box.get()
    print(f"IP Address: {ip_addr}, port: {port}, kamera: {kamera}")
    data = "2026-04-01"

# Konwersja dat na timestamp Unix
    start = int(datetime.strptime(f"{data} 15:00", "%Y-%m-%d %H:%M").timestamp())
    koniec = int(datetime.strptime(f"{data} 16:00", "%Y-%m-%d %H:%M").timestamp())

    url = f"http://{ip_addr}:{port}/api/export/{kamera}/start/{start}/end/{koniec}"

    payload = {
        "playback": "timelapse_25x",
        "name": f"{kamera}_{data}"
    }

    response = requests.post(url, json=payload)
    print(response.status_code, response.text)


root = tk.Tk()
root.title("Frigate Timelapse Requester")
root.minsize(600, 300)
ttk.Label(root, text="IP:").place(x=10, y=52)
entry_ip = ttk.Entry(root)
ttk.Label(root, text="Port:").place(x=160, y=52)
entry_port = ttk.Entry(root)
label = tk.Label(root, text="Próba mikrofonu!")
label2 = tk.Label(root, text=f"{actual_time}")
ok_btn = ttk.Button(root, text="Send!")


combo_box = ttk.Combobox(root, values=["droga", "brama", "strych", "ezviz"], state="readonly")
# combo_box.grid(row=1, column=0)
combo_box.set("droga")
# combo_box.bind("<<ComboboxSelected>>", select)
ok_btn.bind("<Button-1>", btnPressed)
entry_ip.place(x=30, y=52)
entry_port.place(x=190, y=52)

combo_box.place(x=10, y=72)
label.place(x=10, y=10)
label2.place(x=10, y=30)
ok_btn.place(x=10, y=92)


root.mainloop()
