from flask import Flask, render_template, request, send_from_directory, redirect, url_for, session, jsonify
from mysql.connector import pooling
from dotenv import load_dotenv
import os
from functools import wraps

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

load_dotenv(override=True)

# dbconfig = {
#     "host": os.getenv('DB_HOST'),
#     "port": os.getenv('DB_PORT'),
#     "user": os.getenv('DB_USER'),
#     "password": os.getenv('DB_PASSWORD'),
#     "database": os.getenv('DB_NAME'),
# }

# # Increase pool size if needed
# cnxpool = pooling.MySQLConnectionPool(pool_name="mypool",
#                                       pool_size=32,  # Increase if necessary
#                                       **dbconfig)
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'email' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

# def get_candidate_profile2():
#     cnx = cnxpool.get_connection()
#     try:
#         cur = cnx.cursor()
#         cur.execute('SELECT * FROM candidates')
#         candidate2 = cur.fetchall()
#     finally:
#         cur.close()
#         cnx.close()
#     return candidate2

# def get_candidate_profile():
#     cnx = cnxpool.get_connection()
#     try:
#         cur = cnx.cursor(dictionary=True)
#         cur.execute('SELECT * FROM candidates')
#         candidate = cur.fetchall()
#     finally:
#         cur.close()
#         cnx.close()
#     return candidate

# def get_skills_candidate(candidate_ids):
#     cnx = cnxpool.get_connection()
#     try:
#         cur = cnx.cursor(dictionary=True)
#         format_strings = ','.join(['%s'] * len(candidate_ids))
#         cur.execute(f"SELECT * FROM skills WHERE candidate_id IN ({format_strings})", tuple(candidate_ids))
#         skills = cur.fetchall()
#     finally:
#         cur.close()
#         cnx.close()
#     return skills

@app.route('/')
def index():
    # candidate = get_candidate_profile()
    # return render_template('index.html', candidate=candidate)
    return render_template('index.html')

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         email = request.form['email']
#         password = request.form['password']
#         if email == 'info@winvinayafoundation.org' and password == 'Winvinaya@123&':
#             session['email'] = email
#             return redirect(url_for('admin'))
#         else:
#             error = 'Invalid email or password. Please try again.'
#             return render_template('login.html', error=error)
#     return render_template('login.html')

# @app.route('/logout')
# def logout():
#     session.pop('email', None)
#     return redirect(url_for('login'))

# @app.route('/admin')
# @login_required
# def admin():
#     candidates = get_candidate_profile2()
    
#     return render_template('admin.html', candidates=candidates)

# @app.route('/candidates-profile')
# @login_required
# def candidates_profile():
#     category = request.args.get('category', 'all')
#     disability = request.args.get('disability', 'all')
#     domain = request.args.get('domain', 'all')
#     experience = request.args.get('experience', 'all')
#     search = request.args.get('search', '')

#     query = "SELECT * FROM candidates WHERE 1=1"
#     params = {}

#     if category and category != 'all':
#         query += " AND category = %(category)s"
#         params['category'] = category
    
#     if disability and disability != 'all':
#         query += " AND disability_type = %(disability)s"
#         params['disability'] = disability
    
#     if domain and domain != 'all':
#         query += " AND domain = %(domain)s"
#         params['domain'] = domain
    
#     if experience and experience != 'all':
#         query += " AND experience = %(experience)s"
#         params['experience'] = experience

#     if search:
#         query += " AND name LIKE %(search)s"
#         params['search'] = f"%{search}%"

#     cnx = cnxpool.get_connection()
#     try:
#         cur = cnx.cursor(dictionary=True)
#         cur.execute(query, params)
#         candidates = cur.fetchall()
#     finally:
#         cur.close()
#         cnx.close()

#     if candidates:
#         candidate_ids = [candidate['id'] for candidate in candidates]
#         skills = get_skills_candidate(candidate_ids)

#         # Map skills to candidates
#         candidate_skills = {candidate['id']: [] for candidate in candidates}
#         for skill in skills:
#             candidate_skills[skill['candidate_id']].append(skill['skill_name'])

#         # Add skills to each candidate
#         for candidate in candidates:
#             candidate['skills'] = candidate_skills[candidate['id']]
#     else:
#         candidates = []
#         skills = []

#     return render_template('candidates_profile.html', candidates=candidates)


# @app.route('/search')
# def search():
#     search_query = request.args.get('query', '').strip()

#     query = "SELECT * FROM candidates WHERE name LIKE %s"
#     cnx = cnxpool.get_connection()
#     try:
#         cur = cnx.cursor()
#         cur.execute(query, ('%' + search_query + '%',))
#         students = cur.fetchall()
#     finally:
#         cur.close()
#         cnx.close()

#     return render_template('student_profiles.html', students=students)

# @app.route('/download_resume/<filename>')
# def download_resume(filename):
#     resume_path = os.path.join('static/uploads/resume', filename)
#     if os.path.exists(resume_path):
#         return send_from_directory(directory='static/uploads/resume', path=filename, as_attachment=True)
#     else:
#         return 'Resume not found', 404

# @app.route('/download_pdf/<filename>')
# def download_pdf(filename):
#     pdf_path = os.path.join('static/uploads/pdf', filename)
#     if os.path.exists(pdf_path):
#         return send_from_directory(directory='static/uploads/pdf', path=filename, as_attachment=True)
#     else:
#         return 'PDF not found', 404

# @app.route('/add-candidate', methods=['GET', 'POST'])
# @login_required
# def add_candidate():
#     if request.method == 'POST':
#         name = request.form['name']
#         age = request.form['age']
#         gender = request.form['gender']
#         phone = request.form['phone']
#         email = request.form['email']
#         category = request.form['category']
#         disability = request.form.get('disability')
#         disability_percentage = request.form['percentage']

#         if not disability_percentage:
#             disability_percentage = None
#         else:
#             try:
#                 disability_percentage = float(disability_percentage)
#             except ValueError:
#                 return render_template('admin.html', error="Invalid disability percentage. Must be a decimal number.")

#         qualification = request.form['qualification']
#         department = request.form['department']
#         graduation_year = request.form['graduation-year']
#         domain = request.form['domain']
#         skills = request.form['skills']
#         skill_list = [skill.strip() for skill in skills.split(',')]
#         typing_speed = request.form['typing-speed']
#         quality = request.form['quality']
#         experience = request.form['experience']
#         photo = request.files['photo']
#         pdf = request.files['pdf']
#         resume = request.files['resume']
#         video = request.files['video']

#         photo.save(f'static/uploads/image/{photo.filename}')
#         pdf.save(f'static/uploads/pdf/{pdf.filename}')
#         resume.save(f'static/uploads/resume/{resume.filename}')
#         video.save(f'static/uploads/video/{video.filename}')

#         cnx = cnxpool.get_connection()
#         try:
#             cur = cnx.cursor()
#             # Insert candidate details
#             cur.execute("""
#                 INSERT INTO candidates (name, age, gender, phone, email, category, disability_type, disability_percentage, highest_qualification, department, graduation_year, domain, typing_speed, quality, experience, photo, resume, pdf, video)
#                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
#             """, (name, age, gender, phone, email, category, disability, disability_percentage, qualification, department, graduation_year, domain, typing_speed, quality, experience, photo.filename, resume.filename, pdf.filename, video.filename))
#             candidate_id = cur.lastrowid

#             # Insert each skill
#             for skill in skill_list:
#                 cur.execute("INSERT INTO skills (candidate_id, skill_name) VALUES (%s, %s)", (candidate_id, skill))
            
#             cnx.commit()
#         finally:
#             cur.close()
#             cnx.close()
#         return redirect(url_for('candidates_profile'))

#     return render_template('add_candidate.html')

# @app.route('/update_candidate', methods=['POST'])
# @login_required
# def update_candidate():
#     data = request.form.to_dict()
#     id = int(data['id'])
#     name = data['name']
#     age = int(data['age'])
#     gender = data['gender']
#     phone = data['phone']
#     email = data['email']
#     category = data['category']
#     disability_type = data['disability']
#     disability_percentage = int(data['percentage']) if data['percentage'] else None
#     highest_qualification = data['qualification']
#     department = data['department']
#     graduation_year = int(data['graduation-year'])
#     domain = data['domain']
#     typing_speed = data['typing-speed']
#     quality = data['quality']
#     experience = data['experience']

#     params = (
#         name, age, gender, phone, email, category, disability_type, disability_percentage, highest_qualification, 
#         department, graduation_year, domain, typing_speed, quality, experience, id
#     )

#     cnx = cnxpool.get_connection()
#     try:
#         cur = cnx.cursor()
#         cur.execute("""
#             UPDATE candidates SET
#                 name=%s, age=%s, gender=%s, phone=%s, email=%s, category=%s, disability_type=%s, disability_percentage=%s, 
#                 highest_qualification=%s, department=%s, graduation_year=%s, domain=%s, typing_speed=%s, 
#                 quality=%s, experience=%s
#             WHERE id=%s
#         """, params)
#         cnx.commit()
#     finally:
#         cur.close()
#         cnx.close()

#     return jsonify({"status": "success"})

# @app.route('/delete_candidate', methods=['POST'])
# @login_required
# def delete_candidate():
#     candidate_id = request.form['id']

#     cnx = cnxpool.get_connection()
#     try:
#         cur = cnx.cursor()
#         cur.execute("DELETE FROM skills WHERE candidate_id = %s", (candidate_id,))
#         cur.execute("DELETE FROM candidates WHERE id = %s", (candidate_id,))
#         cnx.commit()
#     finally:
#         cur.close()
#         cnx.close()

#     return jsonify({"status": "success"})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    app.secret_key = 'supersecretkey'
    
