# Django-React AWS Template

A production-ready template for building web applications with Django backend, React frontend, and automated AWS deployment through GitHub Actions.

## 🚀 Features

- **Backend**: Django REST Framework with PostgreSQL
- **Frontend**: React (Preact) with Vite and TailwindCSS
- **Infrastructure**: 
  - AWS EC2 for backend hosting
  - AWS S3 for static files and media storage
  - AWS RDS for PostgreSQL database
  - AWS ECR for Docker container registry
- **CI/CD**: Automated GitHub Actions workflows
- **Security**: Automatic SSL/TLS with Let's Encrypt
- **Development**: Docker Compose for local development

## 🛠️ Prerequisites

- AWS Account with configured IAM user
- Domain name (for SSL setup)
- Docker and Docker Compose
- Python 3.11+
- Node.js 18+

## 🔧 Local Development

1. Clone the repository:

```bash
git clone <repository-url>
cd <project-name>
```

2. Set up environment variables:

```bash
# Backend (.env)
SECRET_KEY=your-secret-key
DEBUG=True
DOMAIN=localhost
DB_NAME=postgres
DB_USER=postgres
DB_PWD=postgres
DB_HOST=db
DB_PORT=5432
USE_S3=False

# Frontend (.env)
VITE_API_URL=http://localhost:8000
```

3. Start development servers:

```bash
docker-compose up
```

## 📦 Deployment

1. Configure GitHub Secrets:

```
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
AWS_REGION
ECR_REPOSITORY
DOMAIN
DB_NAME
DB_USER
DB_PWD
DB_HOST
DB_PORT
SECRET_KEY
EMAIL_ADDRESS (for SSL)
EC2_HOST
EC2_USERNAME
EC2_SSH_KEY
S3_BUCKET
```

2. Push to main branch to trigger deployment:

```bash
git push origin main
```

## 🏗️ Project Structure

```
.
├── be/                 # Django Backend
│   ├── api/           # REST API
│   ├── accounts/      # User management
│   └── core/          # Core functionality
├── fe/                # React Frontend
│   ├── src/           # Source code
│   └── public/        # Static files
└── .github/           # GitHub Actions
    └── workflows/     # CI/CD pipelines
```

## 📝 License

MIT

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.