.PHONY: build

build:
	cd page; hugo \
		--cleanDestinationDir \
		--environment manual \
		--destination ../build/manual \
		--logLevel info \
		--baseURL https://docs.isotopeecommerce.org/manual/

# Start a live reload server
live:
	cd page; hugo server \
		--cleanDestinationDir \
		--environment manual \
		--destination ../build/manual \
		--logLevel info

clean:
	rm -r build
