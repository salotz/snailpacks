# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Arcan(CMakePackage):
    """Arcan is a powerful development framework for creating virtually
    anything from user interfaces for specialized embedded applications
    all the way to full-blown standalone desktop environments."""

    homepage = "http://arcan-fe.com/"
    git = "https://github.com/letoram/arcan.git"

    maintainers = ["@salotz"]

    version('master',
            branch='master',
            )


    # SNIPPET
    # variant("", default=False, description="")

    root_cmakelists_dir = "src"

    # SNIPPET
    # generator = "Ninja"
    # depends_on('ninja', type='build')

    # build dependencies
    depends_on('cmake@3.1:', type='build')


    # run time dependencies
    depends_on('sqlite')
    depends_on('sdl2')
    depends_on('libdrm')
    # depends_on('opengl')
    depends_on('lua-luajit')
    depends_on('freetype')
    depends_on('harfbuzz')
    depends_on('libxkbcommon')

    depends_on('openal-soft')
    depends_on('ffmpeg')
    depends_on('leptonica')
    depends_on('tesseract')
    depends_on('libusb')

    depends_on('libxcb')
    depends_on('xcb-util')

    # TODO:
    # depends_on('libvlc')
    # depends_on('libvncserver')

    def cmake_args(self):

        spec = self.spec

        options = [
            self.define('BUILD_PRESET', "everything"),

            # SNIPPET
            # option to make it shared or not
            # self.define_from_variant('GLFW_VULKAN_STATIC', 'vulkan_static'),
        ]

        return options
