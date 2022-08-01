from spack import *

class Chibi(MakefilePackage):
    """Minimal Scheme Implementation for use as an Extension Language

    Chibi-Scheme is a very small library intended for use as an
    extension and scripting language in C programs. In addition to
    support for lightweight VM-based threads, each VM itself runs in
    an isolated heap allowing multiple VMs to run simultaneously in
    different OS threads.

    """

    homepage = "http://synthcode.com/wiki/chibi-scheme"
    url = "https://github.com/ashinn/chibi-scheme/archive/refs/tags/0.10.tar.gz"

    version('0.10',
            sha256='ae1d2057138b7f438f01bfb1e072799105faeea1de0ab3cc10860adf373993b3')
    version('0.9.1',
            sha256='a9ee2afd7671418bc09a4d386448dbfd0662421ea1eb1c5ed3b68c071307854d')
    version('0.9',
            sha256='c61edd9b1891a3248bcd22002a938ccac06d05dbdd879ec34e90fef24451422a')
    version('0.8',
            sha256='8a077859b123216c123c243db391b0fe4c0cf73978c7cdd7b8ea853a48192756')
    version('0.7.3',
            sha256='821ce808573ca4eadfeb84bfd18d4ef839dde24ba882eb232207e48f89bb979b')

    variant('doc', default=False, description="Build documentation")

    depends_on('gmake', type='build')

    def edit(self, spec, prefix):
        env['PREFIX'] = prefix


