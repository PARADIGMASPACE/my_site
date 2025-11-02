run:
	poetry run uvicorn app.main:app --reload

lint:
	poetry run ruff check .

format:
	poetry run ruff format .
up:
	docker-compose up --build

down:
	docker-compose down -v

test:
	poetry run pytest -v

