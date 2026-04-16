## Social Platform Backend

Built with FastAPI • PostgreSQL • SQLAlchemy • Docker • JWT Authentication

## 📌 Overview

This project follows a modular monolithic architecture with a clean separation of concerns.

It is a scalable backend system for a social platform built with FastAPI, providing core functionality including user authentication, content management, and user interactions with secure, production-style backend design principles.
---

## 🚀 Features

* 🔐 JWT-based authentication (login & registration)
* 👤 User management system
* 📝 Post creation, update, and deletion
* 👍 Like/Vote system
* 🔒 Ownership-based access control (users can only modify their own content)
* 🗄️ PostgreSQL relational database integration
* 🔗 ORM-based database handling with SQLAlchemy
* 📦 RESTful API architecture
* 🧪 Testing with Pytest
* 🐳 Docker support for containerization
* ⚙️ CI/CD pipeline integration (GitHub Actions)
* 📖 API Documentation available at `/docs` (Swagger UI)

---

## 🛠️ Tech Stack

* FastAPI
* PostgreSQL
* SQLAlchemy
* Alembic
* Docker
* Pytest
* GitHub Actions

---

## 📂 Project Structure

```
app/
├── routers/        # API route handlers
├── models/         # Database models
├── schemas/        # Pydantic validation schemas
├── database/       # Database connection setup
├── services/       # Business logic layer
├── utils/          # Helper functions (auth, hashing, etc.)
├── config/         # Environment configuration
└── main.py         # Application entry point
```

---

## ⚡ Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/social-platform-backend.git
cd social-platform-backend
```

### 2. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
uvicorn app.main:app --reload
```

---

## 🔐 Environment Variables

Create a `.env` file in the root directory:

```
DATABASE_URL=
SECRET_KEY=
ALGORITHM=
ACCESS_TOKEN_EXPIRE_MINUTES=
```

---

## 🧪 Running Tests

```bash
pytest -v
```

---

## 📌 Future Improvements

* Role-based access control (admin/user permissions)
* Rate limiting for API protection
* Caching with Redis
* API versioning (`/api/v1`)
* Modular architecture improvements (service separation ready)
* Advanced logging and monitoring

---

## 📊 Project Status   

🚧 In active development – new features and improvements are being added regularly.

## 📄 License

This project is intended for educational and portfolio purposes.
