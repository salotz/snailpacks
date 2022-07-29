from spack import *


class Openmw(CMakePackage):
    """Open source implementation of the Elder Scrolls III: Morrowind
    game engine."""

    homepage = "https://openmw.org/en/"
    url      = "https://github.com/OpenMW/openmw.git"

    maintainers = ['salotz']

    # version('1.2.3', '0123456789abcdef0123456789abcdef')

    depends_on('openscenegraph')
    depends_on('sdl2')
    depends_on('openal-soft')
    depends_on('ffmpeg')
    depends_on('lz4')
    depends_on('sqlite')
    depends_on('luajit')

    # TODO
    depends_on('mygui')
    depends_on('bullet')

    # depends_on('cmake')
