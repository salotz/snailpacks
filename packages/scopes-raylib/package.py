from spack import *

import shutil


class ScopesRaylib(Package):
    """Bindings of Raylib for the Scopes programming language."""

    homepage = "https://github.com/salotz/raylib-scopes"
    url      = "https://github.com/salotz/raylib-scopes/archive/refs/tags/v0.1.tar.gz"

    maintainers = ['salotz']

    version('0.4',
            sha256='6508918a07f7f862d743a1acc5eb00d1429a584db03899b731efe40682b7ab14')

    extends('scopes')

    depends_on('raylib')

    @property
    def scopes_package_name(self):
        return '-'.join(self._name.split('-')[1:])

    def install(self, spec, prefix):

        shutil.copytree(
            f'src/{self.scopes_package_name}',
            f"{prefix}/lib/scopes/packages/{self.scopes_package_name}",
        )
