from spack import *

from pathlib import Path
import shutil as sh

class WebgpuHeaders(Package):
    """Header fles for the WebGPU API."""

    maintainers = ['salotz',]

    homepage = "https://github.com/webgpu-native/webgpu-headers"

    git = "https://github.com/webgpu-native/webgpu-headers.git"

    # There are no versions of this and the packages that use them
    # just use the hash as the version so we just use the date it was
    # published

    version(
        '2022-03-22',
        commit='b46ca3c39249c537b2b421a37cf06b0d20bbf2c1',
    )

    def install(self, spec, prefix):

        # then make a copy of the repo into share because
        # unfortunately many of the dependents require this
        prefix_path = Path(prefix)

        (prefix_path / 'include').mkdir()
        (prefix_path / 'share').mkdir()

        # copy this whole repo into share in case you have a
        # dependency which needs it done this way
        sh.copyfile(
            "./webgpu.h",
            prefix_path / "include" / "webgpu.h"
        )

        sh.copytree(
            ".",
            prefix_path / "share" / "repo"
        )
