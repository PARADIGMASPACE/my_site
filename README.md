# My Site — Personal Portfolio

A minimal, production-ready personal portfolio combining a FastAPI backend with an Nginx-served static frontend. The project is containerized with Docker and orchestrated via docker-compose to simplify local development and deployment.

## Key features
- FastAPI backend for lightweight API endpoints.
- Nginx serves the static frontend and proxies /api/ requests to the backend.
- Docker and docker-compose for repeatable builds and deployment.
- Built-in HTTPS support (ssl/ folder contains certificates) and security headers.
- Simple structure intended for easy customization and CI/CD integration.

## Repository layout
- backend/ — FastAPI application, Python dependencies and Dockerfile.
- frontend/ — static site (HTML/CSS, images and CV in static/).
- nginx/ — Nginx configuration and Dockerfile.
- ssl/ — SSL certificate and key (replace with valid certs for production).
- docker-compose.yml — service orchestration.

## Quick start
1. Clone the repository.
2. (Optional) Edit backend/.env based on backend/.env.example.
3. Build and start all services:
   ```bash
   make up
   ```
   or
   ```bash
   docker-compose up --build
   ```
4. Open https://localhost/ (or your server name). HTTP (port 80) redirects to HTTPS.

## Development
- Run backend locally with uvicorn:
  ```bash
  cd backend && poetry run uvicorn app.main:app --reload
  ```

## Testing
- Tests are located in tests/.
  ```bash
  cd backend && pytest -v
  ```
  or
  ```bash
  make test
  ```

## Notes
- Replace ssl/cert.pem and ssl/key.pem with valid certificates in production and configure DNS for your domain in nginx/nginx.conf.
