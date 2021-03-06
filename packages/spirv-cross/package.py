from spack import *

from pathlib import Path
import shutil as sh

class SpirvCross(CMakePackage):
    """SPIRV-Cross is a practical tool and library for performing
    reflection on SPIR-V and disassembling SPIR-V back to high level
    languages.
    """

    homepage = "https://github.com/KhronosGroup/SPIRV-Cross"
    url      = "https://github.com/KhronosGroup/SPIRV-Cross/archive/refs/tags/sdk-1.3.204.1.tar.gz"

    maintainers = ['salotz',]

    version('1.3.204.1', sha256='8608082a59ec91bd3d8ec69180feca3faa96af92517eb25dd8716210607a7633')

    def install(self, spec, prefix):

        # do the normal CMake install
        super().install(spec, prefix)

        # then make a copy of the repo into share because
        # unfortunately many of the dependents require this
        prefix_path = Path(prefix)

        # copy this whole repo into share in case you have a
        # dependency which needs it done this way
        sh.copytree(
            ".",
            prefix_path / "share" / "repo",
        )

