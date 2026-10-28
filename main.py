"""O'z12E moylash nazorati. Ishga tushirish: python main.py seed  ->  uvicorn main:app"""
import os, sys, hashlib, secrets, time
from datetime import date, datetime
from dateutil.relativedelta import relativedelta
from fastapi import FastAPI, Request, Form, Header, HTTPException
from fastapi.responses import RedirectResponse, HTMLResponse
from starlette.middleware.sessions import SessionMiddleware
from jinja2 import Environment, DictLoader, select_autoescape
from sqlalchemy import create_engine, String, Integer, Date, DateTime, ForeignKey, select, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session

DB = os.getenv("DATABASE_URL", "sqlite:///moy.db")        # PostgreSQL: postgresql+psycopg2://u:p@host/db
KM_LIMIT = int(os.getenv("KM_LIMIT", "2000"))
engine = create_engine(DB)

class Base(DeclarativeBase): pass
class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    login: Mapped[str] = mapped_column(String(50), unique=True)
    pw: Mapped[str] = mapped_column(String(200)); name: Mapped[str] = mapped_column(String(100))
    role: Mapped[str] = mapped_column(String(10))           # admin | editor | viewer | user
class Loco(Base):
    __tablename__ = "locos"
    id: Mapped[int] = mapped_column(primary_key=True)
    number: Mapped[str] = mapped_column(String(10), unique=True)
    made: Mapped[date] = mapped_column(Date); km: Mapped[int] = mapped_column(Integer, default=0)
class Point(Base):
    __tablename__ = "points"
    id: Mapped[int] = mapped_column(primary_key=True)
    nom: Mapped[str] = mapped_column(String(100)); moy: Mapped[str] = mapped_column(String(100))
    sarf: Mapped[str] = mapped_column(String(30)); soat: Mapped[int] = mapped_column(Integer)
    oy: Mapped[int] = mapped_column(Integer); kmi: Mapped[int] = mapped_column(Integer)
class Rec(Base):
    __tablename__ = "recs"
    id: Mapped[int] = mapped_column(primary_key=True)
    loco_id: Mapped[int] = mapped_column(ForeignKey("locos.id")); point_id: Mapped[int] = mapped_column(ForeignKey("points.id"))
    last_date: Mapped[date | None] = mapped_column(Date, nullable=True); last_km: Mapped[int | None] = mapped_column(Integer, nullable=True)
class Audit(Base):                                          # faqat INSERT qilinadi
    __tablename__ = "audit"
    id: Mapped[int] = mapped_column(primary_key=True)
    ts: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    user: Mapped[str] = mapped_column(String(50)); what: Mapped[str] = mapped_column(String(150))
    old: Mapped[str] = mapped_column(String(50)); new: Mapped[str] = mapped_column(String(50)); ip: Mapped[str] = mapped_column(String(50), default="")

def pwhash(p, salt=None):
    salt = salt or secrets.token_hex(8)
    return salt + "$" + hashlib.pbkdf2_hmac("sha256", p.encode(), salt.encode(), 200_000).hex()
def pwcheck(p, h): return secrets.compare_digest(pwhash(p, h.split("$")[0]), h)

def calc(rec, p, cur_km, today=None):
    today = today or date.today()
    nd = rec.last_date + relativedelta(months=p.oy) if (rec.last_date and p.oy) else None
    nk = rec.last_km + p.kmi if (rec.last_km is not None and p.kmi) else None
    left = (nd - today).days if nd else None
    kl = nk - cur_km if nk is not None else None
    if not p.oy: st = "none"
    elif not rec.last_date: st = "empty"
    elif left < 0: st = "red"
    elif left <= 15: st = "yellow"
    else: st = "green"
    kst = None if kl is None else ("red" if kl < 0 else "yellow" if kl <= KM_LIMIT else "green")
    return dict(nd=nd, nk=nk, left=left, kl=kl, st=st, kst=kst)
LABEL = {"red": "Muddati o'tgan", "yellow": "Yaqinlashgan", "green": "Norma", "none": "Zarurat bo'yicha", "empty": "Sana kiritilmagan"}

CSS = """:root{--bg:#eef1f3;--ink:#17232d;--mut:#5d6b76;--line:#d9dfe4;--card:#fff;--acc:#1f4e79;--red:#d6303a;--yel:#f2c230;--grn:#3aa76d}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:15px/1.5 "Segoe UI",system-ui,-apple-system,Roboto,sans-serif}
header{background:var(--ink);color:#fff;display:flex;align-items:center;gap:28px;padding:0 28px;height:56px}
header b{font-size:17px;letter-spacing:.2px}header a{color:#b8c4cd;text-decoration:none;padding:18px 0;border-bottom:3px solid transparent}
header a:hover,header a.on{color:#fff;border-color:var(--yel)}header .sp{flex:1}header small{color:#8fa0ac}
main{max-width:1280px;margin:0 auto;padding:28px}h1{font-size:24px;margin:0 0 4px}.sub{color:var(--mut);margin:0 0 22px}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));gap:16px}
.loco{background:var(--card);border:1px solid var(--line);border-radius:6px;padding:18px;text-decoration:none;color:inherit;display:block}
.loco:hover{border-color:var(--acc)}.loco h2{margin:0;font-size:22px}.loco p{margin:2px 0 14px;color:var(--mut);font-size:13px}
.bar{display:flex;height:10px;border-radius:2px;overflow:hidden;background:var(--line)}.bar i{display:block}
.cnt{display:flex;gap:14px;margin-top:12px;font-size:13px;font-variant-numeric:tabular-nums}.cnt span:before{content:"";display:inline-block;width:8px;height:8px;border-radius:50%;margin-right:5px;background:var(--c)}
.tw{background:var(--card);border:1px solid var(--line);border-radius:6px;overflow:auto;max-height:72vh}
table{border-collapse:collapse;width:100%;font-variant-numeric:tabular-nums}th{position:sticky;top:0;background:#e4e9ed;text-align:left;font-weight:600;font-size:13px;padding:10px 12px;white-space:nowrap;z-index:1}
td{padding:9px 12px;border-top:1px solid var(--line);vertical-align:middle}tr:hover td{background:#f6f8fa}td.n{text-align:right}.mut{color:var(--mut);font-size:13px}
.pill{display:inline-block;padding:2px 10px;border-radius:12px;font-size:12px;font-weight:600;white-space:nowrap}
.red{background:var(--red);color:#fff}.yellow{background:var(--yel);color:#4a3600}.green{background:#cdeedd;color:#14532d}.none,.empty{background:#e4e9ed;color:var(--mut)}
td.kr{color:var(--red);font-weight:700}td.ky{color:#9a7400;font-weight:700}td.kg{color:#14532d}
input[type=date],input[type=number],input[type=text],input[type=password],select{font:inherit;border:1px solid #b7c2cb;border-radius:4px;padding:6px 8px;background:#fffdf0;width:100%}
input:focus,select:focus,button:focus-visible{outline:2px solid var(--acc);outline-offset:1px}
button,.btn{font:inherit;font-weight:600;background:var(--acc);color:#fff;border:0;border-radius:4px;padding:9px 18px;cursor:pointer}button:hover{background:#173d5f}
.bar2{display:flex;justify-content:space-between;align-items:end;gap:16px;margin-bottom:16px;flex-wrap:wrap}.km{display:flex;gap:8px;align-items:end}.km label{font-size:12px;color:var(--mut);display:block}
.login{max-width:360px;margin:12vh auto;background:var(--card);border:1px solid var(--line);border-radius:6px;padding:28px}.login label{display:block;margin:14px 0 4px;font-size:13px;color:var(--mut)}
.err{background:#fde8ea;color:#8f1d25;padding:8px 12px;border-radius:4px;margin-top:12px}.ok{background:#e1f4ea;color:#14532d;padding:8px 12px;border-radius:4px;margin-bottom:14px}
@media(max-width:700px){main{padding:14px}header{gap:14px;padding:0 14px}}"""

T = {
"base": """<!doctype html><html lang="uz"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{{ title }} · O'z12E moylash nazorati</title><style>"""+CSS+"""</style>
{% if user %}<header><b>O'z12E moylash nazorati</b><a href="/" class="{{ 'on' if tab=='home' }}">Umumiy holat</a>{% if user.role=='admin' %}<a href="/audit" class="{{ 'on' if tab=='audit' }}">O'zgarishlar jurnali</a>{% endif %}<a href="/account" class="{{ 'on' if tab=='acc' }}">Hisob</a><span class="sp"></span><small>{{ user.name }} ({{ {'admin':'administrator','editor':'kiritish huquqi','viewer':'ko\\'ruvchi','user':'oddiy foydalanuvchi'}[user.role] }})</small><a href="/logout">Chiqish</a></header>{% endif %}
<main>{% block c %}{% endblock %}</main></html>""",
"login": """{% extends 'base' %}{% block c %}<form class="login" method="post"><h1>Tizimga kirish</h1><p class="sub">Login va parolingizni kiriting</p>
<label>Login</label><input type="text" name="login" autofocus required><label>Parol</label><input type="password" name="pw" required><br><br><button style="width:100%">Kirish</button>
{% if err %}<div class="err">{{ err }}</div>{% endif %}</form>{% endblock %}""",
"home": """{% extends 'base' %}{% block c %}<h1>Umumiy holat</h1><p class="sub">Har bir elektrovoz bo'yicha moylash muddatlari. Bugun: {{ today.strftime('%d.%m.%Y') }}</p>
<div class="grid">{% for l in rows %}<a class="loco" href="/loco/{{ l.number }}"><h2>{{ l.number }}</h2><p>{{ '{:,}'.format(l.km).replace(',',' ') }} km bosib o'tgan</p>
<div class="bar">{% for k,c in (('red','--red'),('yellow','--yel'),('green','--grn')) %}<i style="width:{{ l.c[k]/l.tot*100 if l.tot else 0 }}%;background:var({{ c }})"></i>{% endfor %}</div>
<div class="cnt"><span style="--c:var(--red)">{{ l.c.red }} o'tgan</span><span style="--c:var(--yel)">{{ l.c.yellow }} yaqin</span><span style="--c:var(--grn)">{{ l.c.green }} norma</span></div></a>{% endfor %}</div>{% endblock %}""",
"loco": """{% extends 'base' %}{% block c %}<div class="bar2"><div><h1>O'z12E-{{ l.number }}</h1><p class="sub" style="margin:0">Ishlab chiqarilgan: {{ l.made.strftime('%d.%m.%Y') }}</p></div>
{% if can %}<form class="km" method="post" action="/loco/{{ l.number }}/km"><div><label>Joriy bosib o'tgan masofa (km)</label><input type="number" name="km" min="0" value="{{ l.km }}"></div><button>Saqlash</button></form>
{% else %}<div><b>{{ '{:,}'.format(l.km).replace(',',' ') }} km</b> bosib o'tgan</div>{% endif %}</div>
{% if saved %}<div class="ok">O'zgarishlar saqlandi ({{ saved }} ta).</div>{% endif %}
<form method="post" action="/loco/{{ l.number }}/save"><div class="tw"><table><tr><th>T/r</th><th>Moylanadigan joy</th><th>Moy turi</th><th>Sarf</th><th>Davriylik</th><th style="min-width:150px">Oxirgi moylash</th><th style="min-width:130px">Masofa (km)</th><th>Keyingi sana</th><th>Qolgan kun</th><th>Holat</th><th>Qolgan km</th></tr>
{% for p,r,c in items %}<tr><td>{{ loop.index }}</td><td>{{ p.nom }}</td><td class="mut">{{ p.moy }}</td><td>{{ p.sarf }}</td>
<td class="mut">{{ (p.oy~' oy') if p.oy else 'zarurat bo\\'yicha' }}{% if p.kmi %}<br>{{ '{:,}'.format(p.kmi).replace(',',' ') }} km{% endif %}</td>
<td>{% if can %}<input type="date" name="d{{ p.id }}" value="{{ r.last_date or '' }}">{% else %}{{ r.last_date.strftime('%d.%m.%Y') if r.last_date }}{% endif %}</td>
<td>{% if can %}<input type="number" min="0" name="k{{ p.id }}" value="{{ r.last_km if r.last_km is not none }}">{% else %}{{ r.last_km }}{% endif %}</td>
<td>{{ c.nd.strftime('%d.%m.%Y') if c.nd }}</td><td class="n">{{ c.left if c.left is not none }}</td><td><span class="pill {{ c.st }}">{{ L[c.st] }}</span></td>
<td class="n {{ {'red':'kr','yellow':'ky','green':'kg'}.get(c.kst,'') }}">{{ '{:,}'.format(c.kl).replace(',',' ') if c.kl is not none }}</td></tr>{% endfor %}</table></div>
{% if can %}<p><button>O'zgarishlarni saqlash</button></p>{% endif %}</form>{% endblock %}""",
"audit": """{% extends 'base' %}{% block c %}<h1>O'zgarishlar jurnali</h1><p class="sub">Oxirgi 300 ta o'zgarish. Yozuvlarni o'chirib yoki tahrirlab bo'lmaydi.</p>
<div class="tw"><table><tr><th>Vaqt</th><th>Kim</th><th>Nima o'zgardi</th><th>Eski qiymat</th><th>Yangi qiymat</th><th>IP</th></tr>
{% for a in rows %}<tr><td>{{ a.ts.strftime('%d.%m.%Y %H:%M') }}</td><td>{{ a.user }}</td><td>{{ a.what }}</td><td class="mut">{{ a.old }}</td><td><b>{{ a.new }}</b></td><td class="mut">{{ a.ip }}</td></tr>
{% else %}<tr><td colspan="6">Hozircha o'zgarishlar yo'q.</td></tr>{% endfor %}</table></div>{% endblock %}"""}
T["account"] = """{% extends 'base' %}{% block c %}<h1>Hisob</h1><p class="sub">Parolingizni o'zgartiring{% if user.role=='admin' %} va foydalanuvchilarni boshqaring{% endif %}.</p>
{% if msg %}<div class="ok">{{ msg }}</div>{% endif %}{% if err %}<div class="err" style="margin:0 0 14px">{{ err }}</div>{% endif %}
<form method="post" action="/account/password" class="login" style="margin:0 0 24px;max-width:420px"><b>Parolni o'zgartirish</b><label>Joriy parol</label><input type="password" name="old" required><label>Yangi parol (kamida 8 belgi)</label><input type="password" name="new" minlength="8" required><br><br><button>Parolni saqlash</button></form>
{% if user.role=='admin' %}<h2>Foydalanuvchilar</h2><div class="tw" style="max-height:none;margin-bottom:16px"><table><tr><th>Login</th><th>Ism</th><th>Rol</th><th></th></tr>
{% for u in users %}<tr><td>{{ u.login }}</td><td>{{ u.name }}</td><td>{{ {'admin':'administrator','editor':'kiritish huquqi','viewer':"ko'ruvchi",'user':'oddiy foydalanuvchi (faqat kuzatish)'}[u.role] }}</td><td>{% if u.id!=user.id %}<form method="post" action="/users/{{ u.id }}/delete" style="margin:0"><button style="background:#8f1d25;padding:4px 12px">O'chirish</button></form>{% endif %}</td></tr>{% endfor %}</table></div>
<form method="post" action="/users/add" class="login" style="margin:0;max-width:420px"><b>Yangi foydalanuvchi</b><label>Login</label><input type="text" name="login" required><label>Ism</label><input type="text" name="name"><label>Parol (kamida 8 belgi)</label><input type="password" name="pw" minlength="8" required><label>Rol</label><select name="role"><option value="user">Oddiy foydalanuvchi (faqat kuzatish)</option><option value="editor">Kiritish huquqi</option><option value="viewer">Ko'ruvchi</option><option value="admin">Administrator</option></select><br><br><button>Qo'shish</button></form>{% endif %}{% endblock %}"""
from ui import apply; apply(T)
env = Environment(loader=DictLoader(T), autoescape=select_autoescape(default=True))
def render(name, **kw):
    with Session(engine) as db: kw["ver"] = db.scalar(select(func.max(Audit.id))) or 0
    return HTMLResponse(env.get_template(name).render(**kw))

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=os.getenv("SECRET_KEY", "O'ZGARTIRING-uzun-tasodifiy-kalit"), max_age=30*86400, https_only=os.getenv("HTTPS", "0") == "1")
def me(request, db):
    s = request.session; uid = s.get("uid")
    if uid and s.get("exp", 0) < time.time(): s.clear(); return None
    return db.get(User, uid) if uid else None
def log(db, request, user, what, old, new):
    db.add(Audit(user=user, what=what, old=str(old if old is not None else "—"), new=str(new if new is not None else "—"), ip=request.client.host if request.client else ""))

@app.api_route("/login", methods=["GET", "POST"])
async def login(request: Request):
    if request.method == "GET": return render("login", title="Kirish", user=None)
    f = await request.form()
    with Session(engine) as db:
        u = db.scalar(select(User).where(User.login == f.get("login", "").strip()))
        if u and pwcheck(f.get("pw", ""), u.pw):
            request.session["uid"] = u.id; request.session["exp"] = time.time() + (30 * 86400 if f.get("remember") else 12 * 3600)
            return RedirectResponse("/", 303)
    return render("login", title="Kirish", user=None, err="Login yoki parol noto'g'ri.")
@app.get("/api/ver")
def api_ver(request: Request):
    with Session(engine) as db:
        if not me(request, db): raise HTTPException(401)
        return {"v": db.scalar(select(func.max(Audit.id))) or 0}
@app.get("/logout")
def logout(request: Request): request.session.clear(); return RedirectResponse("/login", 303)

@app.get("/")
def home(request: Request):
    with Session(engine) as db:
        u = me(request, db)
        if not u: return RedirectResponse("/login", 303)
        pts = {p.id: p for p in db.scalars(select(Point))}; rows = []
        for l in db.scalars(select(Loco).order_by(Loco.number)):
            c = {"red": 0, "yellow": 0, "green": 0}
            for r in db.scalars(select(Rec).where(Rec.loco_id == l.id)):
                s = calc(r, pts[r.point_id], l.km)["st"]
                if s in c: c[s] += 1
            rows.append(dict(number=l.number, km=l.km, c=c, tot=sum(c.values())))
        return render("home", title="Umumiy holat", user=u, tab="home", rows=rows, today=date.today())

def loco_page(request, num, saved=None):
    with Session(engine) as db:
        u = me(request, db)
        if not u: return RedirectResponse("/login", 303)
        l = db.scalar(select(Loco).where(Loco.number == num))
        if not l: raise HTTPException(404, "Elektrovoz topilmadi")
        items = []
        for p in db.scalars(select(Point).order_by(Point.id)):
            r = db.scalar(select(Rec).where(Rec.loco_id == l.id, Rec.point_id == p.id))
            items.append((p, r, calc(r, p, l.km)))
        return render("loco", title=f"O'z12E-{num}", user=u, tab="home", l=l, items=items, L=LABEL, can=u.role in ("admin", "editor"), saved=saved)
@app.get("/loco/{num}")
def loco(request: Request, num: str, saved: int = None): return loco_page(request, num, saved)

@app.post("/loco/{num}/save")
async def save(request: Request, num: str):
    f = await request.form(); n = 0
    with Session(engine) as db:
        u = me(request, db)
        if not u: return RedirectResponse("/login", 303)
        if u.role not in ("admin", "editor"): raise HTTPException(403, "Ruxsat yo'q")
        l = db.scalar(select(Loco).where(Loco.number == num))
        for p in db.scalars(select(Point)):
            r = db.scalar(select(Rec).where(Rec.loco_id == l.id, Rec.point_id == p.id))
            its = []
            if f"d{p.id}" in f: its.append(("last_date", date.fromisoformat(f[f"d{p.id}"]) if f[f"d{p.id}"] else None, "oxirgi sana"))
            if f"k{p.id}" in f: its.append(("last_km", int(f[f"k{p.id}"]) if f[f"k{p.id}"] else None, "oxirgi masofa"))
            for fld, new, lab in its:
                if getattr(r, fld) != new:
                    log(db, request, u.login, f"{num} · {p.nom} · {lab}", getattr(r, fld), new); setattr(r, fld, new); n += 1
        db.commit()
    return RedirectResponse(f"/loco/{num}?saved={n}", 303)

@app.post("/loco/{num}/km")
async def set_km(request: Request, num: str, km: int = Form(...)):
    with Session(engine) as db:
        u = me(request, db)
        if not u or u.role not in ("admin", "editor"): raise HTTPException(403, "Ruxsat yo'q")
        l = db.scalar(select(Loco).where(Loco.number == num))
        if km != l.km: log(db, request, u.login, f"{num} · joriy masofa", l.km, km); l.km = km; db.commit()
    return RedirectResponse(f"/loco/{num}", 303)

@app.post("/api/mileage")                                    # kunlik avto-yangilash uchun: {"0601": 107200, ...}
async def api_mileage(request: Request, x_token: str = Header("")):
    if not os.getenv("API_TOKEN") or not secrets.compare_digest(x_token, os.getenv("API_TOKEN")): raise HTTPException(401)
    data = await request.json()
    with Session(engine) as db:
        for num, km in data.items():
            l = db.scalar(select(Loco).where(Loco.number == num))
            if l and int(km) != l.km: log(db, request, "avto-yangilash", f"{num} · joriy masofa", l.km, km); l.km = int(km)
        db.commit()
    return {"ok": True}

@app.get("/audit")
def audit(request: Request):
    with Session(engine) as db:
        u = me(request, db)
        if not u: return RedirectResponse("/login", 303)
        if u.role != "admin": raise HTTPException(403, "Ruxsat yo'q")
        return render("audit", title="Jurnal", user=u, tab="audit", rows=db.scalars(select(Audit).order_by(Audit.id.desc()).limit(300)).all())

def acct(request, msg=None, err=None):
    with Session(engine) as db:
        u = me(request, db)
        if not u: return RedirectResponse("/login", 303)
        users = db.scalars(select(User).order_by(User.id)).all() if u.role == "admin" else []
        return render("account", title="Hisob", user=u, tab="acc", msg=msg, err=err, users=users)
@app.get("/account")
def account(request: Request): return acct(request)
@app.post("/account/password")
async def chpw(request: Request):
    f = await request.form()
    with Session(engine) as db:
        u = me(request, db)
        if not u: return RedirectResponse("/login", 303)
        if not pwcheck(f.get("old", ""), u.pw): return acct(request, err="Joriy parol noto'g'ri.")
        if len(f.get("new", "")) < 8: return acct(request, err="Yangi parol kamida 8 belgidan iborat bo'lsin.")
        u.pw = pwhash(f["new"]); log(db, request, u.login, "parol o'zgartirildi", None, None); db.commit()
    return acct(request, msg="Parol o'zgartirildi.")
@app.post("/users/add")
async def uadd(request: Request):
    f = await request.form(); lg = f.get("login", "").strip()
    with Session(engine) as db:
        u = me(request, db)
        if not u or u.role != "admin": raise HTTPException(403, "Ruxsat yo'q")
        if not lg or len(f.get("pw", "")) < 8 or f.get("role") not in ("admin", "editor", "viewer", "user"): return acct(request, err="Login, kamida 8 belgili parol va rolni to'g'ri kiriting.")
        if db.scalar(select(User).where(User.login == lg)): return acct(request, err="Bu login band.")
        db.add(User(login=lg, pw=pwhash(f["pw"]), name=f.get("name", "").strip() or lg, role=f["role"]))
        log(db, request, u.login, f"foydalanuvchi qo'shildi: {lg}", None, f["role"]); db.commit()
    return acct(request, msg=f"{lg} qo'shildi.")
@app.post("/users/{uid}/delete")
def udel(request: Request, uid: int):
    with Session(engine) as db:
        u = me(request, db)
        if not u or u.role != "admin": raise HTTPException(403, "Ruxsat yo'q")
        x = db.get(User, uid)
        if x and x.id != u.id: log(db, request, u.login, f"foydalanuvchi o'chirildi: {x.login}", None, None); db.delete(x); db.commit()
    return acct(request, msg="Foydalanuvchi o'chirildi.")

@app.post("/locos/add")
async def ladd(request: Request):
    f = await request.form(); num = f.get("number", "").strip()
    with Session(engine) as db:
        u = me(request, db)
        if not u or u.role != "admin": raise HTTPException(403, "Ruxsat yo'q")
        if not num or db.scalar(select(Loco).where(Loco.number == num)): return RedirectResponse(f"/loco/{num}", 303)
        made = date.fromisoformat(f["made"]); l = Loco(number=num, made=made, km=int(f.get("km") or 0)); db.add(l); db.flush()
        db.add_all([Rec(loco_id=l.id, point_id=p.id, last_date=made, last_km=0) for p in db.scalars(select(Point))])
        log(db, request, u.login, f"elektrovoz qo'shildi: {num}", None, None); db.commit()
    return RedirectResponse(f"/loco/{num}", 303)
@app.post("/loco/{num}/delete")
def ldel(request: Request, num: str):
    with Session(engine) as db:
        u = me(request, db)
        if not u or u.role != "admin": raise HTTPException(403, "Ruxsat yo'q")
        l = db.scalar(select(Loco).where(Loco.number == num))
        if l:
            for r in db.scalars(select(Rec).where(Rec.loco_id == l.id)): db.delete(r)
            db.delete(l); log(db, request, u.login, f"elektrovoz o'chirildi: {num}", None, None); db.commit()
    return RedirectResponse("/", 303)

POINTS = [("Avtoulagich (автосцепка)","SY1412-75","0,2 l",0,0,0),("Havo kompressori","Mobil Rarus SHC 1024","16 l",3000,24,0),
("Kompressor dvigateli","Mobilith SHC 220","60 g",2000,24,0),("Mashinist o'rindig'i","Molykote BR2","800 g",0,12,200000),
("Oyna tozalagich","Great Wall 7036","80 g",0,0,0),("Tortuv elektrodvigateli","Mobil SHC 100","1,2 kg",0,3,50000),
("Tishli uzatma (кожух)","Mobil Delvac 1 Gear Oil 80W-140","84 l",0,12,200000),("Tayanch o'q podshipnigi","Mobilith SHC 220","1,2 kg",0,3,0),
("G'ildirak grebeni","NLGI 0","64 kg",0,4,0),("Tortish shkvoreni","Kluberlub BE 71-501","haqiqiy sarf",0,3,50000),
("Tok qabul qilgich","7253 aviatsiya moyi","0,1 kg",0,6,0),("Yuqori kuchlanishli yerga ulagich","Mobil SHC 100","0,1 kg",0,6,0),
("Mashinist boshqaruv kontrolleri","Mobil SHC 100","0,1 kg",0,12,0),("Yuqori kuchlanishli ajratgich kaliti","Mobil SHC 100","0,2 kg",0,12,0),
("Bosh vakuum o'chirgich","Mobil SHC 100","0,1 kg",0,6,0),("Sovutish minorasi ventilyatori","Mobiltemp SHC 100","84 g",0,3,0),
("Transformator shkafi ventilyatori","Mobiltemp SHC 100","36 g",0,3,0),("Tortuv ventilyatori dvigateli","Mobiltemp SHC 100","180 g",0,3,0)]
LOCOS = [("0601",date(2025,12,15),106991),("0602",date(2025,12,15),104718),("0603",date(2026,1,1),79072),("0605",date(2026,3,1),68200),("0606",date(2026,3,1),65869)]

def seed():
    Base.metadata.create_all(engine)
    with Session(engine) as db:
        if db.scalar(select(Point)): return print("Baza allaqachon to'ldirilgan.")
        db.add_all([Point(nom=a, moy=b, sarf=c, soat=d, oy=e, kmi=f) for a, b, c, d, e, f in POINTS]); db.flush()
        import json; from pathlib import Path
        D = json.loads((Path(getattr(sys, "_MEIPASS", Path(__file__).parent)) / "data.json").read_text(encoding="utf-8"))
        pts = list(db.scalars(select(Point).order_by(Point.id)))
        for num, d in D.items():
            l = Loco(number=num, made=date.fromisoformat(d["made"]), km=d["km"]); db.add(l); db.flush()
            db.add_all([Rec(loco_id=l.id, point_id=p.id, last_date=date.fromisoformat(r[0]) if r[0] else None, last_km=r[1]) for p, r in zip(pts, d["recs"])])
        pw = os.getenv("ADMIN_PASSWORD") or secrets.token_urlsafe(9)
        db.add(User(login="admin", pw=pwhash(pw), name="Administrator", role="admin")); db.commit()
        print(f"Tayyor. Login: admin  Parol: {pw}  (birinchi kirishdan keyin o'zgartiring)")
def add_user(login, password, name, role):
    with Session(engine) as db: db.add(User(login=login, pw=pwhash(password), name=name, role=role)); db.commit()
if __name__ == "__main__":
    if sys.argv[1:2] == ["seed"]: seed()
    elif sys.argv[1:2] == ["user"]: add_user(*sys.argv[2:6])   # python main.py user login parol "Ism" editor
