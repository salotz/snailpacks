from spack import *

import os
from pathlib import Path
import shutil as sh

class Scopes(Package):
    """Scopes programming language."""

    homepage = "http://scopes.rocks"
    hg = "https://hg.sr.ht/~duangle/scopes"
    url = "https://hg.sr.ht/~duangle/scopes/archive/release-0.17.tar.gz"

    maintainers = ['salotz']

    version('tip', revision='tip')

    version('0.18',
            preferred=True,
            sha256='2ed2ac785f2f50b4d4c4b097b28b873d2421319ad35d686b0644f56d42adabf5'
            )

    version('0.17',
            sha256='c1102a70accc6c6678e30175eaac9da1c57febfb40c10fdef926462e058a7b52')

    extendable = True

    variant('build_type',
            default='debug',
            description='Type of build to generate, passed to "config={value}"',
            values=('release', 'debug',),
            multi=False,
            )

    depends_on('genie', type='build')

    depends_on('llvm@13.0.1 targets=all', when='@tip')
    depends_on('llvm@13.0.1 targets=all', when='@0.18')
    depends_on('llvm@12.0.1 targets=all', when='@0.17')

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
        make(
            "-C",
            "build",
            f"config={spec.variants['build_type'].value}",
        )

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

        # the location for these changed so do this differently for different versions
        if spec.satisfies("@0.18:") or spec.satisfies('@tip'):
            sh.copytree(
                clang_bridge_headers,
                Path(".") / "lib" / "scopes/clang/include",
            )

        else:
            sh.copytree(
                clang_bridge_headers,
                Path(".") / "lib" / "clang/include",
            )


        # first move the `libscopesrt.so` file from bin, since it
        # should be in lib, in general
        sh.move(
            Path(".") / "bin" / 'libscopesrt.so',
            Path(".") / "lib" / 'libscopesrt.so',
        )

        # then go ahead and copy all the artifacts over

        # only copy the scopes binary and the runtime library
        os.makedirs(Path(prefix) / "bin")
        sh.copy(
            Path(".") / "bin" / "scopes",
            Path(prefix) / "bin" / "scopes",
        )

        sh.copytree(
            Path(".") / "lib",
            Path(prefix) / "lib",
        )

        sh.copytree(
            Path(".") / "include",
            Path(prefix) / "include",
        )

        # libscopesrt.so is expected to be in the same directory as
        # scopes
        (Path(prefix) / "bin/libscopesrt.so").symlink_to(
            Path(prefix) / "lib/libscopesrt.so"
        )
