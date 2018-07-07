.PHONY: all

test: image
	@docker run -it --rm golismero-dev:0.1 pytest

image:
	@docker build . -t golismero-dev:0.1