
from spack import *

class Scopes(Package):
    """Scopes programming language."""

    homepage = "http://scopes.rocks"
    hg = "https://hg.sr.ht/~duangle/scopes"

    maintainers = ['salotz']

    version('tip', revision='tip')

    extendable = True

    # TODO
    # depends('llvm')
    # depends('spirv-tools')
    # depends('spirv-headers')

    # depends('googletest', type=('build'))
    # depends('effcee', type=('build'))
    # depends('re2', type=('build'))

    def install(self, spec, prefix):
        pass
