from spack.package import *


class Chapel(AutotoolsPackage):
    """Chapel is a modern programming language that is parallel, productive,
    portable, scalable and open-source."""

    homepage = "https://chapel-lang.org/"
    url = "https://github.com/chapel-lang/chapel/releases/download/1.24.1/chapel-1.24.1.tar.gz"

    version("1.24.1", sha256="f898f266fccaa34d937b38730a361d42efb20753ba43a95e5682816e008ce5e4")
    version("1.24.0", sha256="77c6087f3e0837268470915f2ad260d49cf7ac4adf16f5b44862ae624c1be801")
    version("1.23.0", sha256="7ae2c8f17a7b98ac68378e94a842cf16d4ab0bcfeabc0fee5ab4aaa07b205661")
    version("1.22.1", sha256="8235eb0869c9b04256f2e5ce3ac4f9eff558401582fba0eba05f254449a24989")
    version("1.22.0", sha256="57ba6ee5dfc36efcd66854ecb4307e1c054700ea201eff73012bd8b4572c2ce6")
    version("1.21.0", sha256="886f7ba0e0e86c86dba99417e3165f90b1d3eca59c8cd5a7f645ce28cb5d82a0")
    version("1.20.0", sha256="08bc86df13e4ad56d0447f52628b0f8e36b0476db4e19a90eeb2bd5f260baece")
    version("1.19.0", sha256="c2b68a20d87cc382c2f73dd1ecc6a4f42fb2f590b0b10fbc577382dd35c9e9bd")
    version("1.18.0", sha256="68471e1f398b074edcc28cae0be26a481078adc3edea4df663f01c6bd3b6ae0d")

    variant('gmp',
            default=True,
            description="Enable GMP support in Chapel.",
            )
    variant('hwloc',
            default=True,
            description="Enable hwloc support with bundled hwloc code.",
            )

    variant('lustre',
            default=False,
            description="Enable performance enhancements for lustre \n"
                        "filesystem.",
            )

    variant('pic',
            default=False,
            description="Build position independent code.",
            )

    variant('unwind',
            default=False,
            description="Enable libunwind support for stack traces.",
            )

    variant('threads',
            default='qthreads',
            description="The threading library to use.",
            values=('qthreads', 'pthreads'),
            multi=False,
            )

    variant('comm',
            default='none',
            description="""Choose the communication layer to implement
inter-locale communication.

- 'none' : Only a single locale (default)
- 'gasnet' : GASNet
- 'ofi' : libfabric
- 'ugni' : ??
""",
            values=(
                'none',
                'gasnet',
                'ofi',
                # 'ugni',
            ),
            multi=False,
            )

    variant('allocator',
            default='jemalloc',
            description="""Choose the memory allocator you want to use.

- 'malloc' : The standard C malloc/free commands
- 'jemalloc' : Jason Evan's memory allocator
    (default)
""",
            values=(
                'malloc',
                'jemalloc',
            ),
            multi=False,
            )

    depends_on('gmp', when='+gmp')

    # threads
    depends_on('qthreads', when="threads=qthreads")

    # comm
    depends_on('gasnet', when='comm=gasnet')
    depends_on('libfabric', when='comm=ofi')

    # allocator
    depends_on('jemalloc', when='allocator=jemalloc')

    def setup_build_environment(self, env):

        # GMP
        if '+gmp' in self.spec:
            env.set("CHPL_GMP", 'system')
        else:
            env.set("CHPL_GMP", 'none')

        # threads
        if self.spec.satisfies('threads=qthreads'):
            env.set("CHPL_TASKS", 'qthreads')
        elif self.spec.satisfies('threads=pthreads'):
            env.set("CHPL_TASKS", 'fifo')

        # comm
        if self.spec.satisfies('comm=none'):
            env.set("CHPL_COMM", 'none')
        elif self.spec.satisfies('comm=gasnet'):
            env.set("CHPL_COMM", 'gasnet')
        elif self.spec.satisfies('comm=ofi'):
            env.set("CHPL_COMM", 'libfabric')
        elif self.spec.satisfies('comm=ugni'):
            env.set("CHPL_COMM", 'ugni')

        # allocator
        if self.spec.satisfies('allocator=jemalloc'):
            env.set("CHPL_MEM", 'jemalloc')
        elif self.spec.satisfies('allocator=malloc'):
            env.set("CHPL_MEM", 'cstdlib')

        # hwloc
        if '+hwloc' in self.spec:
            env.set("CHPL_HWLOC", 'bundled')
        else:
            env.set("CHPL_HWLOC", 'none')

        # filesystem
        if '+lustre' in self.spec:
            env.set("CHPL_AUX_FILESYS", 'lustre')
        else:
            env.set("CHPL_AUX_FILESYS", 'none')

        # libunwind
        if '+unwind' in self.spec:
            env.set("CHPL_UNWIND", 'system')
        else:
            env.set("CHPL_UNWIND", 'none')

        # PIC
        if '+pic' in self.spec:
            env.set("CHPL_PIC", 'pic')
        else:
            env.set("CHPL_PIC", 'none')
