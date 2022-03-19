from spack import *

import shutil
import os


class Genie(Package):
    """GENie (pronounced as Jenny) is project generator tool. It
    automagically generates project from Lua script, making applying the
    same settings for multiple projects easy."""

    homepage = "https://github.com/bkaradzic/GENie"

    git = "https://github.com/bkaradzic/GENie.git"

    maintainers = ['salotz']

    # GENie is a little weird they provide self contained precompiled
    # binaries in another repository just versioned with git. Not very
    # normal.. But the versions of the source are just monotonically
    # increasing numbers associated with a hash.
    version('1160',
            commit='f9bd455a8439dbcb807816c0be9e4aedf5991bc3',
            )


    def install(self, spec, prefix):

        make()

        # the build will make a folder for the platform we are
        # building on, lets just automatically get whatever that is
        # rather than introspecting on the platform and mapping that
        # to what genie means by them
        platform_dirs = os.listdir("bin")
        assert len(platform_dirs) == 1, "More than one platform had a binary generated"

        platform = platform_dirs[0]

        shutil.copytree(
            f'bin/{platform}',
            f"{prefix}/bin",
        )
