from spack import *

from pathlib import Path

class SpirvTools(CMakePackage):
    """The SPIR-V Tools project provides an API and commands for
    processing SPIR-V modules."""

    homepage = "https://github.com/KhronosGroup/SPIRV-Tools"
    url      = "https://github.com/KhronosGroup/SPIRV-Tools/archive/refs/tags/v2022.1.tar.gz"

    maintainers = ['salotz',]

    version('2022.1', sha256='844c0f590a0ab9237cec947e27cfc75bd14f39a68fc3b37d8f1b9e1b21490a58')
    version('2021.4', sha256='d68de260708dda785d109ff1ceeecde2d2ab71142fa5bf59061bb9f47dd3bb2c')
    version('2021.3', sha256='b6b4194121ee8084c62b20f8d574c32f766e4e9237dfe60b0658b316d19c6b13')
    version('2020.4', sha256='d6377d2febe831eb78e84593a10d242a4fd52cb12174133151cb48801abdc6d2')
    version('2019.2', sha256='1fde9d2a0df920a401441cd77253fc7b3b9ab0578eabda8caaaceaa6c7638440')

    depends_on('spirv-headers')

    def cmake(self, spec, prefix):

        # we first have to link in the spirv-headers appropriately

        prefix_path = Path(prefix)

        headers_prefix = Path(spec['spirv-headers'].prefix)

        # the full "repo" release is kept in this share folder
        src_path = headers_prefix / "share" / "repo"

        # needs to be linked here for proper compilation of spirv-tools
        dest_path = Path(".") / "external" / "spirv-headers"

        dest_path.symlink_to(src_path)

        # then run the normal CMake project generation
        super().cmake(spec, prefix)
