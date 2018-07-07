.PHONY: all

VERSION=`cat VERSION`

test: image
	@docker run -it --rm --entrypoint pytest golismero-plugin-dns-resolver:${VERSION}

image:
	@docker build . -t golismero-plugin-dns-resolver:${VERSION}

prune:
	@docker rmi -f golismero-plugin-dns-resolver:${VERSION}
	@docker system prune -f