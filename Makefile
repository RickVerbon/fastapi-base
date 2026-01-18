init:
	docker compose build
	docker compose up -d
	sleep 2
	make init-db

sync:
	docker compose exec app uv sync

up:
	docker compose up -d --build

init-db:
	docker compose exec app python -m app.db.init_db

test:
	docker compose exec app pytest -v

reset-db:
	docker compose exec app python -m app.db.reset_db
	make init-db

.PHONY: init-db test up init reset-db flake8 qa sync
