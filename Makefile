.PHONY: all

test: image
	@docker run -it --rm golismero-dev:0.1 pytest --ignore=featured_plugins

image:
	@docker build . -t golismero-dev:0.1

prune:
	@docker rmi -f golismero-dev:0.1
	@docker system prune -f