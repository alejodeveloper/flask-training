build-docker-dev:
	cp -a flask-app/ docker/dev/flask-app
	cd docker/dev/ && docker build --no-cache -t "flask-app/dev" .
	rm -rf docker/dev/flask-app

start-dev:
	cd docker/dev/ && docker-compose up -d

stop-dev:
	cd docker/dev/ && docker-compose stop
