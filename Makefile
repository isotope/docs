.PHONY: build

build:
	cd page; hugo \
		--cleanDestinationDir \
		--environment manual \
		--destination ../build/manual \
		--verbose \
		--baseURL https://docs.isotopeecommerce.org/manual/

# Start a live reload server
live:
	cd page; hugo server \
		--cleanDestinationDir \
		--environment manual \
		--destination ../build/manual \
		--verbose

clean:
	rm -r build
