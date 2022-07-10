from spack import *

import shutil
import os


class Majoreo(Package):
    """Project Oriented Package Management"""

    homepage = "http://majoreo.rocks"
    url = "https://hg.sr.ht/~duangle/majoreo/archive/0.12.tar.gz"

    hg = "https://hg.sr.ht/~duangle/majoreo"

    maintainers = ['salotz']

    version('0.12', sha256='b4b467a89c112f012b22329993e16d64085e0c21f43c3a126acd8319af9992d6')

    # archives
    variant('tar', default=True, description="Add tar support")
    variant('unzip', default=True, description="Add unzip support")


    # VCSs
    variant('hg', default=True, description="Add Mercurial support")
    variant('git', default=True, description="Add Git support")
    variant('svn', default=False, description="Add Subversion support")

    depends_on('python@3.8:')

    depends_on('mercurial', when='+hg')
    depends_on('git', when='+git')
    depends_on('subversion', when='+svn')

    depends_on('tar', when='+tar')
    depends_on('unzip', when='+unzip')

    def install(self, spec, prefix):

        os.makedirs(f"{prefix}/bin")

        shutil.copy(
            f'eo',
            f"{prefix}/bin/eo",
        )

