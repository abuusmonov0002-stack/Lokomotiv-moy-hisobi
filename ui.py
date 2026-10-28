CSS = r"""
@property --k{syntax:'<number>';inherits:true;initial-value:0}
:root{--frame:#4a4a46;--panel:#e6e5df;--card:#f1f0eb;--tx:#1f2421;--mut:#7b7e79;--line:#d6d5ce;--mint:#8fe5c4;--mint2:#63cfa8;--lime:#e5f43a;--red:#ef5350;--yel:#f2c94c;--grn:#5ccf9c;--org:#f5793a;
--raise:8px 8px 20px rgba(60,60,50,.13),-7px -7px 18px rgba(255,255,255,.75);--inset:inset 3px 3px 7px rgba(60,60,50,.13),inset -3px -3px 7px rgba(255,255,255,.85)}
*{box-sizing:border-box}
body{margin:0;min-height:100vh;padding:26px;background:radial-gradient(circle at 20% 0,#f3f3f1,#d9dce1);color:var(--tx);font:14.5px/1.5 "Segoe UI Variable","Segoe UI",system-ui,sans-serif;-webkit-font-smoothing:antialiased}
.shell{max-width:1560px;margin:auto;background:var(--frame);border-radius:42px;padding:10px;box-shadow:0 40px 70px -30px rgba(30,30,25,.55)}
.top{display:flex;align-items:center;gap:14px;padding:6px 12px 14px;flex-wrap:wrap}
.logo{width:48px;height:48px;border-radius:50%;background:#fff;display:grid;place-items:center;flex:none;box-shadow:0 6px 16px -6px rgba(0,0,0,.5)}
.ttl{background:var(--panel);border-radius:30px;padding:8px 26px;margin-right:auto;font-size:26px;font-weight:500;letter-spacing:-.5px;line-height:1.2}.ttl small{display:block;font-size:11.5px;color:var(--mut);font-weight:400;letter-spacing:0}
.nav{display:flex;gap:8px;flex-wrap:wrap;align-items:center}
.nav a{display:flex;gap:8px;align-items:center;padding:10px 20px;border-radius:99px;color:#d9dad5;text-decoration:none;background:rgba(255,255,255,.1);transition:.25s;font-weight:500}
.nav a:hover{background:rgba(255,255,255,.22);color:#fff;transform:translateY(-2px)}.nav a.on{background:#fff;color:var(--tx);box-shadow:0 8px 18px -8px rgba(0,0,0,.6)}
.nav svg{width:17px;height:17px;stroke:currentColor;fill:none;stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round}
.who{display:flex;align-items:center;gap:10px;color:#d9dad5;font-size:13px;padding-left:6px}.who b{color:#fff;display:block;line-height:1.1}.who u{width:38px;height:38px;border-radius:50%;background:var(--lime);color:#2b2f00;display:grid;place-items:center;font-weight:700;text-decoration:none}
.live{display:inline-flex;gap:7px;align-items:center;font-size:12px;color:#c9cbc4}.live i{width:9px;height:9px;border-radius:50%;background:var(--lime);animation:pulse 1.8s infinite}
.panel{background:var(--panel);border-radius:32px;padding:30px 32px 36px;min-height:70vh}
h1{font-size:34px;font-weight:500;margin:0;letter-spacing:-1px}h2{font-size:19px;font-weight:600;margin:30px 0 14px}.sub{color:var(--mut);margin:4px 0 0}.hd{display:flex;justify-content:space-between;align-items:flex-end;gap:20px;flex-wrap:wrap;margin-bottom:22px}
.card,.kpi,.loco,.km,.login,.tw{background:var(--card);border-radius:26px;box-shadow:var(--raise)}
.tl{position:relative;display:flex;justify-content:space-between;gap:10px;margin:8px 0 34px;padding:0 10px;overflow-x:auto}
.tl:before{content:"";position:absolute;left:0;right:0;top:25px;height:2px;background:linear-gradient(90deg,var(--red),var(--yel),var(--grn))}
.nd{position:relative;text-decoration:none;color:var(--tx);text-align:center;font-size:12px;font-weight:600;min-width:62px;animation:up .6s both;animation-delay:calc(var(--i)*70ms)}
.nd b{display:grid;place-items:center;width:50px;height:50px;margin:0 auto 5px;border-radius:50%;background:var(--lime);box-shadow:0 0 0 6px var(--panel),0 10px 20px -8px rgba(0,0,0,.4);transition:.25s}
.nd.r b{background:var(--red);color:#fff;animation:ring 2s infinite}.nd.y b{background:var(--yel)}.nd:hover b{transform:scale(1.14)}
.kpis{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:18px}
.kpi{padding:20px 24px;animation:up .6s both;animation-delay:calc(var(--i)*70ms);position:relative}
.kpi span{color:var(--mut);font-size:13px}.kpi strong{display:block;font-size:42px;font-weight:500;line-height:1.1;letter-spacing:-1px;font-variant-numeric:tabular-nums}
.kpi:after{content:"";position:absolute;right:20px;top:20px;width:14px;height:14px;border-radius:50%;background:var(--c);box-shadow:0 0 0 5px color-mix(in srgb,var(--c) 25%,transparent)}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(270px,1fr));gap:20px}
.loco{padding:22px;text-decoration:none;color:inherit;display:block;transition:.3s;animation:up .6s both;animation-delay:calc(var(--i)*70ms + 250ms);position:relative;overflow:hidden}
.loco:hover{transform:translateY(-6px);box-shadow:var(--raise),0 24px 40px -18px rgba(99,207,168,.7)}
.loco:after{content:"";position:absolute;inset:0;background:linear-gradient(115deg,transparent 40%,rgba(255,255,255,.65) 50%,transparent 60%);transform:translateX(-120%);transition:.7s}.loco:hover:after{transform:translateX(120%)}
.loco .t{display:flex;justify-content:space-between;align-items:flex-start}.loco h3{margin:0;font-size:26px;font-weight:500;letter-spacing:-.6px}.loco small{color:var(--mut)}
.ring{--r:0;--y:0;--k:0;width:118px;height:118px;border-radius:50%;margin:18px auto 14px;position:relative;transition:--k 1.3s cubic-bezier(.2,.8,.2,1) .2s;background:conic-gradient(var(--red) 0 calc(var(--r)*var(--k)*1%),var(--yel) 0 calc((var(--r) + var(--y))*var(--k)*1%),var(--grn) 0 calc(100*var(--k)*1%),#d9d8d1 0);box-shadow:var(--raise)}
.ring.go{--k:1}.ring:after{content:"";position:absolute;inset:14px;border-radius:50%;background:var(--card);box-shadow:var(--inset)}
.ring b{position:absolute;inset:0;display:grid;place-items:center;z-index:1;font-size:28px;font-weight:500}.ring em{font-style:normal;font-size:11px;color:var(--mut);display:block;text-align:center;margin-top:-6px}
.cnt{display:flex;justify-content:space-between;font-size:13px;color:var(--mut)}.cnt span:before{content:"";display:inline-block;width:9px;height:9px;border-radius:50%;margin-right:6px;background:var(--c)}
.chips{display:flex;gap:6px;flex-wrap:wrap;align-items:center;margin-bottom:16px}
.seg{display:inline-flex;background:var(--panel);border-radius:99px;padding:5px;box-shadow:var(--inset);gap:2px}
.seg button{background:transparent;color:var(--tx);box-shadow:none;padding:8px 18px;font-size:13px}.seg button:hover{transform:none;background:rgba(255,255,255,.5)}
.seg button.on{background:linear-gradient(#a8efd2,var(--mint2));box-shadow:inset 0 1px 0 rgba(255,255,255,.8),0 4px 10px -3px rgba(60,170,130,.6)}
.chips input{margin-left:auto;max-width:280px}
.tw{overflow:auto;max-height:66vh;animation:up .6s .1s both}
table{border-collapse:separate;border-spacing:0;width:100%;font-variant-numeric:tabular-nums}
th{position:sticky;top:0;z-index:2;background:rgba(241,240,235,.88);backdrop-filter:blur(10px);text-align:left;font-size:12.5px;color:var(--mut);font-weight:600;padding:14px;white-space:nowrap}
td{padding:12px 14px;border-top:1px solid var(--line);vertical-align:middle;transition:background .2s}tr:hover td{background:rgba(255,255,255,.55)}
td.n{text-align:right}.mut{color:var(--mut);font-size:13px}.nm{font-weight:600}
.pr{height:8px;border-radius:9px;background:#dcdbd3;box-shadow:var(--inset);margin-top:6px;overflow:hidden;min-width:90px}.pr i{display:block;height:100%;border-radius:9px;width:0;animation:fill 1.1s cubic-bezier(.2,.8,.2,1) .3s forwards}
.pill{display:inline-flex;align-items:center;gap:7px;padding:5px 14px;border-radius:99px;font-size:12.5px;font-weight:700;white-space:nowrap;box-shadow:inset 0 1px 0 rgba(255,255,255,.6),0 4px 10px -5px rgba(0,0,0,.3)}.pill:before{content:"";width:7px;height:7px;border-radius:50%;background:currentColor}
.red{background:var(--red);color:#fff}.red:before{animation:pulse 1.6s infinite}.yellow{background:#f6dd82;color:#6b5200}.green{background:#a8efd2;color:#0d5d40}.none,.empty{background:#dcdbd3;color:#6b6e69}
.pr .red{background:var(--red)}.pr .yellow{background:var(--yel)}.pr .green{background:var(--grn)}
td.kr{color:#d93a37;font-weight:700}td.ky{color:#a07a00;font-weight:700}td.kg{color:#0d7a54;font-weight:600}
input,select{font:inherit;color:var(--tx);border:0;border-radius:99px;padding:9px 16px;background:var(--panel);box-shadow:var(--inset);width:100%;transition:.2s}
input:focus,select:focus{outline:0;box-shadow:var(--inset),0 0 0 4px rgba(143,229,196,.65)}
button,.btn{font:inherit;font-weight:600;color:#10382a;background:linear-gradient(#a8efd2,var(--mint2));border:0;border-radius:99px;padding:11px 24px;cursor:pointer;box-shadow:inset 0 1px 0 rgba(255,255,255,.8),0 8px 16px -8px rgba(60,170,130,.9);transition:.25s}
button:hover{transform:translateY(-2px);box-shadow:inset 0 1px 0 rgba(255,255,255,.8),0 12px 22px -8px rgba(60,170,130,1),0 0 0 4px rgba(143,229,196,.4)}button:active{transform:none}
.gl{color:var(--tx);background:linear-gradient(135deg,rgba(255,255,255,.85),rgba(255,255,255,.3));border:1.5px solid rgba(255,255,255,.95);box-shadow:inset 0 1px 0 #fff,0 10px 22px -10px rgba(70,90,130,.45),6px 4px 16px -8px rgba(245,121,58,.35),-6px 4px 16px -8px rgba(80,140,255,.3)}
.hot{color:#fff;background:linear-gradient(#ff9a5c,var(--org) 55%,#e4571d);box-shadow:inset 0 1px 0 rgba(255,255,255,.6),0 10px 22px -8px rgba(228,87,29,.8)}
.km{display:flex;gap:12px;align-items:flex-end;padding:12px 16px}.km label,.login label{font-size:12.5px;color:var(--mut);display:block;margin:0 0 5px 6px}
.login{padding:26px}.login label{margin-top:14px}
.savebar{position:sticky;bottom:12px;z-index:4;display:flex;justify-content:space-between;align-items:center;gap:16px;margin:18px auto 0;max-width:560px;background:#2e2e2b;color:#e8e9e4;border-radius:99px;padding:8px 8px 8px 26px;box-shadow:0 20px 40px -14px rgba(0,0,0,.6)}
.savebar b{color:var(--lime);font-size:17px}
.sw{display:flex;align-items:center;gap:12px;margin:14px 0 0;cursor:pointer;color:inherit;font-size:14px}.sw input{display:none}
.sw i{width:50px;height:28px;border-radius:99px;background:rgba(120,125,130,.35);box-shadow:inset 0 2px 6px rgba(0,0,0,.2);position:relative;transition:.3s;flex:none}
.sw i:after{content:"";position:absolute;left:3px;top:3px;width:22px;height:22px;border-radius:50%;background:#fff;box-shadow:0 3px 8px rgba(0,0,0,.3);transition:.3s}
.sw input:checked+i{background:linear-gradient(135deg,#58d3a8,#2fae85)}.sw input:checked+i:after{transform:translateX(22px)}
.err,.ok{padding:12px 18px;border-radius:99px;margin:14px 0 0;font-weight:500}.err{background:#f6b3b0;color:#7a1713}.ok{background:#a8efd2;color:#0d5d40}
.toast{position:fixed;right:28px;top:24px;z-index:9;padding:14px 26px;border-radius:99px;background:linear-gradient(135deg,rgba(255,255,255,.95),rgba(255,255,255,.7));backdrop-filter:blur(14px);border:2px solid var(--org);box-shadow:0 20px 40px -14px rgba(0,0,0,.4);font-weight:600;animation:toast 4.4s cubic-bezier(.2,.8,.2,1) forwards}
#upd{animation:none;top:auto;bottom:90px}#upd a{color:var(--org);margin-left:12px}
.auth{display:grid;place-items:center;overflow:hidden;position:relative}
.auth:before,.auth:after{content:"";position:fixed;width:50vmax;height:50vmax;border-radius:50%;filter:blur(80px);opacity:.7;animation:drift 16s ease-in-out infinite alternate;pointer-events:none}
.auth:before{background:#a8efd2;left:-15vmax;top:-20vmax}.auth:after{background:#ffc9a3;right:-18vmax;bottom:-22vmax;animation-delay:-8s}
.box{position:relative;z-index:1;width:min(420px,92vw);padding:36px;border-radius:34px;background:linear-gradient(135deg,rgba(255,255,255,.85),rgba(255,255,255,.4));backdrop-filter:blur(24px);border:1.5px solid rgba(255,255,255,.95);box-shadow:0 30px 70px -24px rgba(50,60,80,.45),8px 6px 30px -12px rgba(245,121,58,.35),-8px 6px 30px -12px rgba(80,140,255,.3);animation:up .8s both}
.box h1{font-size:30px;margin:18px 0 4px}.box p{color:var(--mut);margin:0}.box label.l{display:block;margin:18px 0 6px 8px;font-size:13px;color:var(--mut)}.box button{width:100%;margin-top:22px;padding:14px}
@keyframes up{from{opacity:0;transform:translateY(18px)}}@keyframes fill{to{width:var(--w)}}
@keyframes pulse{0%{box-shadow:0 0 0 0 rgba(229,244,58,.8)}70%,100%{box-shadow:0 0 0 8px rgba(229,244,58,0)}}
@keyframes ring{0%{box-shadow:0 0 0 6px var(--panel),0 0 0 6px rgba(239,83,80,.6)}100%{box-shadow:0 0 0 6px var(--panel),0 0 0 18px rgba(239,83,80,0)}}
@keyframes toast{0%{transform:translateX(130%)}10%,85%{transform:none}100%{transform:translateX(130%);opacity:0}}
@keyframes drift{to{transform:translate(8vmax,6vmax) scale(1.15)}}
@media(max-width:800px){body{padding:8px}.panel{padding:18px}.shell{border-radius:28px}}
@media(prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important}.ring{--k:1}.pr i{width:var(--w)}}
"""
IC = {"home": '<path d="M3 11l9-8 9 8M5 10v10h14V10"/>', "log": '<path d="M5 4h14v16H5zM9 9h6M9 13h6M9 17h3"/>', "acc": '<circle cx="12" cy="8" r="4"/><path d="M4 21c1-5 15-5 16 0"/>', "out": '<path d="M9 4H5v16h4M16 8l4 4-4 4M20 12H9"/>'}
def ico(k): return '<svg viewBox="0 0 24 24">' + IC[k] + '</svg>'
LOGO = '<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#2f2f2b" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2.5S5 10.2 5 14.8a7 7 0 0014 0C19 10.2 12 2.5 12 2.5z"/><path d="M9 15a3 3 0 003 3" stroke-width="1.6"/></svg>'
FAV = '<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns=%27http://www.w3.org/2000/svg%27 viewBox=%270 0 24 24%27%3E%3Crect width=%2724%27 height=%2724%27 rx=%2712%27 fill=%27%23e5f43a%27/%3E%3Cpath d=%27M12 4S6.5 10.2 6.5 14a5.5 5.5 0 0011 0C17.5 10.2 12 4 12 4z%27 fill=%27none%27 stroke=%27%232f2f2b%27 stroke-width=%271.8%27/%3E%3C/svg%3E">'
JS = r"""<script>
const B=document.body,V0=+B.dataset.v,AUTH=!B.classList.contains('auth');let dirty=false;
if(sessionStorage.y){scrollTo(0,+sessionStorage.y);sessionStorage.removeItem('y')}
if(sessionStorage.n){sessionStorage.removeItem('n');const t=document.createElement('div');t.className='toast';t.textContent="Ma'lumotlar yangilandi — boshqa foydalanuvchi o'zgartirdi";document.body.append(t)}
document.querySelectorAll('[data-n]').forEach(e=>{const t=+e.dataset.n,s=performance.now();(function f(n){const p=Math.min((n-s)/900,1);e.textContent=Math.round(t*(1-Math.pow(1-p,3)));if(p<1)requestAnimationFrame(f)})(s)});
setTimeout(()=>document.querySelectorAll('.ring').forEach(r=>r.classList.add('go')),80);
const rows=[...document.querySelectorAll('tr[data-st]')],q=document.getElementById('q');let cur='all';
function flt(){const t=(q&&q.value||'').toLowerCase();rows.forEach(r=>r.style.display=((cur=='all'||r.dataset.st==cur)&&r.textContent.toLowerCase().includes(t))?'':'none')}
document.querySelectorAll('.seg button').forEach(b=>b.onclick=e=>{e.preventDefault();cur=b.dataset.f;document.querySelectorAll('.seg button').forEach(x=>x.classList.toggle('on',x==b));flt()});
if(q)q.oninput=flt;
const tf=document.querySelector('form.track');
if(tf){const dn=document.getElementById('dn');tf.addEventListener('input',()=>{dirty=true;dn.textContent=[...tf.querySelectorAll('input')].filter(i=>i.value!==i.defaultValue).length});
tf.addEventListener('submit',()=>tf.querySelectorAll('input').forEach(i=>{if(i.value===i.defaultValue)i.disabled=true}))}
if(AUTH)setInterval(async()=>{try{const r=await fetch('/api/ver');if(!r.ok)return;const v=(await r.json()).v;if(v!==V0){if(!dirty){sessionStorage.y=scrollY;sessionStorage.n=1;location.reload()}else document.getElementById('upd').hidden=false}}catch(e){}},3000);
const lg=document.getElementById('lg');if(lg){const sv=localStorage.getItem('lg');if(sv){lg.value=sv;document.getElementById('rl').checked=true}
lg.form.addEventListener('submit',()=>{document.getElementById('rl').checked?localStorage.setItem('lg',lg.value):localStorage.removeItem('lg')})}
</script>"""
BASE = r"""<!doctype html><html lang="uz"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{{ title }} · O'z12E</title>%%FAV%%<style>%%CSS%%</style>
<body class="{{ '' if user else 'auth' }}" data-v="{{ ver }}">{% if user %}<div class="shell"><div class="top"><div class="logo">%%LOGO%%</div><div class="ttl">Moylash nazorati<small>O'z12E elektrovozlari</small></div>
<nav class="nav"><span class="live"><i></i>Jonli</span><a href="/" class="{{ 'on' if tab=='home' }}">%%home%%Umumiy holat</a>{% if user.role=='admin' %}<a href="/audit" class="{{ 'on' if tab=='audit' }}">%%log%%Jurnal</a>{% endif %}<a href="/account" class="{{ 'on' if tab=='acc' }}">%%acc%%Hisob</a></nav>
<div class="who"><u>{{ user.name[:1]|upper }}</u><div><b>{{ user.name }}</b>{{ {'admin':'Administrator','editor':'Kiritish huquqi','viewer':"Ko'ruvchi",'user':'Oddiy foydalanuvchi · faqat kuzatish'}[user.role] }}</div><a href="/logout" title="Chiqish" style="padding:10px;background:rgba(255,255,255,.12);border-radius:50%;color:#d9dad5;display:grid;width:38px;height:38px;place-items:center">%%out%%</a></div></div>
<div class="panel">{% block c %}{% endblock %}</div></div><div class="toast" id="upd" hidden>Boshqa foydalanuvchi o'zgartirdi<a href="">Yangilash</a></div>{% else %}{% block c2 %}{% endblock %}{% endif %}%%JS%%</body></html>"""
LOGIN = r"""{% extends 'base' %}{% block c2 %}<form class="box" method="post"><div class="logo" style="box-shadow:var(--raise)">%%LOGO%%</div><h1>Xush kelibsiz</h1><p>Davom etish uchun tizimga kiring</p>
<label class="l">Login</label><input id="lg" name="login" autocomplete="username" autofocus required><label class="l">Parol</label><input type="password" name="pw" autocomplete="current-password" required>
<label class="sw"><input type="checkbox" id="rl"><i></i>Loginni eslab qolish</label><label class="sw"><input type="checkbox" name="remember"><i></i>Tizimda qolish (30 kun) — keyingi safar parol so'ralmaydi</label>
<button class="hot">Kirish</button>{% if err %}<div class="err">{{ err }}</div>{% endif %}</form>{% endblock %}"""
HOME = r"""{% extends 'base' %}{% block c %}<div class="hd"><div><h1>Umumiy holat</h1><p class="sub">Moylash muddatlari nazorati · {{ today.strftime('%d.%m.%Y') }}</p></div></div>
<div class="tl">{% for l in rows %}<a class="nd {{ 'r' if l.c.red else 'y' if l.c.yellow else '' }}" style="--i:{{ loop.index0 }}" href="/loco/{{ l.number }}"><b>{{ l.c.red or l.c.yellow or '✓' }}</b>{{ l.number }}</a>{% endfor %}</div>
<div class="kpis">{% for lab,key,col in (('Nazoratdagi punktlar','tot','#8a8d88'),("Muddati o'tgan",'red','#ef5350'),('Yaqinlashgan','yellow','#f2c94c'),('Norma','green','#5ccf9c')) %}<div class="kpi" style="--c:{{ col }};--i:{{ loop.index0 }}"><span>{{ lab }}</span><strong data-n="{{ rows|sum(attribute='tot') if key=='tot' else rows|sum(attribute='c.'~key) }}">0</strong></div>{% endfor %}</div>
<h2>Elektrovozlar</h2><div class="grid">{% for l in rows %}<a class="loco" style="--i:{{ loop.index0 }}" href="/loco/{{ l.number }}"><div class="t"><div><h3>{{ l.number }}</h3><small>{{ '{:,}'.format(l.km).replace(',',' ') }} km</small></div>{% if l.c.red %}<span class="pill red">{{ l.c.red }} ta o'tgan</span>{% else %}<span class="pill green">Tartibda</span>{% endif %}</div>
<div class="ring" style="--r:{{ l.c.red/l.tot*100 if l.tot else 0 }};--y:{{ l.c.yellow/l.tot*100 if l.tot else 0 }}"><b><span>{{ l.c.green }}<em>norma</em></span></b></div>
<div class="cnt"><span style="--c:var(--red)">{{ l.c.red }} o'tgan</span><span style="--c:var(--yel)">{{ l.c.yellow }} yaqin</span><span style="--c:var(--grn)">{{ l.c.green }} norma</span></div></a>{% endfor %}</div>
{% if user.role=='admin' %}<h2>Yangi elektrovoz qo'shish</h2><form class="login" method="post" action="/locos/add" style="display:flex;gap:14px;align-items:flex-end;flex-wrap:wrap"><div><label>Raqami (masalan 0612)</label><input name="number" required pattern="[0-9A-Za-z\-]+"></div><div><label>Ishlab chiqarilgan sana</label><input type="date" name="made" required></div><div><label>Bosib o'tgan masofa (km)</label><input type="number" name="km" min="0" value="0"></div><button>Qo'shish</button></form>{% endif %}{% endblock %}"""
LOCO = r"""{% extends 'base' %}{% block c %}{% if saved %}<div class="toast">Saqlandi · {{ saved }} ta o'zgarish</div>{% endif %}
<div class="hd"><div><h1>O'z12E-{{ l.number }}</h1><p class="sub">Ishlab chiqarilgan: {{ l.made.strftime('%d.%m.%Y') }} · {{ '{:,}'.format(l.km).replace(',',' ') }} km bosib o'tgan</p></div>
{% if can %}<form class="km" method="post" action="/loco/{{ l.number }}/km"><div><label>Joriy masofa (km)</label><input type="number" name="km" min="0" value="{{ l.km }}"></div><button class="gl">Yangilash</button></form>{% endif %}</div>
<div class="chips"><div class="seg"><button class="on" data-f="all">Hammasi</button><button data-f="red">Muddati o'tgan</button><button data-f="yellow">Yaqinlashgan</button><button data-f="green">Norma</button></div><input id="q" placeholder="Qidirish…"></div>
<form class="track" method="post" action="/loco/{{ l.number }}/save"><div class="tw"><table><tr><th>#</th><th>Moylanadigan joy</th><th>Sarf</th><th>Davriylik</th><th style="min-width:170px">Oxirgi moylash</th><th style="min-width:140px">Masofa (km)</th><th>Keyingi sana</th><th style="min-width:150px">Qolgan muddat</th><th>Holat</th><th>Qolgan km</th></tr>
{% for p,r,c in items %}<tr data-st="{{ c.st }}"><td class="mut">{{ loop.index }}</td><td><div class="nm">{{ p.nom }}</div><div class="mut">{{ p.moy }}</div></td><td>{{ p.sarf }}</td>
<td class="mut">{{ (p.oy~' oy') if p.oy else "zarurat bo'yicha" }}{% if p.kmi %}<br>{{ '{:,}'.format(p.kmi).replace(',',' ') }} km{% endif %}</td>
<td>{% if can %}<input type="date" name="d{{ p.id }}" value="{{ r.last_date or '' }}">{% else %}{{ r.last_date.strftime('%d.%m.%Y') if r.last_date }}{% endif %}</td>
<td>{% if can %}<input type="number" min="0" name="k{{ p.id }}" value="{{ r.last_km if r.last_km is not none }}">{% else %}{{ r.last_km }}{% endif %}</td>
<td>{{ c.nd.strftime('%d.%m.%Y') if c.nd }}</td><td>{% if c.left is not none %}<b>{{ c.left }}</b> <span class="mut">kun</span>{% set pc = [[((1 - c.left/(p.oy*30.4))*100)|round|int, 0]|max, 100]|min %}<div class="pr"><i class="{{ c.st }}" style="--w:{{ pc }}%"></i></div>{% endif %}</td>
<td><span class="pill {{ c.st }}">{{ L[c.st] }}</span></td><td class="n {{ {'red':'kr','yellow':'ky','green':'kg'}.get(c.kst,'') }}">{{ '{:,}'.format(c.kl).replace(',',' ') if c.kl is not none }}</td></tr>{% endfor %}</table></div>
{% if can %}<div class="savebar"><span>O'zgargan kataklar: <b id="dn">0</b></span><button class="hot">O'zgarishlarni saqlash</button></div>{% endif %}</form>
{% if user.role=='admin' %}<form method="post" action="/loco/{{ l.number }}/delete" onsubmit="return confirm('Bu elektrovozni butunlay o\'chirasizmi?')" style="margin-top:34px"><button class="gl" style="color:#b91c1c">Elektrovozni o'chirish</button></form>{% endif %}{% endblock %}"""
AUDIT = r"""{% extends 'base' %}{% block c %}<div class="hd"><div><h1>O'zgarishlar jurnali</h1><p class="sub">Oxirgi 300 ta o'zgarish. Yozuvlarni tahrirlab yoki o'chirib bo'lmaydi.</p></div></div>
<div class="chips"><input id="q" placeholder="Foydalanuvchi yoki elektrovoz bo'yicha qidirish…" style="margin:0;max-width:400px"></div>
<div class="tw"><table><tr><th>Vaqt</th><th>Kim</th><th>Nima o'zgardi</th><th>Eski</th><th>Yangi</th><th>IP</th></tr>
{% for a in rows %}<tr data-st="all"><td class="mut">{{ a.ts.strftime('%d.%m.%Y %H:%M') }}</td><td class="nm">{{ a.user }}</td><td>{{ a.what }}</td><td class="mut">{{ a.old }}</td><td><b>{{ a.new }}</b></td><td class="mut">{{ a.ip }}</td></tr>
{% else %}<tr><td colspan="6" class="mut">Hozircha o'zgarishlar yo'q.</td></tr>{% endfor %}</table></div>{% endblock %}"""
def apply(T):
    def fill(s):
        s = s.replace("%%CSS%%", CSS).replace("%%JS%%", JS).replace("%%FAV%%", FAV).replace("%%LOGO%%", LOGO)
        for k in IC: s = s.replace("%%" + k + "%%", ico(k))
        return s
    for k, v in (("base", BASE), ("login", LOGIN), ("home", HOME), ("loco", LOCO), ("audit", AUDIT)): T[k] = fill(v)
