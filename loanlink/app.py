"""
LoanLink Hyderabad - Main Flask Application
==========================================
Entry point for the Flask web application.
Handles routing, form submissions, and database operations.
"""

from flask import Flask, render_template, request, flash, redirect, url_for, jsonify
from datetime import datetime
import os
import re

# ─── App Initialization ────────────────────────────────────────────────────────
app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'loanlink-hyderabad-secret-2024')

# ─── MySQL Configuration (via environment variables for security) ──────────────
DB_CONFIG = {
    'host':     os.environ.get('DB_HOST', 'localhost'),
    'user':     os.environ.get('DB_USER', 'root'),
    'password': os.environ.get('DB_PASSWORD', ''),
    'database': os.environ.get('DB_NAME', 'loanlink_db'),
    'port':     int(os.environ.get('DB_PORT', 3306)),
}

# ─── Database Helper ───────────────────────────────────────────────────────────
def get_db_connection():
    """Returns a MySQL connection. Install: pip install mysql-connector-python"""
    try:
        import mysql.connector
        conn = mysql.connector.connect(**DB_CONFIG)
        return conn
    except Exception as e:
        print(f"[DB ERROR] Could not connect: {e}")
        return None


def init_db():
    """Creates the leads table if it does not exist."""
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS leads (
                id          INT AUTO_INCREMENT PRIMARY KEY,
                name        VARCHAR(120)  NOT NULL,
                phone       VARCHAR(20)   NOT NULL,
                email       VARCHAR(150),
                loan_amount VARCHAR(50),
                loan_type   VARCHAR(80),
                message     TEXT,
                created_at  DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()
        cursor.close()
        conn.close()
        print("[DB] Table 'leads' ready.")


# ─── Context Processor (globals for all templates) ─────────────────────────────
@app.context_processor
def inject_globals():
    return {
        'company_name':  'LoanLink Hyderabad',
        'company_phone': '+91 9550131314',
        'company_email': 'info@loanlinkhyderabad.com',
        'company_address': '3rd Floor, Kondapur Main Road, Hyderabad – 500084',
        'whatsapp_number': '919550131314',
        'working_hours':  'Mon–Sat: 10 AM – 7 PM',
        'year':           datetime.now().year,
    }


# ─── Routes ────────────────────────────────────────────────────────────────────

@app.route('/')
def home():
    """Home page – hero, services overview, stats, testimonials, FAQ."""
    return render_template('home.html', page='home')


@app.route('/about')
def about():
    """About page – company story, team, mission & vision."""
    return render_template('about.html', page='about')


@app.route('/services')
def services():
    """Services page – detailed loan products."""
    return render_template('services.html', page='services')


@app.route('/eligibility')
def eligibility():
    """Eligibility page – criteria, documents, process steps."""
    return render_template('eligibility.html', page='eligibility')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    """Contact page with enquiry form. Saves leads to MySQL."""
    if request.method == 'POST':
        # ── Collect form data ──────────────────────────────────────────────────
        name        = request.form.get('name', '').strip()
        phone       = request.form.get('phone', '').strip()
        email       = request.form.get('email', '').strip()
        loan_amount = request.form.get('loan_amount', '').strip()
        loan_type   = request.form.get('loan_type', '').strip()
        message     = request.form.get('message', '').strip()

        # ── Basic validation ───────────────────────────────────────────────────
        errors = []
        if not name:
            errors.append('Name is required.')
        if not phone or not re.match(r'^\+?[6-9]\d{9}$', phone):
            errors.append('Enter a valid 10-digit Indian phone number.')
        if email and not re.match(r'^[\w.+-]+@[\w-]+\.[a-z]{2,}$', email, re.I):
            errors.append('Enter a valid email address.')

        if errors:
            for err in errors:
                flash(err, 'danger')
            return render_template('contact.html', page='contact',
                                   form_data=request.form)

        # ── Save to MySQL ──────────────────────────────────────────────────────
        conn = get_db_connection()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO leads
                        (name, phone, email, loan_amount, loan_type, message)
                    VALUES (%s, %s, %s, %s, %s, %s)
                """, (name, phone, email, loan_amount, loan_type, message))
                conn.commit()
                cursor.close()
            except Exception as e:
                print(f"[DB INSERT ERROR] {e}")
            finally:
                conn.close()

        flash('Thank you! We received your enquiry and will call you shortly.', 'success')
        return redirect(url_for('contact'))

    return render_template('contact.html', page='contact', form_data={})


# ─── AJAX endpoint: quick WhatsApp lead capture ────────────────────────────────
@app.route('/api/quick-enquiry', methods=['POST'])
def quick_enquiry():
    data = request.get_json(silent=True) or {}
    name  = data.get('name', '').strip()
    phone = data.get('phone', '').strip()
    ltype = data.get('loan_type', '').strip()

    if not name or not phone:
        return jsonify({'ok': False, 'msg': 'Name and phone are required.'}), 400

    conn = get_db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO leads (name, phone, loan_type)
                VALUES (%s, %s, %s)
            """, (name, phone, ltype))
            conn.commit()
            cursor.close()
        except Exception as e:
            print(f"[QUICK ENQUIRY DB ERROR] {e}")
        finally:
            conn.close()

    return jsonify({'ok': True, 'msg': 'Enquiry received!'})


# ─── 404 handler ───────────────────────────────────────────────────────────────
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


# ─── Entry ─────────────────────────────────────────────────────────────────────
if __name__ == '__main__':
    init_db()
    app.run(debug=os.environ.get('FLASK_DEBUG', 'True') == 'True',
            host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
