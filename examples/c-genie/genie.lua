solution "SnailpacksDemo"
    configurations { "debug", "release" }
    location "build"

project "demo"
    kind "ConsoleApp"
    language "C"
    targetdir "build/bin"

    files {"include/**.h", "src/**.c"}


    includedirs {".spack-env/view/include"}
    libdirs { ".spack-env/view/lib" }

    links { "chipmunk", "m", "pthread"}

    configuration "debug"
        defines { "DEBUG" }
        flags { "Symbols" }
        objdir ("build/debug")

    configuration "release"
        defines { "NDEBUG" }
        flags { "Optimize" }
        objdir ("build/release")

