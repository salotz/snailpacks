let spack-path = "/.spack-env/view"

'bind-symbols __env

    module-search-path =
        cons
            # the current module in development
            .. module-dir "/demo/?.sc"
            .. module-dir "/demo/?/init.sc"
            # spack installed packages
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
