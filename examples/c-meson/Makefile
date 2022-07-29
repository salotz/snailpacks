init: .spack-env
	meson setup build
.PHONY:

build:
	meson compile -C build
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
