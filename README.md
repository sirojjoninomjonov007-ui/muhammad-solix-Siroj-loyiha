# 📋 Muhammad-Solix-Siroj Loyiha - TODO API


---

## 👥 FOYDALANUVCHILAR (Users)

### 🔐 Ro'yxatdan O'tish (Registration)

**Yangi foydalanuvchini tizimga qo'shish**

- **URL**: `/api/v1/user/register/`
- **Method**: `POST`
- **Tavsifi**: Yangi foydalanuvchi ro'yxatdan o'tkazish va hisob ochish.
- **Autentifikatsiya**: ❌ Talab qilinmaydi (Ochiq Endpoint)

**📤 So'rov (Request Body)**:
```json
{
    "username": "foydalanuvchi_nomi",
    "password": "parol",
    "first_name": "ism",
    "last_name": "familiya"
}
```

**📥 Javob (Response)**:
```json
{
    "id": 1,
    "username": "foydalanuvchi_nomi",
    "first_name": "ism",
    "last_name": "familiya",
    "message": "User registered successfully"
}
```

**✅ Muvaffaqiyatli Kod**: `201 Created`

---

### 🔑 Kirish (Login)

**Tizimga kirib JWT token olish**

- **URL**: `/api/v1/user/login/`
- **Method**: `POST`
- **Tavsifi**: Foydalanuvchi tizimga kirib, JWT token oladi.
- **Autentifikatsiya**: ❌ Talab qilinmaydi (Ochiq Endpoint)

**📤 So'rov (Request Body)**:
```json
{
    "username": "foydalanuvchi_nomi", 
    "password": "parol"
}
```

**📥 Javob (Response)**:
```json
{
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "user": {
        "id": 1,
        "username": "foydalanuvchi_nomi",
        "first_name": "ism",
        "last_name": "familiya"
    }
}
```

**✅ Muvaffaqiyatli Kod**: `200 OK`

---

## ✏️ TODO OPERATSIYALARI (Todos)

### ✨ Todo Yaratish (Create Todo)

**Yangi todo qo'shish**

- **URL**: `/api/v1/todos/`
- **Method**: `POST`
- **Tavsifi**: Yangi todo qo'shish.
- **Autentifikatsiya**: ✅ JWT Token Talab (Authorization: Bearer \<token\>)

**📤 So'rov (Request Body)**:
```json
{
    "title": "Todo sarlavhasi",
    "description": "Todo tavsifi",
    "date_time": "2024-12-31T23:59:00Z",
    "is_completed": false
}
```

**📥 Javob (Response)**:
```json
{
    "id": 1,
    "user_id": 1,
    "title": "Todo sarlavhasi",
    "description": "Todo tavsifi",
    "date_time": "2024-12-31T23:59:00Z",
    "is_completed": false,
    "created_at": "2024-01-01T12:00:00Z"
}
```

**✅ Muvaffaqiyatli Kod**: `201 Created`

---

### 📖 Todo Ro'yxatini Olish (List Todos)

**Foydalanuvchining barcha todolarini ko'rish**

- **URL**: `/api/v1/todos/`
- **Method**: `GET`
- **Tavsifi**: Foydalanuvchining barcha todoları ko'rish.
- **Autentifikatsiya**: ✅ JWT Token Talab

**📥 Javob (Response)**:
```json
[
    {
        "id": 1,
        "user_id": 1,
        "title": "Todo sarlavhasi",
        "description": "Todo tavsifi",
        "date_time": "2024-12-31T23:59:00Z",
        "is_completed": false,
        "created_at": "2024-01-01T12:00:00Z"
    },
    {
        "id": 2,
        "user_id": 1,
        "title": "Boshqa todo",
        "description": "Boshqa tavsif",
        "date_time": "2024-11-30T18:00:00Z",
        "is_completed": true,
        "created_at": "2024-02-01T09:30:00Z"
    }
]
```

**✅ Muvaffaqiyatli Kod**: `200 OK`

---

### 🔄 Todo Yangilash (Update Todo)

**Mavjud todoni o'zgartirish**

- **URL**: `/api/v1/todos/{id}/`
- **Method**: `PUT`
- **Tavsifi**: Mavjud todoni yangilash.
- **Autentifikatsiya**: ✅ JWT Token Talab

**📤 So'rov (Request Body)**:
```json
{
    "title": "Yangilangan todo sarlavhasi",
    "description": "Yangilangan todo tavsifi",
    "date_time": "2024-12-31T23:59:00Z",
    "is_completed": true
}
```

**📥 Javob (Response)**:
```json
{
    "id": 1,
    "user_id": 1,
    "title": "Yangilangan todo sarlavhasi",
    "description": "Yangilangan todo tavsifi",
    "date_time": "2024-12-31T23:59:00Z",
    "is_completed": true,
    "created_at": "2024-01-01T12:00:00Z"
}
```

**✅ Muvaffaqiyatli Kod**: `200 OK`

---

### ❌ Todo O'chirish (Delete Todo)

**Mavjud todoni o'chirish**

- **URL**: `/api/v1/todos/{id}/`
- **Method**: `DELETE`
- **Tavsifi**: Mavjud todoni tizimdan o'chirish.
- **Autentifikatsiya**: ✅ JWT Token Talab

**📥 Javob (Response)**:
```json
{
    "message": "Todo muvaffaqiyatli o'chirildi."
}
```

**✅ Muvaffaqiyatli Kod**: `204 No Content`

---

### 🔍 Todo Tafsilotlarini Olish (Retrieve Todo)

**Bitta todonya tafsilotlar**

- **URL**: `/api/v1/todos/{id}/`
- **Method**: `GET`
- **Tavsifi**: Bitta todonya batafsil ma'lumotlar olish.
- **Autentifikatsiya**: ✅ JWT Token Talab

**📥 Javob (Response)**:
```json
{
    "id": 1,
    "user_id": 1,
    "title": "Todo sarlavhasi",
    "description": "Todo tavsifi",
    "date_time": "2024-12-31T23:59:00Z",
    "is_completed": false,
    "created_at": "2024-01-01T12:00:00Z"
}
```

**✅ Muvaffaqiyatli Kod**: `200 OK`

---

### ✔️ Todo Tugallash (Complete Todo)

**Todoni tugallangan deb belgilash**

- **URL**: `/api/v1/todos/{id}/complete/`
- **Method**: `POST`
- **Tavsifi**: Todoni tugallangan holatiga o'zgartirish.
- **Autentifikatsiya**: ✅ JWT Token Talab

**📥 Javob (Response)**:
```json
{
    "id": 1,
    "user_id": 1,
    "title": "Todo sarlavhasi",
    "description": "Todo tavsifi",
    "date_time": "2024-12-31T23:59:00Z",
    "is_completed": true,
    "created_at": "2024-01-01T12:00:00Z"
}
```

**✅ Muvaffaqiyatli Kod**: `200 OK`

---

## 🔐 AUTENTIFIKATSIYA (Authentication)

### JWT Token Ishlatish

Barcha himoyalangan API endpointlar **JWT token** orqali autentifikatsiya talab qiladi.

1. **Token Olish**: Avval `/api/v1/user/login/` dan token oling.
2. **Token Yuborish**: Keyingi so'rovlarda `Authorization` headeriga qo'shing:

```
Authorization: Bearer <your_jwt_token_here>
```

### Token Yangilash

Access token tugadi bo'lsa, refresh token orqali yangi token olib olishingiz mumkin:

- **URL**: `/api/v1/user/token/refresh/`
- **Method**: `POST`
- **Request Body**:
```json
{
    "refresh": "your_refresh_token_here"
}
```

---

## ⚠️ Xato Javoblari (Error Responses)

### 400 Bad Request
```json
{
    "error": "Invalid request data"
}
```

### 401 Unauthorized
```json
{
    "error": "Invalid username or password"
}
```

### 403 Forbidden
```json
{
    "detail": "Authentication credentials were not provided."
}
```

### 404 Not Found
```json
{
    "detail": "Not found."
}
```

---

## 📝 Eslatma

- ✅ Barcha API endpointlar JWT token orqali autentifikatsiya talab qiladi (faqat **register** va **login** ochiq).
- 🔒 Parollar bazada xesh qilib saqlaladi (bcrypt).
- 📅 Vaqt formati: ISO 8601 (2024-12-31T23:59:00Z)
- 🌍 TimeZone: UTC
- 📦 Response Content-Type: `application/json`

---

## 🚀 API Ishga Tushirish

```bash
# Virtual muhit yaratish
python -m venv venv

# Virtual muhitni faollashtirish (Windows)
venv\Scripts\activate

# Kerakli paketlarni o'rnatish
pip install -r requirements.txt

# Migratsiyalarni bajarish
python manage.py migrate

# Server ishga tushirish
python manage.py runserver
```

Server manzili: `http://localhost:8000`

---

**Oxirgi yangilash**: 2024-04-26
**API Versiyasi**: v1
