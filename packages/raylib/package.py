from pathlib import Path

from spack import *


class Raylib(CMakePackage):
    """A simple and easy-to-use library to enjoy videogames programming."""

    homepage = "https://www.raylib.com/"
    url      = "https://github.com/raysan5/raylib/archive/refs/tags/4.0.0.tar.gz"

    maintainers = ['salotz',]

    version('4.0.0',
            sha256='11f6087dc7bedf9efb3f69c0c872f637e421d914e5ecea99bbe7781f173dc38c')
    version('3.7.0',
            sha256='439dc1851dd1b7f385f4caf4f5c7191dda90add9d8d531e5e74702315e432003')
    version('3.5.0',
            sha256='e93a883071b9a027d6aa4174aebd5fd17afe16b67236712d6c17c1a9ecff7863')
    version('3.0.0',
            sha256='be17b6b39bb0e742c0df1e683b49853981854aefa25a758ddcf40f71da8b8436')
    version('2.6.0',
            sha256='ffcdd9e2a138340edf621de826ff8371ab73cede0738ae2b38b349408e0a1b6e')
    version('2.5.0',
            sha256='e9ebdf70ad4912dc9f3c7965dc702d5c61f2841aeae521e8dd3b0a96a9d82d58')
    version('2.0.0',
            sha256='b27fdfc8f44dab230d56a06c5674b3a340139ef18bbd4264c660787cf18b3ede')

    variant("platform",
            default='Desktop',
            description="Platform to build for.",
            values=('Desktop', 'Web', 'Android', 'Raspberry Pi'),
            multi=False,
            )

    # we set this to ON for spack since we can control dependencies
    variant("external_glfw",
            default=True,
            description="Link raylib against system GLFW instead of embedded one",
            )

    variant("opengl_version",
            default='OFF',
            description="Force a specific OpenGL Version",
            values=('OFF',
                    '3.3',
                    '2.1',
                    '1.1',
                    'ES 2.0',
                    ),
            multi=False,
            )

    variant("shared", default=True, description="Build shared libraries")

    # TODO: there are lots of variants for raylib that we could add.
    # variant("audio", default=True, description="Build with audio support")

    depends_on('libxrandr', when='platform=linux')
    depends_on('libxi', when='platform=linux')
    depends_on('libx11', when='platform=linux')
    # depends_on('xorg-server', when='platform=linux')
    depends_on('mesa -llvm', when='platform=linux')
    depends_on('mesa-glu', when='platform=linux')
    depends_on('alsa-lib', when='platform=linux')

    # if we are building against external GLFW
    depends_on('glfw',
               when='+external_glfw')

    # only install a few fonts in the GLFW dependency
    depends_on('font-util fonts=encodings,font-alias',
               when='+external_glfw')

    def cmake_args(self):

        options = [
            self.define_from_variant('PLATFORM', 'platform'),
            self.define_from_variant('USE_EXTERNAL_GLFW', 'external_glfw'),
            self.define_from_variant('OPENGL_VERSION', 'opengl_version'),
            self.define_from_variant('BUILD_SHARED_LIBS', 'shared'),
        ]

        return options

    def install(self, spec, prefix):

        # run the normal install
        super().install(spec, prefix)

        # then symlink the lib64 directory if it exists (some compiler
        # versions do this I guess)
        prefix_path = Path(prefix)

        if (prefix_path / 'lib64').exists() and not (prefix_path / 'lib').exists():
            (prefix_path / 'lib').symlink_to(prefix_path / 'lib64')
