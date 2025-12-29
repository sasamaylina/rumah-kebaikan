from flask import Flask, render_template, request, redirect, url_for, session, flash
from models.CampaignModel import CampaignModel
from models.DonationModel import DonationModel
from models.UserModel import UserModel

app = Flask(__name__)
app.secret_key = 'rumah_kebaikan_secret'

# Initialize models
campaign_model = CampaignModel()
donation_model = DonationModel()
user_model = UserModel()

# ============================================
# Authentication Helper Functions
# ============================================

def is_logged_in():
    return 'user_id' in session

def is_admin():
    return is_logged_in() and session.get('role') == 'admin'

def is_donor():
    return is_logged_in() and session.get('role') == 'donor'

# ============================================
# Public Routes
# ============================================

@app.route('/')
def index():
    campaigns = campaign_model.getActive()
    return render_template('index.html', campaigns=campaigns)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if is_logged_in():
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = user_model.find_by_username(username)
        
        if user and user['password'] == password:
            session['user_id'] = user['id']
            session['username'] = user['username']
            session['role'] = user['role']
            flash('Login berhasil! Selamat datang, ' + user['username'], 'success')
            
            if user['role'] == 'admin':
                return redirect(url_for('admin_dashboard'))
            else:
                return redirect(url_for('campaigns'))
        else:
            flash('Username atau password salah', 'error')
    
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if is_logged_in():
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        
        # Validation
        if password != confirm_password:
            flash('Password tidak cocok!', 'error')
            return render_template('register.html')
        
        if user_model.find_by_username(username):
            flash('Username sudah digunakan!', 'error')
            return render_template('register.html')
        
        if user_model.find_by_email(email):
            flash('Email sudah terdaftar!', 'error')
            return render_template('register.html')
        
        # Create user
        user_model.create(username, email, password, 'donor')
        flash('Registrasi berhasil! Silakan login.', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('Anda telah logout.', 'info')
    return redirect(url_for('index'))

# ============================================
# Donor Routes
# ============================================

@app.route('/campaigns')
def campaigns():
    campaign_list = campaign_model.getActive()
    return render_template('campaigns.html', campaigns=campaign_list)

@app.route('/campaigns/<int:campaign_id>')
def campaign_detail(campaign_id):
    campaign = campaign_model.getById(campaign_id)
    if not campaign:
        flash('Campaign tidak ditemukan', 'error')
        return redirect(url_for('campaigns'))
    
    donations = donation_model.getByCampaignId(campaign_id)
    return render_template('campaign_detail.html', campaign=campaign, donations=donations)

@app.route('/campaigns/<int:campaign_id>/donate', methods=['GET', 'POST'])
def donate(campaign_id):
    if not is_logged_in():
        flash('Silakan login untuk berdonasi', 'error')
        return redirect(url_for('login'))
    
    campaign = campaign_model.getById(campaign_id)
    if not campaign:
        flash('Campaign tidak ditemukan', 'error')
        return redirect(url_for('campaigns'))
    
    if request.method == 'POST':
        try:
            jumlah = int(request.form['jumlah'])
            message = request.form.get('message', '')
            
            if jumlah < 1000:
                flash('Minimal donasi Rp 1.000', 'error')
                return render_template('donate.html', campaign=campaign)
            
            # Create donation
            donation_model.create(session['user_id'], campaign_id, jumlah, message)
            
            # Update campaign terkumpul
            campaign_model.updateTerkumpul(campaign_id, jumlah)
            
            flash(f'Terima kasih! Donasi sebesar Rp {jumlah:,} berhasil.', 'success')
            return redirect(url_for('my_donations'))
        except ValueError:
            flash('Jumlah donasi tidak valid', 'error')
    
    return render_template('donate.html', campaign=campaign)

@app.route('/my-donations')
def my_donations():
    if not is_logged_in():
        flash('Silakan login untuk melihat riwayat donasi', 'error')
        return redirect(url_for('login'))
    
    donations = donation_model.getByUserId(session['user_id'])
    return render_template('my_donations.html', donations=donations)

# ============================================
# Admin Routes
# ============================================

@app.route('/admin/dashboard')
def admin_dashboard():
    if not is_admin():
        flash('Akses ditolak. Hanya untuk admin.', 'error')
        return redirect(url_for('login'))
    
    stats = {
        'total_campaigns': campaign_model.countAll(),
        'total_donations': donation_model.getTotalDonations(),
        'total_donors': donation_model.countDonors(),
        'total_transactions': donation_model.countAll()
    }
    
    recent_donations = donation_model.getAll()[:5]
    campaigns = campaign_model.getAll()[:5]
    
    return render_template('dashboard.html', stats=stats, recent_donations=recent_donations, campaigns=campaigns)

@app.route('/admin/campaigns')
def admin_campaigns():
    if not is_admin():
        flash('Akses ditolak. Hanya untuk admin.', 'error')
        return redirect(url_for('login'))
    
    campaign_list = campaign_model.getAll()
    return render_template('admin_campaigns.html', campaigns=campaign_list)

@app.route('/admin/campaigns/create', methods=['GET', 'POST'])
def admin_campaign_create():
    if not is_admin():
        flash('Akses ditolak. Hanya untuk admin.', 'error')
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        data = {
            'nama': request.form['nama'],
            'deskripsi': request.form.get('deskripsi', ''),
            'alamat': request.form.get('alamat', ''),
            'kebutuhan': request.form.get('kebutuhan', 0),
            'terkumpul': 0,
            'is_active': 1 if request.form.get('is_active') else 0
        }
        campaign_model.create(data)
        flash('Campaign berhasil dibuat!', 'success')
        return redirect(url_for('admin_campaigns'))
    
    return render_template('admin_campaign_form.html', campaign=None, action='create')

@app.route('/admin/campaigns/<int:campaign_id>/edit', methods=['GET', 'POST'])
def admin_campaign_edit(campaign_id):
    if not is_admin():
        flash('Akses ditolak. Hanya untuk admin.', 'error')
        return redirect(url_for('login'))
    
    campaign = campaign_model.getById(campaign_id)
    if not campaign:
        flash('Campaign tidak ditemukan', 'error')
        return redirect(url_for('admin_campaigns'))
    
    if request.method == 'POST':
        data = {
            'nama': request.form['nama'],
            'deskripsi': request.form.get('deskripsi', ''),
            'alamat': request.form.get('alamat', ''),
            'kebutuhan': request.form.get('kebutuhan', 0),
            'terkumpul': request.form.get('terkumpul', 0),
            'is_active': 1 if request.form.get('is_active') else 0
        }
        campaign_model.update(campaign_id, data)
        flash('Campaign berhasil diperbarui!', 'success')
        return redirect(url_for('admin_campaigns'))
    
    return render_template('admin_campaign_form.html', campaign=campaign, action='edit')

@app.route('/admin/campaigns/<int:campaign_id>/delete', methods=['POST'])
def admin_campaign_delete(campaign_id):
    if not is_admin():
        flash('Akses ditolak. Hanya untuk admin.', 'error')
        return redirect(url_for('login'))
    
    campaign = campaign_model.getById(campaign_id)
    if campaign:
        campaign_model.delete(campaign_id)
        flash('Campaign berhasil dihapus!', 'success')
    else:
        flash('Campaign tidak ditemukan', 'error')
    
    return redirect(url_for('admin_campaigns'))

@app.route('/admin/donations')
def admin_donations():
    if not is_admin():
        flash('Akses ditolak. Hanya untuk admin.', 'error')
        return redirect(url_for('login'))
    
    donations = donation_model.getAll()
    return render_template('admin_donations.html', donations=donations)

# ============================================
# Run Application
# ============================================

if __name__ == '__main__':
    app.run(debug=True)