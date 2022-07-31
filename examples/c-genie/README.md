

# Using the Genie build system

Simple example of using snailpacks and Spack for writing code using
some libraries installed via Spack.

```sh
# install dependencies via spack into local view
make init

# generate project files
make configure

# run the build
make build

# run the executable
make run
```
