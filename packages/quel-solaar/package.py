from spack import *

class QuelSolaar(Package):
    """Quel Solaar game pipeline."""

    homepage = "http://gamepipeline.org/index.html"

    # note that this is a fork to save versions in
    git = "https://gitlab.com/salotz/quel-solaar.git"

    # this is the official zip and who knows how it gets updated
    url = "http://www.quelsolaar.com/quel_solaar.zip"

    maintainers = ['salotz',]

    version('2022-08-10',
            revision='ceb03772837e4ac9dd6f84fb34382cfd9e5a91f2',)
