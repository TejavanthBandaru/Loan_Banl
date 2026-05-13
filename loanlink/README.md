# LoanLink Hyderabad – Flask Website

A modern, professional loan company website built with **Python Flask**, **Bootstrap 5**, **MySQL**, and clean Jinja2 templating.

---

## 📁 Project Structure

```
loanlink/
├── app.py                    # Main Flask application & routes
├── requirements.txt          # Python dependencies
├── Procfile                  # Gunicorn start command (Render)
├── .env.example              # Environment variable template
├── .gitignore
├── templates/
│   ├── base.html             # Master layout (navbar + footer + loader)
│   ├── home.html             # Landing page
│   ├── about.html            # About Us page
│   ├── services.html         # Loan Services page
│   ├── eligibility.html      # Eligibility + EMI Calculator
│   ├── contact.html          # Contact + Loan Enquiry Form
│   └── 404.html              # Custom error page
└── static/
    ├── css/
    │   └── style.css         # Global design system
    ├── js/
    │   ├── main.js           # Global JS (loader, navbar, AOS)
    │   └── home.js           # Hero EMI calculator
    └── images/
        └── favicon.svg
```

---

## ⚡ Local Setup

### 1. Clone / Download

```bash
git clone https://github.com/yourname/loanlink.git
cd loanlink
```

### 2. Create Virtual Environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment

```bash
cp .env.example .env
# Edit .env with your MySQL credentials and a strong SECRET_KEY
```

### 5. Set Up MySQL Database

```sql
CREATE DATABASE loanlink_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

The `leads` table is created automatically when you run the app (`init_db()` in `app.py`).

### 6. Run the App

```bash
python app.py
```

Visit: **http://localhost:5000**

---

## 🗄️ Database Schema

```sql
CREATE TABLE leads (
    id          INT AUTO_INCREMENT PRIMARY KEY,
    name        VARCHAR(120)  NOT NULL,
    phone       VARCHAR(20)   NOT NULL,
    email       VARCHAR(150),
    loan_amount VARCHAR(50),
    loan_type   VARCHAR(80),
    message     TEXT,
    created_at  DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

---

## 🚀 Deploy to Render (Free Tier)

### Step 1: Push to GitHub

```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/yourname/loanlink.git
git push -u origin main
```

### Step 2: Create Web Service on Render

1. Go to [render.com](https://render.com) → **New → Web Service**
2. Connect your GitHub repository
3. Configure:
   - **Name:** `loanlink-hyderabad`
   - **Runtime:** Python 3
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app --bind 0.0.0.0:$PORT`
   - **Instance Type:** Free

### Step 3: Add Environment Variables on Render

In Render dashboard → Environment → Add these:

| Key            | Value                        |
|----------------|------------------------------|
| `SECRET_KEY`   | `your-strong-random-key`     |
| `FLASK_DEBUG`  | `False`                      |
| `DB_HOST`      | your MySQL host              |
| `DB_USER`      | your MySQL user              |
| `DB_PASSWORD`  | your MySQL password          |
| `DB_NAME`      | `loanlink_db`                |
| `DB_PORT`      | `3306`                       |

> **Tip:** Use [PlanetScale](https://planetscale.com) or [Aiven](https://aiven.io) for free hosted MySQL on Render.

### Step 4: Deploy

Click **Deploy** — Render will build and deploy automatically. Your site will be live at:
`https://loanlink-hyderabad.onrender.com`

---

## 🎨 Design System

| Token          | Value               |
|----------------|---------------------|
| Navy           | `#0a1f44`           |
| Red            | `#d72b2b`           |
| White          | `#ffffff`           |
| Heading Font   | Playfair Display    |
| Body Font      | DM Sans             |
| Border Radius  | 14px (cards)        |

---

## 📞 Contact Details (hard-coded in `app.py` context processor)

- **Phone:** +91 9550131314
- **Hours:** Mon–Sat: 10 AM – 7 PM
- **Address:** 3rd Floor, Kondapur Main Road, Hyderabad – 500084

---

## 📋 Pages & Routes

| URL              | Template           | Description                    |
|------------------|--------------------|--------------------------------|
| `/`              | `home.html`        | Hero, stats, services, FAQ     |
| `/about`         | `about.html`       | Company story, mission, values |
| `/services`      | `services.html`    | Detailed loan products         |
| `/eligibility`   | `eligibility.html` | Criteria, docs, EMI calculator |
| `/contact`       | `contact.html`     | Enquiry form (saves to MySQL)  |
| `/api/quick-enquiry` | JSON API      | AJAX quick lead capture        |

---

## ✅ Features Checklist

- [x] Sticky navbar with active state
- [x] Top info bar (hours, phone, email)
- [x] Hero with live EMI calculator card
- [x] 5 loan product cards with details
- [x] Stats counter section
- [x] Why Choose Us feature grid
- [x] How It Works (3-step process)
- [x] Testimonials section
- [x] FAQ accordion
- [x] Eligibility criteria by profile type
- [x] Documents checklist
- [x] Full EMI Calculator page
- [x] Loan enquiry form with MySQL storage
- [x] Flash messages (success / error)
- [x] WhatsApp floating button
- [x] Scroll-to-top button
- [x] Page loader animation
- [x] Custom 404 page
- [x] Scroll-reveal animations (AOS-style)
- [x] Fully mobile responsive (Bootstrap 5)
- [x] SEO meta tags on all pages
- [x] Jinja2 context processor for global vars
- [x] Gunicorn + Procfile for Render deployment
