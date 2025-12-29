# 🔐 Security Policy

## Keamanan di Rumah Kebaikan

Kami mengambil keamanan aplikasi ini dengan sangat serius. Dokumen ini menjelaskan fitur-fitur keamanan yang telah diimplementasikan dan bagaimana melaporkan vulnerability jika ditemukan.

---

## 🛡️ Fitur Keamanan yang Diimplementasikan

### 1. Password Security

#### Password Hashing
- ✅ **Algoritma**: Bcrypt dengan cost factor 12
- ✅ **Tidak ada plain text passwords** di database
- ✅ **Salt otomatis** untuk setiap password
- ✅ **Password minimum 8 karakter**

```python
# Password di-hash sebelum disimpan
hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

# Verification aman menggunakan constant-time comparison
bcrypt.check_password_hash(hashed_password, plain_password)
```

### 2. CSRF Protection

- ✅ **Flask-WTF CSRF tokens** pada semua form
- ✅ **Automatic token generation & validation**
- ✅ **Protection untuk POST/PUT/DELETE requests**

Semua form HTML sudah include CSRF token:
```html
<form method="POST">
    {{ csrf_token() }}
    <!-- form fields -->
</form>
```

### 3. SQL Injection Prevention

- ✅ **Parameterized queries** di semua operasi database
- ✅ **Tidak ada string concatenation** untuk SQL
- ✅ **PyMySQL prepared statements**

Contoh implementasi aman:
```python
cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
```

### 4. XSS (Cross-Site Scripting) Protection

- ✅ **Flask auto-escaping** enabled untuk semua templates
- ✅ **Jinja2 automatic HTML escaping**
- ✅ **Input sanitization** pada user inputs

### 5. Security Headers

Headers yang diterapkan pada setiap response:

| Header | Value | Purpose |
|--------|-------|---------|
| `X-Content-Type-Options` | `nosniff` | Prevent MIME-type sniffing |
| `X-Frame-Options` | `SAMEORIGIN` | Prevent clickjacking |
| `X-XSS-Protection` | `1; mode=block` | Enable browser XSS protection |
| `Strict-Transport-Security` | `max-age=31536000` | Force HTTPS (production only) |

### 6. Session Security

- ✅ **HTTPOnly cookies** - Tidak accessible via JavaScript
- ✅ **SameSite cookies** - CSRF protection
- ✅ **Secure flag** untuk HTTPS (production)
- ✅ **Session timeout** otomatis
- ✅ **Server-side session storage**

```python
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SAMESITE = 'Lax'
SESSION_COOKIE_SECURE = True  # Production only (HTTPS)
```

### 7. Environment-Based Configuration

- ✅ **No hard-coded credentials** dalam source code
- ✅ **python-dotenv** untuk environment variables
- ✅ **`.env` file  tidak di-track git**
- ✅ **Separate config** untuk dev/production

### 8. Input Validation

- ✅ **Server-side validation** untuk semua inputs
- ✅ **Type checking** dan sanitization
- ✅ **Email format validation**
- ✅ **Password strength requirements**
- ✅ **Integer validation** untuk amounts

---

## 🔒 Best Practices untuk Deployment

### Production Environment

#### 1. Environment Variables
```env
# Gunakan strong SECRET_KEY
SECRET_KEY=generate-random-string-min-32-chars

# Disable debug mode
FLASK_ENV=production
FLASK_DEBUG=False

# Enable secure cookies (require HTTPS)
SESSION_COOKIE_SECURE=True
SESSION_COOKIE_SAMESITE=Strict
```

#### 2. Database Security

- ✅ Gunakan user database dengan **privilege terbatas**
- ✅ Jangan gunakan `root` user
- ✅ Enable **MySQL SSL connection** jika memungkinkan
- ✅ **Firewall** database port, hanya allow dari app server
- ✅ **Regular backups** database

```sql
-- Buat user dengan privilege terbatas
CREATE USER 'rumah_kebaikan_app'@'localhost' IDENTIFIED BY 'strong_password';
GRANT SELECT, INSERT, UPDATE, DELETE ON rumah_kebaikan.* TO 'rumah_kebaikan_app'@'localhost';
FLUSH PRIVILEGES;
```

#### 3. HTTPS/SSL

- ✅ **Wajib gunakan HTTPS** di production
- ✅ Gunakan valid SSL certificate (Let's Encrypt gratis)
- ✅ Redirect HTTP ke HTTPS
- ✅ Enable HSTS header

#### 4. Server Security

- ✅ **Update sistem** secara regular
- ✅ **Firewall** hanya allow port yang diperlukan (80, 443)
- ✅ **Fail2ban** untuk protect brute force
- ✅ **Rate limiting** untuk login attempts
- ✅ **Monitoring & logging**

#### 5. Application Security

- ✅ **Update dependencies** secara regular
- ✅ Run vulnerability scan: `pip install safety && safety check`
- ✅ **File permissions** yang proper
- ✅ Disable **directory listing**
- ✅ **Error messages** tidak expose sensitive info

---

## 🚨 Vulnerability Reporting

Jika Anda menemukan security vulnerability, **JANGAN** buat public issue di GitHub.

### Cara Melaporkan

1. **Email** ke: security@rumahkebaikan.id
2. **Subject**: `[SECURITY] Brief description`
3. **Include**:
   - Deskripsi detail vulnerability
   - Steps untuk reproduce
   - Potential impact
   - Suggested fix (jika ada)

### Response Timeline

- **24 jam**: Konfirmasi penerimaan report
- **72 jam**: Initial assessment
- **7 hari**: Status update atau fix

### Responsible Disclosure

Kami berkomitmen untuk:
- ✅ Merespons laporan dengan cepat
- ✅ Menjaga kerahasiaan reporter
- ✅ Credit kepada reporter (jika diinginkan)
- ✅ Update public setelah fix deployed

---

## 📋 Security Checklist

Sebelum go live, pastikan:

### Pre-Deployment
- [ ] Semua dependencies ter-update
- [ ] Security scan passed (`safety check`)
- [ ] No hardcoded secrets dalam code
- [ ] `.env` tidak di-commit ke git
- [ ] Strong `SECRET_KEY` generated
- [ ] Default passwords diganti
- [ ] Database user memiliki privilege minimal

### Production Configuration
- [ ] `FLASK_DEBUG=False`
- [ ] `FLASK_ENV=production`
- [ ] `SESSION_COOKIE_SECURE=True`
- [ ] HTTPS enabled dengan valid certificate
- [ ] Security headers configured
- [ ] Database SSL enabled (jika memungkinkan)

### Server Security
- [ ] Firewall configured
- [ ] SSH key-based auth (disable password)
- [ ] Regular backup enabled
- [ ] Monitoring & alerting setup
- [ ] Log rotation configured
- [ ] Rate limiting implemented

### Application Security
- [ ] All forms have CSRF protection
- [ ] Password requirements enforced
- [ ] Input validation implemented
- [ ] Error handling tidak leak info
- [ ] Session timeout configured

---

## 🔍 Security Testing

### Automated Testing

```bash
# Check Python dependencies vulnerabilities
pip install safety
safety check

# Basic security headers check (manual via browser DevTools)
```

### Manual Testing

#### Test CSRF Protection
```bash
# Try to submit form tanpa CSRF token - should fail
curl -X POST http://localhost:5000/login -d "username=test&password=test"
```

#### Test SQL Injection
```bash
# Try SQL injection di login form - should fail safely
username: admin' OR '1'='1
password: anything
```

#### Test XSS
```bash
# Try XSS in donation message - should be escaped
message: <script>alert('XSS')</script>
```

---

## 📚 Security Resources

### Documentation
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [Flask Security Guide](https://flask.palletsprojects.com/en/stable/security/)
- [Python Security Best Practices](https://python.readthedocs.io/en/stable/library/security_warnings.html)

### Tools
- [Safety](https://github.com/pyupio/safety) - Python dependency vulnerability scanner
- [Bandit](https://github.com/PyCQA/bandit) - Python security linter
- [OWASP ZAP](https://www.zaproxy.org/) - Web application security scanner

---

## 📝 Security Updates

### v1.0.0 (2025-01-01)
- ✅ Implemented bcrypt password hashing
- ✅ Added CSRF protection
- ✅ Added security headers
- ✅ Environment-based configuration
- ✅ SQL injection prevention
- ✅ XSS protection

---

## 🙏 Acknowledgments

Terima kasih kepada security researchers dan community yang telah membantu meningkatkan keamanan aplikasi ini.

---

**Last Updated**: 2025-12-29  
**Security Contact**: security@rumahkebaikan.id
