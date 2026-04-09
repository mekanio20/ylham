# 📜 Açyk Çeşme Şygyr Platformasy

Minimalistik we döwrebap dizaýn bilen döredilen, ulanyjylaryň şygyrlary paýlaşyp, okap bilýän **açyk çeşme (open-source) şygyr platformasy**.

---

## 🚀 Taslama hakda

Bu platforma edebiýaty söýýän adamlar üçin döredildi. Maksat — sosial medýadan tapawutlylykda, diňe mazmuna gönükdirilen, arassa we rahat okalýan gurşawy döretmek.

Ulanyjylar:
- Öz şygyrlaryny paýlaşyp biler  
- Beýleki şygyrlary okap biler  
- Jemgyýet bilen pikir alyşyp biler

---

## ✨ Esasy aýratynlyklar

- ✍️ Şygyr goşmak we paýlaşmak
- 📖 Şygyr okamak
- ❤️ Like (halamak) ulgamy
- 💬 Teswir ýazmak mümkinçiligi
- 🌙 Minimalistik dizaýn

---

## 🛠️ Tehnologiýalar

### Frontend
- Vue 3
- Vite
- Tailwind CSS

### Backend
- DJANGO
- (sqlite3)
- PostgreSQL

---

## 📁 Taslama gurluşy
```
ylham/
    ├─ backend/
    ├─ frontend/
    └─ README.md
```

---

## ⚙️ Gurmak we işe girizmek

### 1. Repo'ny klonla

```
git clone https://github.com/mekanio20/ylham.git
cd ylham/
```

### 2. Backend

```
cd backend/

# virtualenv döret
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Gerekli paketleri ýükle
pip install -r requirements.txt

# Database döret
python manage.py migrate

# Superuser döret (optional)
python manage.py createsuperuser

# Backend'i başlat
python manage.py runserver
```

---

### 3. Frontend

```
cd frontend/
yarn install
yarn run dev
```

---

## 🤝 Goşant goşmak

Bu taslama açyk çeşmeli bolup, her kim goşant goşup biler.

### Ädimler:
1. Repo'ny fork et  
2. Täze branch aç (`feature/your-feature`)  
3. Üýtgetmeleri giriz  
4. Pull Request ugrat

---

## 📄 Lisenziýa

MIT License

---

## 💡 Maksat

Bu taslama diňe bir platforma däl, eýsem:
- edebiýaty ösdürmek  
- döredijilikli adamlary birleşdirmek  
- açyk çeşme jemgyýetini döretmek
üçin niýetlenendir.