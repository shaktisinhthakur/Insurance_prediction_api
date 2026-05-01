# 🛡️ Insurance Premium Prediction API

> FastAPI + Machine Learning + Docker

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-Latest-green.svg)
![Docker](https://img.shields.io/badge/Docker-Available-blue.svg)

---

## 📌 Project Overview

This project is a REST API built with **FastAPI** that predicts insurance premium categories using a trained **Machine Learning model**. The API accepts user details such as age group, BMI, lifestyle risk, city tier, income, and occupation — then returns a predicted premium category.

The application is containerized using **Docker** and is publicly available on Docker Hub.

🐳 **Docker Hub:** `shaktisinh1557/insurance-prediction-api`

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| FastAPI | Web framework for REST API |
| Pydantic v2 | Input validation & schemas |
| Scikit-learn | ML model for prediction |
| Uvicorn | ASGI server |
| Docker | Containerization |

---

## 📁 Project Structure

```
insurance-premium-api/
├── app.py                  # Main FastAPI application
├── schema/
│   └── user_input.py       # Pydantic input validation schema
├── Model/
│   └── predict.py          # ML model loading & prediction logic
├── requirements.txt        # Python dependencies
└── Dockerfile              # Docker build instructions
```

---

## 🚀 API Endpoints

### `GET /`
Home endpoint — returns a welcome message.

**Response:**
```json
{ "message": "Insurance Premium" }
```

---

### `GET /health`
Health check endpoint — used by platforms like **Kubernetes** and **AWS** to verify the service is live and the ML model is loaded.

**Response:**
```json
{ "status": "OK", "model_loaded": true }
```

---

### `POST /predict`
Main prediction endpoint — accepts user data and returns the predicted insurance premium category.

**Request Body:**

| Field | Type | Description | Example |
|---|---|---|---|
| `bmi` | float | Body Mass Index | `24.5` |
| `age_group` | string | Age group category | `"adult"` |
| `lifestyle_risk` | string | Risk level | `"low"` |
| `city_tier` | int | City tier (1 / 2 / 3) | `1` |
| `income_lpa` | float | Annual income in LPA | `10.5` |
| `occupation` | string | Job type | `"salaried"` |

**Example Request:**
```json
{
  "bmi": 24.5,
  "age_group": "adult",
  "lifestyle_risk": "low",
  "city_tier": 1,
  "income_lpa": 10.5,
  "occupation": "salaried"
}
```

**Success Response `200`:**
```json
{ "predicted_category": "Gold" }
```

**Error Response `500`:**
```json
{ "detail": "Internal server error message" }
```

---

## 🐳 Run with Docker

### Pull from Docker Hub
```bash
docker pull shaktisinh1557/insurance-prediction-api:tagname
```

### Run the Container
```bash
docker run -d -p 8000:8000 shaktisinh1557/insurance-prediction-api:tagname
```

Once running, open your browser and visit:

- 🏠 Home: http://localhost:8000/
- ❤️ Health Check: http://localhost:8000/health
- 📄 Swagger Docs: http://localhost:8000/docs
- 📘 ReDoc: http://localhost:8000/redoc

---

## 💻 Run Locally (Without Docker)

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/insurance-premium-api.git
cd insurance-premium-api
```

### 2. Create a Virtual Environment
```bash
python -m venv myenv

# Windows
myenv\Scripts\activate

# Mac/Linux
source myenv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Application
```bash
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```

---

## ✅ Input Validation

This project uses **Pydantic v2** for strict input validation. Key features:

- City names are **automatically normalized** — e.g. `"mumbai"` → `"Mumbai"` using a custom `@field_validator`
- All fields are **type-checked** before reaching the ML model
- Invalid inputs return descriptive **422 Unprocessable Entity** errors automatically

---

## 🔧 Build & Push Docker Image (For Contributors)

```bash
# Build the image
docker build -t shaktisinh1557/insurance-prediction-api .

# Push to Docker Hub
docker push shaktisinh1557/insurance-prediction-api:tagname
```

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 👤 Author

**Shaktisinh**  
🐳 Docker Hub: [shaktisinh1557](https://hub.docker.com/u/shaktisinh1557)  
🐙 GitHub: [YOUR_GITHUB_LINK]
