from spack.package import *

class PySln(PythonPackage):
    """Python ."""

    homepage = "https://github.com/salotz/python-sln"
    url = "https://github.com/salotz/python-sln/archive/refs/tags/0.2.tar.gz"

    version('0.2', sha256='ee0efc541580aa4af9cbd2412c3a521238c6ece0474bfd6335db40f96820c13c')
