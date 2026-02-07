# Portfolio Website - Full-Stack Application

Modern portfolio website built with **React** frontend and **FastAPI** backend.

## 🚀 Tech Stack

### Frontend
- **React 18** with TypeScript
- **CSS3** with modern animations
- **Font Awesome** icons
- **Responsive design**

### Backend
- **FastAPI** (Python)
- **Uvicorn** ASGI server
- **RESTful API architecture**
- **Auto-generated API documentation**

## 📁 Project Structure

```
portfolio-website/
├── frontend/                # React application
│   ├── src/
│   │   ├── components/     # React components
│   │   ├── services/       # API service layer
│   │   ├── App.tsx         # Main app component
│   │   └── index.tsx       # Entry point
│   ├── public/             # Static assets
│   └── package.json
│
├── backend/                 # FastAPI application
│   ├── app/
│   │   ├── main.py         # FastAPI app
│   │   ├── api/            # API routes
│   │   ├── models/         # Data models
│   │   └── schemas/        # Pydantic schemas
│   └── requirements.txt
│
├── index.html              # Original static version (backup)
├── styles-enhanced.css     # Original styles (reference)
└── README.md
```

## 🛠️ Development Setup

### Prerequisites
- Node.js 16+ and npm
- Python 3.8+
- pip and venv

### Backend Setup

```bash
# Navigate to backend
cd backend

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run development server
uvicorn app.main:app --reload --port 8000
```

Backend will run at: http://localhost:8000
API Docs: http://localhost:8000/docs

### Frontend Setup

```bash
# Navigate to frontend
cd frontend

# Install dependencies
npm install

# Run development server
npm start
```

Frontend will run at: http://localhost:3000

## 🌐 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | API information |
| `/api/about` | GET | Personal information & stats |
| `/api/projects` | GET | All projects |
| `/api/projects/{id}` | GET | Specific project |
| `/api/experience` | GET | Work experience |
| `/api/skills` | GET | Skills & competencies |

## 🎨 Features

- ✅ **Modern UI** with smooth animations
- ✅ **Dark mode** toggle
- ✅ **Responsive design** for all devices
- ✅ **RESTful API** with FastAPI
- ✅ **Type-safe** with TypeScript
- ✅ **Component-based** architecture
- ✅ **API documentation** (Swagger/ReDoc)

## 📦 Production Build

### Frontend
```bash
cd frontend
npm run build
# Creates optimized production build in frontend/build/
```

### Backend
```bash
# Use production ASGI server
uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4
```

## 🚢 Deployment Options

### Frontend
- **Netlify** / **Vercel** (Recommended for React)
- **GitHub Pages** (static build)
- **AWS S3** + CloudFront

### Backend
- **Railway** / **Render** (Recommended for FastAPI)
- **AWS EC2** / **Lambda**
- **Docker** container deployment

## 🔧 Environment Variables

### Frontend (.env)
```
REACT_APP_API_URL=http://localhost:8000
```

### Backend (.env)
```
CORS_ORIGINS=http://localhost:3000,https://yourdomain.com
DEBUG=True
```

## 📝 License

This is a personal portfolio project by Lilavati Mhaske.

## 👤 Author

**Lilavati Mhaske**
- Location: Leicester, United Kingdom
- Email: mhaskelilavati4545@gmail.com
- LinkedIn: [linkedin.com/in/lilavati-mhaske](https://www.linkedin.com/in/lilavati-mhaske/)
- GitHub: [github.com/Lilavati25](https://github.com/Lilavati25)
