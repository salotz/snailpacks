solution "SnailpacksDemo"
    configurations { "debug", "release" }
    location "build"

project "demo"
    kind "ConsoleApp"
    language "C"
    targetdir "build/bin"

    files {"include/**.h", "src/**.c"}

    includedirs {".spack-env/view/include", ".spack-env/view/include/python3.9"}
    libdirs {".spack-env/view/lib"}

    links {"crypt", "intl", "pthread", "dl", "util", "m", "m", "python3.9"}

    configuration "debug"
        defines {"DEBUG"}
        flags {"Symbols"}
        objdir ("build/debug")

    configuration "release"
        defines {"NDEBUG"}
        flags {"Optimize"}
        objdir ("build/release")

