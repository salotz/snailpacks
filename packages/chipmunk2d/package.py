from spack import *


class Chipmunk2d(CMakePackage):
    """A fast and lightweight 2D game physics library."""

    homepage = "http://chipmunk-physics.net/"
    url      = "https://github.com/slembcke/Chipmunk2D/archive/refs/tags/Chipmunk-7.0.3.tar.gz"
    git = "https://github.com/slembcke/Chipmunk2D.git"

    maintainers = ['salotz',]

    version('7.0.3', sha256='1e6f093812d6130e45bdf4cb80280cb3c93d1e1833d8cf989d554d7963b7899a')

    variant("shared", default=True, description="Build shared libraries")
    variant("static", default=False, description="Build as static libraries")

    variant("demos", default=False, description="Whether to build and install the demos")

    depends_on('mesa -llvm', when='+demos')

    def cmake_args(self):
        args = [
            self.define_from_variant('BUILD_DEMOS', 'demos'),
            self.define_from_variant('INSTALL_DEMOS', 'demos'),
            self.define_from_variant('BUILD_SHARED', 'shared'),
            self.define_from_variant('BUILD_STATIC', 'static'),
            self.define_from_variant('INSTALL_STATIC', 'static'),
        ]
        return args
