
from spack import *

import os
from pathlib import Path
import shutil as sh

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

    depends_on('spirv-tools')
    depends_on('spirv-cross')

    def patch(self):

        # change the paths that the build script expects

        # longest match first
        filter_file(
            r'SPIRV-Tools/build/source/opt',
            'SPIRV-Tools/lib',
            'genie.lua',
        )

        filter_file(
            r'SPIRV-Tools/build/source',
            'SPIRV-Tools/lib',
            'genie.lua',
        )

    def install(self, spec, prefix):

        llvm_prefix = Path(spec['llvm'].prefix)
        (Path(".") / "clang").symlink_to(llvm_prefix)

        spirv_cross_prefix = Path(spec['spirv-cross'].prefix)

        (Path(".") / "SPIRV-Cross").symlink_to(spirv_cross_prefix / "share" / "repo")

        spirv_tools_prefix = Path(spec['spirv-tools'].prefix)
        (Path(".") / "SPIRV-Tools").symlink_to(spirv_tools_prefix)

        # run the genie project generator
        genie = which('genie')
        genie('gmake')

        # compile the code
        make("-C", "build")

        # Then we install the clang bridge which is used for bridging
        # to C

        clang_bridge_headers = (
            llvm_prefix /
            "lib/clang" /
            str(spec['llvm'].version) /
            "include"
        )

        # copy them into the build env lib folder. This will get
        # copied to the install prefix in the next section
        sh.copytree(
            clang_bridge_headers,
            Path(".") / "lib" / "clang/include",
        )

        # first move the `libscopesrt.so` file from bin, since it
        # should be in lib
        sh.move(
            Path(".") / "bin" / 'libscopesrt.so',
            Path(".") / "lib" / 'libscopesrt.so',
        )

        # then go ahead and copy all the folders over
        sh.copytree(
            Path(".") / "bin",
            Path(prefix) / "bin",
        )

        sh.copytree(
            Path(".") / "lib",
            Path(prefix) / "lib",
        )

        sh.copytree(
            Path(".") / "include",
            Path(prefix) / "include",
        )
