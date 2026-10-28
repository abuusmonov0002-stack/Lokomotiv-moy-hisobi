"""Kompyuter ilovasi. Mahalliy rejim yoki umumiy server rejimi (--server http://manzil:8000)."""
import os, sys, socket, threading, time, secrets, webbrowser
from pathlib import Path
DATA = Path(os.getenv("APPDATA") or Path.home() / ".local" / "share") / "Oz12E_Moylash"
DATA.mkdir(parents=True, exist_ok=True)
SRV = DATA / "server.txt"
if "--server" in sys.argv: SRV.write_text(sys.argv[sys.argv.index("--server") + 1].strip())
if "--local" in sys.argv and SRV.exists(): SRV.unlink()
URL = SRV.read_text().strip() if SRV.exists() else ""

def info(text):
    try:
        import tkinter as tk; from tkinter import messagebox
        r = tk.Tk(); r.withdraw(); messagebox.showinfo("O'z12E moylash nazorati", text); r.destroy()
    except Exception: pass

if not URL:                                   # mahalliy rejim: o'z bazasi shu kompyuterda
    KEY = DATA / "kalit.txt"
    if not KEY.exists(): KEY.write_text(secrets.token_hex(32))
    DB = DATA / "moylash.db"; FIRST = not DB.exists(); PW = secrets.token_urlsafe(9)
    os.environ.update(SECRET_KEY=KEY.read_text(), DATABASE_URL="sqlite:///" + DB.as_posix(), ADMIN_PASSWORD=PW)
    import main, uvicorn
    main.seed()
    s = socket.socket(); s.bind(("127.0.0.1", 0)); PORT = s.getsockname()[1]; s.close(); URL = f"http://127.0.0.1:{PORT}"
    server = uvicorn.Server(uvicorn.Config(main.app, host="127.0.0.1", port=PORT, log_config=None))
    threading.Thread(target=server.run, daemon=True).start()
    while not server.started: time.sleep(0.05)
    if FIRST:
        (DATA / "birinchi_parol.txt").write_text(f"Login: admin\nParol: {PW}\nKirgach 'Hisob' bo'limida parolni o'zgartiring va bu faylni o'chiring.\n", encoding="utf-8")
        info(f"Birinchi ishga tushirish.\n\nLogin: admin\nParol: {PW}\n\nKirgach 'Hisob' bo'limida parolni o'zgartiring.")
try:
    import webview
    webview.create_window("O'z12E moylash nazorati", URL, width=1400, height=880, min_size=(900, 600))
    webview.start(private_mode=False, storage_path=str(DATA / "webview"))   # "tizimda qolish" ishlashi uchun
except Exception:
    webbrowser.open(URL)
    import tkinter as tk
    r = tk.Tk(); r.title("O'z12E moylash nazorati"); r.geometry("380x120")
    tk.Label(r, text="Dastur ishlayapti (brauzerda ochildi).\nTugatish uchun shu oynani yoping.", pady=14).pack()
    tk.Button(r, text="Brauzerda ochish", command=lambda: webbrowser.open(URL)).pack(); r.mainloop()
os._exit(0)
