clean:
	rm -rf README.html certifi_debian.egg-info/ build/ dist/

build:
	python setup.py sdist bdist_wheel

publish: build
	twine upload --skip-existing --sign dist/*
