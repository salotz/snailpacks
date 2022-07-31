cmake_minimum_required(VERSION 3.10)

project('snailpacks-demo')

link_directories(.spack-env/view/lib)

add_executable(demo src/demo.c)

target_link_libraries(demo PUBLIC chipmunk pthread m)

target_include_directories(demo PUBLIC .spack-env/view/include)
