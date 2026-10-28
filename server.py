"""Umumiy server: bitta kompyuterda ishga tushiring, qolganlar shu manzilga ulanadi (tarmoq ichida)."""
import os, socket, secrets
from pathlib import Path
DATA = Path(os.getenv("APPDATA") or Path.home() / ".local" / "share") / "Oz12E_Server"; DATA.mkdir(parents=True, exist_ok=True)
K = DATA / "kalit.txt"
if not K.exists(): K.write_text(secrets.token_hex(32))
os.environ.update(SECRET_KEY=K.read_text(), DATABASE_URL="sqlite:///" + (DATA / "moylash.db").as_posix())
import main, uvicorn
main.seed()
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try: s.connect(("8.8.8.8", 80)); ip = s.getsockname()[0]
except Exception: ip = "127.0.0.1"
print(f"\n>>> Boshqa kompyuterlar shu manzilga ulansin:  http://{ip}:8000\n>>> Bu oynani yopmang, aks holda tizim to'xtaydi.\n")
uvicorn.run(main.app, host="0.0.0.0", port=8000)
