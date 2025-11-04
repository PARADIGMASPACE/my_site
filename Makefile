BACKEND_DIR=backend

run:
	cd $(BACKEND_DIR) && poetry run uvicorn app.main:app --reload

lint:
	cd $(BACKEND_DIR) && poetry run ruff check .

format:
	cd $(BACKEND_DIR) && poetry run ruff format .

up:
	docker-compose up --build

down:
	docker-compose down -v

test:
	cd $(BACKEND_DIR) && poetry run pytest -v

requirements:
	cd $(BACKEND_DIR) && poetry export -f requirements.txt --output requirements.txt --without-hashes
