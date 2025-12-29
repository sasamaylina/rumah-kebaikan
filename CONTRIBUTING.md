# Contributing to Rumah Kebaikan

Terima kasih atas minat Anda untuk berkontribusi pada **Rumah Kebaikan**! Kontribusi dari community sangat kami hargai.

---

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [How to Contribute](#how-to-contribute)
- [Coding Guidelines](#coding-guidelines)
- [Commit Message Guidelines](#commit-message-guidelines)
- [Pull Request Process](#pull-request-process)
- [Bug Reports](#bug-reports)
- [Feature Requests](#feature-requests)

---

## Code of Conduct

Dengan berpartisipasi dalam proyek ini, Anda setuju untuk menjaga lingkungan yang respectful dan inclusive. Kami mengharapkan:

- ✅ Gunakan bahasa yang welcoming dan inclusive
- ✅ Respect terhadap pandangan dan pengalaman berbeda
- ✅ Terima kritik konstruktif dengan graceful
- ✅ Fokus pada apa yang terbaik untuk komunitas
- ❌ No harassment, trolling, atau personal attacks

---

## Getting Started

### Prerequisites

- Python 3.9+
- MySQL 8.0+
- Git
- Text editor atau IDE (VSCode, PyCharm, etc.)

### Fork dan Clone

1. **Fork** repository ini via GitHub
2. **Clone** fork Anda:
```bash
git clone https://github.com/YOUR_USERNAME/rumah-kebaikan.git
cd rumah-kebaikan
```

3. **Add upstream** remote:
```bash
git remote add upstream https://github.com/sasamaylina/rumah-kebaikan.git
```

---

## Development Setup

### 1. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Setup Database

```bash
# Buat database
mysql -u root -p
CREATE DATABASE rumah_kebaikan;
USE rumah_kebaikan;
SOURCE rumah_kebaikan.sql;
exit;
```

### 4. Configure Environment

```bash
cp .env.example .env
# Edit .env dengan database credentials Anda
```

### 5. Run Development Server

```bash
python app.py
```

Visit: http://127.0.0.1:5000

---

## 🎯 How to Contribute

### Types of Contributions

- 🐛 **Bug fixes**
- ✨ **New features**
- 📝 **Documentation improvements**
- 🎨 **UI/UX enhancements**
- ♻️ **Code refactoring**
- ✅ **Tests**
- 🌍 **Translations**

### Workflow

1. **Sync dengan upstream:**
```bash
git fetch upstream
git checkout main
git merge upstream/main
```

2. **Create a branch:**
```bash
git checkout -b feature/your-feature-name
# atau
git checkout -b fix/bug-description
```

Format branch names:
- `feature/` - untuk fitur baru
- `fix/` - untuk bug fixes
- `docs/` - untuk dokumentasi
- `refactor/` - untuk refactoring
- `test/` - untuk tests

3. **Make your changes**

4. **Test thoroughly:**
```bash
# Test manual semua affected features
# Pastikan tidak ada error
```

5. **Commit changes:**
```bash
git add .
git commit -m "feat: add new donation filter feature"
```

6. **Push to your fork:**
```bash
git push origin feature/your-feature-name
```

7. **Create Pull Request** via GitHub

---

## 📐 Coding Guidelines

### Python Style Guide

Ikuti **PEP 8** style guide:

#### Naming Conventions

```python
# Classes: PascalCase
class UserModel:
    pass

# Functions & variables: snake_case
def get_user_donations(user_id):
    total_amount = 0
    return total_amount

# Constants: UPPER_CASE
MAX_DONATION_AMOUNT = 1000000000
```

#### Code Formatting

```python
# Good: Proper spacing
def create_campaign(name, description, target):
    if not name or not description:
        return None
    
    campaign = Campaign(
        name=name,
        description=description,
        target=target
    )
    return campaign

# Bad: No spacing, unclear
def create_campaign(name,description,target):
    if not name or not description:return None
    campaign=Campaign(name=name,description=description,target=target)
    return campaign
```

#### Docstrings

Tambahkan docstrings untuk fungsi-fungsi penting:

```python
def calculate_campaign_progress(campaign_id):
    """
    Calculate campaign fundraising progress percentage.
    
    Args:
        campaign_id (int): ID of the campaign
        
    Returns:
        float: Progress percentage (0-100)
        
    Raises:
        ValueError: If campaign_id is invalid
    """
    campaign = get_campaign(campaign_id)
    if not campaign:
        raise ValueError(f"Campaign {campaign_id} not found")
    
    progress = (campaign['terkumpul'] / campaign['kebutuhan']) * 100
    return min(progress, 100)
```

### Database Guidelines

#### Use Parameterized Queries

```python
# Good: Parameterized query (safe)
cursor.execute(
    "SELECT * FROM campaigns WHERE id = %s",
    (campaign_id,)
)

# Bad: String concatenation (SQL injection risk!)
cursor.execute(
    f"SELECT * FROM campaigns WHERE id = {campaign_id}"
)
```

#### Always Close Connections

```python
# Good: Using try-finally
connection = get_db_connection()
try:
    with connection.cursor() as cursor:
        cursor.execute(sql)
        result = cursor.fetchall()
    connection.commit()
    return result
finally:
    connection.close()
```

### HTML/Template Guidelines

#### Use CSRF Protection

```html
<!-- Good: Include CSRF token -->
<form method="POST" action="/donate">
    {{ csrf_token() }}
    <input type="number" name="amount" required>
    <button type="submit">Donate</button>
</form>
```

#### Proper Jinja2 Escaping

```html
<!-- Good: Auto-escaped -->
<p>{{ user_message }}</p>

<!-- If you REALLY need raw HTML (be careful!) -->
<div>{{ content | safe }}</div>
```

### Security Guidelines

#### Never Commit Secrets

```python
# Bad: Hardcoded secret
SECRET_KEY = 'my-secret-123'

# Good: From environment
SECRET_KEY = os.getenv('SECRET_KEY')
```

#### Validate All User Inputs

```python
# Good: Input validation
amount = request.form.get('amount', '').strip()
try:
    amount = int(amount)
    if amount < 1000:
        flash('Minimal donasi Rp 1.000', 'error')
        return redirect(url_for('donate'))
except ValueError:
    flash('Jumlah tidak valid', 'error')
    return redirect(url_for('donate'))
```

---

## 💬 Commit Message Guidelines

Gunakan **Conventional Commits** format:

### Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Types

- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc)
- `refactor`: Code refactoring
- `test`: Adding tests
- `chore`: Maintenance tasks

### Examples

```bash
# Feature
git commit -m "feat(donations): add donation filters by date range"

# Bug fix
git commit -m "fix(auth): resolve password verification issue"

# Documentation
git commit -m "docs(readme): update installation instructions"

# Multiple lines
git commit -m "feat(campaigns): add campaign image upload

- Add image upload field to campaign form
- Implement file validation and storage
- Update campaign model and templates

Closes #123"
```

---

## 🔄 Pull Request Process

### Before Submitting PR

- [ ] Code mengikuti style guidelines
- [ ] Semua tests passing
- [ ] Tidak ada console.log atau debug code
- [ ] Dokumentasi ter-update (jika perlu)
- [ ] Commit messages clear dan descriptive
- [ ] Branch ter-sync dengan latest main

### PR Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation
- [ ] Code refactoring

## Testing
Describe testing yang dilakukan

## Screenshots (jika UI changes)
Add screenshots here

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Documentation updated
- [ ] No breaking changes
```

### Review Process

1. Maintainer akan review dalam **48 jam**
2. Discussions dan revisions jika diperlukan
3. Approval dari minimal 1 maintainer
4. Merge to main branch

---

## 🐛 Bug Reports

### Before Reporting

1. **Search** existing issues terlebih dahulu
2. **Test** di latest version
3. **Verify** bug reproducible

### Bug Report Template

```markdown
**Bug Description**
Clear description of the bug

**Steps to Reproduce**
1. Go to '...'
2. Click on '...'
3. See error

**Expected Behavior**
What you expected to happen

**Actual Behavior**
What actually happened

**Screenshots**
If applicable

**Environment**
- OS: [e.g. Windows 10]
- Browser: [e.g. Chrome 120]
- Python Version: [e.g. 3.9.7]
- Database: [e.g. MySQL 8.0]

**Additional Context**
Any other relevant information
```

---

## ✨ Feature Requests

### Feature Request Template

```markdown
**Feature Description**
Clear description of the feature

**Problem It Solves**
What problem does this solve?

**Proposed Solution**
How would you implement this?

**Alternatives Considered**
Any alternative solutions?

**Additional Context**
Mockups, examples, etc.
```

---

## 📞 Need Help?

- 💬 **Discussions**: [GitHub Discussions](https://github.com/sasamaylina/rumah-kebaikan/discussions)
- 🐛 **Issues**: [GitHub Issues](https://github.com/sasamaylina/rumah-kebaikan/issues)
- 📧 **Email**: contribute@rumahkebaikan.id

---

## 🙏 Recognition

Kontributor akan ditambahkan ke:
- README.md Contributors section
- Release notes
- Special thanks pada major features

---

**Thank you for contributing to Rumah Kebaikan! 🎉**

Together, we can make a difference in digital fundraising.
