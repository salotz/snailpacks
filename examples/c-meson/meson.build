project('demo', 'c')

# resolve the math library to use
cc = meson.get_compiler('c')
math_dep = cc.find_library('m', required : false)

executable(
    'demo',
    sources: ['src/main.c', ],

    include_directories: '.spack-env/view/include',

    # objects to link against
    objects: ['.spack-env/view/lib/libchipmunk.a'],
    
    # chimpunk2d needs threads and this is the portable way to enable them
    dependencies: [
                  math_dep,
                  dependency('threads')
                  ]
    
    )