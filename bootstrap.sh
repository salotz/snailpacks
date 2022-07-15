#!/bin/sh

# set up spack and snailpacks locally for scopes development


## Install Spack

git clone \
    -c feature.manyFiles=true \
    https://github.com/spack/spack.git \
    ~/spack

echo "To enable Spack put the following into your shell startup, e.g. .profile"

echo ". ~/spack/share/spack/setup-env.sh"

. ~/spack/share/spack/setup-env.sh || exit

# configure mirrors, only relevant if you are using GCC 7.4.0 or 8.2.0

# NOTE: I don't do this by default since unless you use an old distro
# the GCC used to compile things they won't match up and --reuse will
# give you weird compiler versions

# echo "Adding mirrors"
# spack mirror add official-binaries https://binaries.spack.io/releases/v0.18
# spack mirror add E4S https://cache.e4s.io

# spack buildcache keys --install --trust

# bootstrap base pkgs
echo "Bootstrapping base packages"
spack spec zlib

## install snailpacks repo

echo "Installing snailpacks repo"
mkdir -p ~/.spack/repos
git clone git@github.com:salotz/snailpacks.git ~/.spack/repos/snailpacks
spack repo add ~/.spack/repos/snailpacks

## download and setup LLVM external

echo "Downloading prebuilt LLVM"
clang_version='13.0.1'
clang_filename="clang+llvm-${clang_version}-x86_64-linux-gnu-ubuntu-18.04"
clang_url="https://github.com/llvm/llvm-project/releases/download/llvmorg-${clang_version}/${clang_filename}.tar.xz"

mkdir -p $HOME/opt/llvm || exit
cd $HOME/opt/llvm || exit
wget "${clang_url}" || exit
tar -xvf ${clang_filename}.tar.xz || exit
rm ${clang_filename}.tar.xz || exit

cat << EOF >> $HOME/.spack/packages.yaml || exit
  # added by bootstrap.sh
  packages:
    llvm:
      externals:
      - spec: llvm@${clang_version}
        prefix: /opt/llvm/clang+llvm-${clang_version}-x86_64-linux-gnu-ubuntu-
EOF
