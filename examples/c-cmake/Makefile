init: .spack-env
	mkdir -p build
.PHONY:

configure:
	rm -rf build
	mkdir -p build
	cmake -B build
.PHONY: configure

build:
	cmake --build build
.PHONY: build

run:
	./build/demo
.PHONY: run

env: .spack-env
.PHONY: env

.spack-env: spack.yaml
	spack env create -d .
	spack -e . install --reuse
	echo "activate with: spacktivate ."

clean:
	rm -rf .spack-env
	rm -f spack.lock
	rm -rf build
.PHONY: clean
