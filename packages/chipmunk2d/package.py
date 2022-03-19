
from spack import *


class Chipmunk2d(CMakePackage):
    """A fast and lightweight 2D game physics library."""

    homepage = "http://chipmunk-physics.net/"
    url      = "https://github.com/slembcke/Chipmunk2D/archive/refs/tags/Chipmunk-7.0.3.tar.gz"

    maintainers = ['salotz',]

    version('7.0.3', sha256='1e6f093812d6130e45bdf4cb80280cb3c93d1e1833d8cf989d554d7963b7899a')

    # FIXME: Add dependencies if required.
    # depends_on('foo')

    def cmake_args(self):
        # FIXME: Add arguments other than
        # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        # FIXME: If not needed delete this function
        args = []
        return args
