from spack import *

from pathlib import Path
import shutil as sh

class SpirvHeaders(CMakePackage):
    """Machine-readable files for the SPIR-V Registry."""

    homepage = "https://github.com/KhronosGroup/SPIRV-Headers"
    url = "https://github.com/KhronosGroup/SPIRV-Headers/archive/refs/tags/sdk-1.3.204.1.tar.gz"

    maintainers = ['salotz',]

    version('1.3.204.1', sha256='262864053968c217d45b24b89044a7736a32361894743dd6cfe788df258c746c')

    def install(self, spec, prefix):

        # do the normal CMake installation
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
