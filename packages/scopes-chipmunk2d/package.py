from spack import *

import shutil


class ScopesChipmunk2d(Package):
    """Scopes language wrapper for Chipmunk2D"""

    homepage = "https://github.com/salotz/scopes-chipmunk2d"
    url = "https://github.com/salotz/scopes-chipmunk2d/archive/refs/tags/v0.1.tar.gz"
    git = "https://github.com/salotz/scopes-chipmunk2d"

    maintainers = ['salotz']

    version('0.2', sha256='c4a65d8a99e78be6b6ab66893eec98b95456666796b31cd4fce142c402768fc0')
    # broken
    # version('0.1', sha256='6e7a7d0288df8821c23672e703baa75dd1908461f3de97757e73d64e7fffc4b6')

    extends('scopes')

    depends_on('chipmunk2d')

    @property
    def scopes_package_name(self):
        return '-'.join(self._name.split('-')[1:])

    def install(self, spec, prefix):

        shutil.copytree(
            f'src/{self.scopes_package_name}',
            f"{prefix}/lib/scopes/packages/{self.scopes_package_name}",
        )
