.PHONY: all

PLUGIN=`basename $(realpath .)`
VERSION=`cat VERSION`

test: image
	@cat input.json | docker run -i golismero-plugin-${PLUGIN}

debug: image
	@docker run -it --entrypoint /bin/sh golismero-plugin-${PLUGIN}

image:
	@docker build . -t golismero-plugin-${PLUGIN}
	@docker build . -t golismero-plugin-${PLUGIN}:${VERSION}

prune:
	@docker rmi -f golismero-plugin-${PLUGIN}:${VERSION}
	@docker system prune -f