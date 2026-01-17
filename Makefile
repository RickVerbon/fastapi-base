init-db:
	docker compose exec app python -m app.db.init_db

.PHONY: init-db
