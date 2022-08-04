solution "WgpuNativeTriangleExample"
    configurations { "debug", "release" }
    location "build"
    platforms {"x64"}
    startproject "TriangleExample"
    targetdir "bin"
    debugdir "bin"

    configuration {"x64", "debug"}
        targetsuffix "_x64_debug"

    configuration {"x64", "release"}
        targetsuffix "_x64"

    configuration "debug"
        defines { "DEBUG" }
        flags { "Symbols" }
        objdir "build/debug"

    configuration "release"
        defines { "NDEBUG"}
        flags { "Optimize" }
        objdir "build/release"

    configuration {"gmake"}
        buildoptions {
           "-Wall",
           "-Wextra",
           "-pedantic"
        }

    configuration {"linux"}
        defines {"WGPU_TARGET=WGPU_TARGET_LINUX_X11"}


project "TriangleExample"
    kind "ConsoleApp"
    language "C"
    targetdir "bin"
    targetname "triangle"

    files {"src/**.c"}


    includedirs {"include", ".spack-env/view/include"}
    libdirs { ".spack-env/view/lib" }

    links { "wgpu_native", "glfw" }

