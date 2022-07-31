

# Embedding Python to a C Program

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

You can see the link flags with:

```sh
spacktivate .
python3.9-config --ldflags
```
