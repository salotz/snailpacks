from spack import *

class Spitbol(MakefilePackage):
    """Implementation of SNOBOL4."""

    homepage = "https://github.com/spitbol/x64"
    url      = "https://github.com/spitbol/x64/archive/refs/tags/V4.0.tar.gz"

    maintainers = ['salotz',]

    version('4.0',
            sha256='1bc930686611c2ee65a9b078cba5483e533e13bdb42110b20a0bdeb71481e698')

    depends_on('nasm', type='build')

    def edit(self, spec, prefix):
        # FIXME: Edit the Makefile if necessary
        # FIXME: If not needed delete this function
        # makefile = FileFilter('Makefile')
        # makefile.filter('CC = .*', 'CC = cc')
