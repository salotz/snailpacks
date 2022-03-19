
from spack import *

class SpirvCross(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    homepage = "https://github.com/KhronosGroup/SPIRV-Cross"
    url      = "https://github.com/KhronosGroup/SPIRV-Cross/archive/refs/tags/sdk-1.3.204.1.tar.gz"

    maintainers = ['salotz',]

    version('1.3.204.1', sha256='8608082a59ec91bd3d8ec69180feca3faa96af92517eb25dd8716210607a7633')

    # depends_on('foo')

    # def cmake_args(self):
    #     args = []
    #     return args
