
from spack import *

import os

class Scopes(Package):
    """Scopes programming language."""

    homepage = "http://scopes.rocks"
    hg = "https://hg.sr.ht/~duangle/scopes"

    maintainers = ['salotz']

    version('tip', revision='tip')

    extendable = True

    depends_on('genie', type='build')

    # we need this version of LLVM and to explicitly build for all
    # targets
    depends_on('llvm@12.0.1 +all_targets')
    # TODO: need the headers for this
    # depends_on('spirv-tools')
    depends_on('spirv-cross')

    def install(self, spec, prefix):

        # TODO: link the llvm folder to the location expected by scopes
        # os.symlink()

        # run the genie project generator
        genie = which('genie')

        genie('gmake')

        make("-C", "build")
