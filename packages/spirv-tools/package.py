from spack import *

class SpirvTools(CMakePackage):
    """The SPIR-V Tools project provides an API and commands for processing SPIR-V modules."""

    homepage = "https://github.com/KhronosGroup/SPIRV-Tools"
    url      = "https://github.com/KhronosGroup/SPIRV-Tools/archive/refs/tags/v2022.1.tar.gz"

    maintainers = ['salotz',]

    version('2022.1', sha256='844c0f590a0ab9237cec947e27cfc75bd14f39a68fc3b37d8f1b9e1b21490a58')
    version('2021.4', sha256='d68de260708dda785d109ff1ceeecde2d2ab71142fa5bf59061bb9f47dd3bb2c')
    version('2021.3', sha256='b6b4194121ee8084c62b20f8d574c32f766e4e9237dfe60b0658b316d19c6b13')
    version('2020.4', sha256='d6377d2febe831eb78e84593a10d242a4fd52cb12174133151cb48801abdc6d2')
    version('2019.2', sha256='1fde9d2a0df920a401441cd77253fc7b3b9ab0578eabda8caaaceaa6c7638440')

    # TODO:
    # depends_on('spirv-headers')

    # NOTE: optional
    # depends_on('effcee', type='test')
    # depends_on('googletest', type='test')

    def cmake_args(self):
        args = [
            # # TODO
            # "-DSPIRV_BUILD_FUZZER=OFF",
            # # TODO
            # "-DSPIRV_COLOR_TERMINAL=ON",
            # # TODO
            # "-DSPIRV_SKIP_TESTS=ON",
            # # TODO
            # "-DSPIRV_SKIP_EXECUTABLES=OFF",
            # # "-DSPIRV_USE_SANITIZER=",
            # "-DSPIRV_WARN_EVERYTHING=OFF",
            # "-DSPIRV_WERROR=ON",
        ]
        return args
