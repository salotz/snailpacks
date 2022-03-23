let spack-path = "/.spack-env/view"

'define-symbol package 'path
    cons
        .. module-dir spack-path "/lib/scopes/packages/?.sc"
        .. module-dir spack-path "/lib/scopes/packages/?/init.sc"
        package.path

'define-symbol package 'library-path
    cons
        .. module-dir spack-path "/lib"
        package.library-path

'define-symbol package 'include-path
    cons
        .. module-dir spack-path "/include"
        package.include-path
