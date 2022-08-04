init: .spack-env
.PHONY:

configure:
	rm -rf build
	genie gmake
.PHONY: configure

build:
	(cd build && make)
.PHONY: build

run:
	(cd src && ../bin/triangle_x64_d)
.PHONY: run

env: .spack-env
.PHONY: env

.spack-env: spack.yaml
	spack env create -d .
	spack -e . install --reuse
	echo "activate with: spacktivate ."

clean:
	rm -rf bin build
.PHONY: clean

clean-all: clean
	rm -rf .spack-env
	rm -f spack.lock
.PHONY: clean
