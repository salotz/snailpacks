from spack.package import *

from pathlib import Path
import shutil as sh


class WgpuNative(Package):
    """This is a native WebGPU implementation in Rust, based on
    wgpu-core.

    The bindings are based on the WebGPU-native header found at
    ffi/webgpu-headers/webgpu.h and wgpu-native specific items in
    ffi/wgpu.h

    """

    homepage = "https://github.com/gfx-rs/wgpu-native"
    url = "https://github.com/gfx-rs/wgpu-native/archive/refs/tags/v0.12.0.1.tar.gz"

    version('0.12.0.1',
            sha256='b555b1d27216b53e205310849cbf32ffdf796c465443d17efce7051fa9b052c0',)
    # version('0.11.0.1',
    #         sha256='9abb7b4381eb61ae49d96d6f8078cbdf307e3155a7e56dc7d61a8d344f0777e0')
    # version('0.10.4.1',
    #         sha256='0c700bdf97f30b561b6eaf303b7c13ca1ecb82b63a1fc26fd169d5d53d0a7508')


    depends_on("rust")

    depends_on('webgpu-headers@2022-03-22',
               when='@0.12.0.1',
               )

    # TODO: the rest of the older versions, don't really care to do
    # them all now

    variant('build_type',
            default='debug',
            description='Type of build to generate, passed to "config={value}"',
            values=('release', 'debug',),
            multi=False,
            )

    def install(self, spec, prefix):

        # install the header files for webgpu
        prefix_path = Path(prefix)

        (prefix_path / 'lib').mkdir()
        (prefix_path / 'include').mkdir()


        webgpu_headers_prefix = Path(spec['webgpu-headers'].prefix)

        src_path = webgpu_headers_prefix / "include" / "webgpu.h"

        dest_path = Path('.') / "ffi" / "webgpu-headers" / "webgpu.h"

        dest_path.symlink_to(src_path)

        # build the package
        cargo = which("cargo")

        build_type = spec.variants['build_type'].value

        if build_type == 'release':
            target_name = build_type
            cargo('build' '-r')

        elif build_type == 'debug':
            target_name = build_type
            cargo('build')
        else:
            raise ValueError(f"Unknown build_type {build_type}")

        # then copy the binaries
        build_path = Path('.') / 'target' / target_name

        for path in build_path.glob('*.a'):
            sh.copyfile(path, prefix_path / 'lib' / path.name)

        for path in build_path.glob('*.so'):
            sh.copyfile(path, prefix_path / 'lib' / path.name)

        # NOTE: not sure we want the rust libs so I'll leave out

        # for path in build_path.glob('lib*.rlib'):
        #     sh.copyfile(path, prefix_path / 'lib' / path.name)

        ## Install the headers

        # put the wgpu.h into the installed include
        sh.copyfile(Path('.') / 'ffi' / 'wgpu.h',
                    prefix_path / 'include' / 'wgpu.h'
                    )

        (prefix_path / 'include' / 'webgpu-headers').mkdir()
        sh.copyfile(Path('.') / 'ffi' / 'webgpu-headers' / 'webgpu.h',
                    prefix_path / 'include' / 'webgpu-headers' / 'webgpu.h'
                    )
