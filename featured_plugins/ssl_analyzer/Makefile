.PHONY: all

PLUGIN=`basename $(realpath .)`
VERSION=`cat VERSION`

test: image
	@docker run -it --rm --entrypoint pytest golismero-plugin-${PLUGIN}:${VERSION}

image:
	@docker build . -t golismero-plugin-${PLUGIN}:${VERSION}

prune:
	@docker rmi -f golismero-plugin-${PLUGIN}:${VERSION}
	@docker system prune -f