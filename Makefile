init:
	docker-compose build
	# docker-compose run --entrypoint "poetry init --name demo-app --dependency fastapi --dependency uvicorn[standard]" app
	docker-compose run --entrypoint "poetry install" app
	docker-compose run --entrypoint "poetry add sqlalchemy aiomysql" app

up:
	docker-compose up

dbinit:
	docker-compose exec db mysql masaqitta

down:
	docker-compose down
