# 🧭 Ceļojumu Dienasgrāmata (Konsoles programma)

Šī ir lietotājam draudzīga Python programma, kas ļauj saglabāt, pārvaldīt un pārskatīt savus ceļojumus tieši konsolē. Katrs ceļojums tiek saglabāts atsevišķā failā, un lietotājs var veikt vairākas darbības – no pievienošanas līdz statistikas skatīšanai.

---

## 📌 Ievads

**Mērķis:**  
Programma ļauj lietotājam veidot savu ceļojumu dienasgrāmatu, saglabājot datus par braucieniem – to nosaukumu, galamērķi, datumu un aprakstu.

**Galvenās iespējas:**
- Pievienot jaunu ceļojumu
- Skatīt visus saglabātos ceļojumus tabulā
- Meklēt pēc galamērķa vai apraksta
- Rediģēt vai dzēst esošu ierakstu
- Kārtot ceļojumus pēc datuma vai nosaukuma
- Skatīt ceļojumu statistiku

---

## 🧑‍💻 Lietotāja interfeiss

Programma darbojas konsolē (komandrindā) un piedāvā numerētu izvēlni:


---

## ⚙️ Kā izmantot programmu

### ✅ Pievienot jaunu ceļojumu
1. Izvēlies `1. Pievienot jaunu ceļojumu`
2. Ievadi:  
   - Ceļojuma nosaukumu  
   - Galamērķi  
   - Datumu (`YYYY-MM-DD`)  
   - Aprakstu  
3. Ceļojums tiek saglabāts failā `trips/trip_#.json`

---

### ✅ Skatīt visus ceļojumus
- Izvēlies `2. Skatīt visus ceļojumus`
- Visi ceļojumi tiks rādīti tabulas veidā

---

### ✅ Meklēt ceļojumu
- Izvēlies `3. Meklēt...`
- Ievadi atslēgvārdu (meklē gan galamērķī, gan aprakstā)

---

### ✅ Rediģēt ceļojumu
- Izvēlies `4. Rediģēt...`
- Norādi ceļojuma numuru
- Ievadi jaunos laukus

---

### ✅ Dzēst ceļojumu
- Izvēlies `5. Dzēst...`
- Norādi ceļojuma numuru

---

### ✅ Kārtot ceļojumus
- Izvēlies `6. Kārtot...`
- Izvēlies kārtošanu pēc datuma vai nosaukuma

---

### ✅ Statistika
- Izvēlies `7. Statistika`
- Tiek rādīts:  
  - Kopējais ceļojumu skaits  
  - Apmeklēto valstu skaits  
  - Ceļojumu sadalījums pa gadiem

---

## 📂 Datu struktūra

Katrs ceļojums tiek saglabāts `.json` failā šādā formātā:
```json
{
  "name": "Ceļojums uz Itāliju",
  "destination": "Roma",
  "date": "2024-07-15",
  "description": "Apmeklēju Kolizeju un Panteonu."
}
