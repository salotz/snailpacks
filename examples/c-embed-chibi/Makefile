init: .spack-env
.PHONY:

configure:
	rm -rf build
	genie ninja
.PHONY: configure

build:
	(cd build/debug && ninja)
.PHONY: build

run:
	./build/bin/demo
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
