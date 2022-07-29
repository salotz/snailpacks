workspace "SnailpacksDemo"
configurations { "debug", "release" }
location "build"

project "demo"
    kind "ConsoleApp"
    language "C"
    targetdir "build/bin/%{cfg.buildcfg}"

    files {"include/**.h", "src/**.c"}


    includedirs {".spack-env/view/include"}
    libdirs { ".spack-env/view/lib" }

    links { "chipmunk", "m", "pthread"}

    filter "configurations:debug"
        defines { "DEBUG" }
        symbols "On"

    filter "configurations:release"
        defines { "NDEBUG" }
        optimize "On"

