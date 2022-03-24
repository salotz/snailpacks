let spack-path = "/.spack-env/view"

'bind-symbols __env

    module-search-path =
        cons
            .. module-dir spack-path "/lib/scopes/packages/?.sc"
            .. module-dir spack-path "/lib/scopes/packages/?/init.sc"
            __env.module-search-path

    include-search-path =
        cons
            .. module-dir spack-path "/include"
            __env.include-search-path

    library-search-path =
        cons
            .. module-dir spack-path "/lib"
            __env.library-search-path
