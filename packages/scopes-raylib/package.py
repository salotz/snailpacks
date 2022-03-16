# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install raylib-scopes
#
# You can edit this file again by typing:
#
#     spack edit raylib-scopes
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *

import shutil


class ScopesRaylib(Package):
    """FIXME: Put a proper description of your package here."""

    homepage = "https://github.com/salotz/raylib-scopes"
    url      = "https://github.com/salotz/raylib-scopes/archive/refs/tags/v0.1.tar.gz"

    maintainers = ['salotz']


    version('0.1', sha256='cdd6f2ffb60357cc37ad6e680bb4cc8e107235c5fdd6fb5c2591f311dd348bfa')

    depends_on('raylib')

    # TODO
    # depends_on('scopes')

    @property
    def scopes_name(self):
        return '-'.join(self._name.split('-')[1:])

    def install(self, spec, prefix):

        shutil.copytree('src', f"{prefix}/scopes/{self.scopes_name}")

        print(prefix)
        which('ls')(prefix)
