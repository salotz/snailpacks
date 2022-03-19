# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Libtcod(CMakePackage):
    """libtcod is a free, fast, portable and uncomplicated API for
    roguelike developers providing a true color console, pathfinding,
    field-of-view, and a few other utilities frequently used in
    roguelikes.
    """

    homepage = "https://github.com/libtcod/libtcod"
    url      = "https://github.com/libtcod/libtcod/archive/refs/tags/1.20.1.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    maintainers = ['@salotz',]

    version('1.20.1', sha256='e36dccd1ad531503d1ceefe794a57b3b661e5e669c3d1db1d5bfaf0b95c933df')
    version('1.19.0', sha256='37c9dff5eb61be1aa4dc08f6c7fe910385e12244c14c6b163e2ffab373d779d7')

    depends_on('sdl2')

    # def cmake_args(self):
    #     args = []
    #     return args
