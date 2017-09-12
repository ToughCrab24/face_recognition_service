DC=docker-compose -f docker/base.yml

build:
	@${DC} build
env:
	${DC} -f docker/dev.yml up -d
logs:
	${DC} -f docker/dev.yml logs -f
stop-env:
	${DC} -f docker/dev.yml stop
destroy-env:
	${DC} -f docker/dev.yml down
migrate:
	${DC} -f docker/dev.yml run web python manage.py migrate
test:
	@docker run --rm -v ${PWD}:/code ${IMAGE} python manage.py test --pattern="test_*.py"  --settings=config.settings.test
web-bash:
	${DC} -f docker/dev.yml exec web bash
db-bash:
	${DC} -f docker/dev.yml exec db bash
restart-web:
	${DC} -f docker/dev.yml restart web
