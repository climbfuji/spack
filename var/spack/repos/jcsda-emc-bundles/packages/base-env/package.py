# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import sys

from spack.package import *


class BaseEnv(BundlePackage):
    """Basic development environment used by other environments"""

    homepage = "https://github.com/noaa-emc/spack-stack"
    git = "https://github.com/noaa-emc/spack-stack.git"

    maintainers = ["climbfuji", "AlexanderRichert-NOAA"]

    version("1.0.0")

    variant("shared", default=True, description="Build shared libraries as much as possible")

    # Basic utilities
    if sys.platform == "darwin":
        depends_on("libbacktrace", type="run")
    depends_on("cmake", type="run")
    depends_on("git", type="run")
    depends_on("wget", type="run")
    depends_on("curl", type="run")

    # I/O
    with when("+shared"):
        shared_variant = "+shared"
    with when("~shared"):
        shared_variant = "~shared"
    depends_on("zlib{}".format(shared_variant), type="run", when="{}".format(shared_variant))
    depends_on("hdf5{}".format(shared_variant), type="run", when="{}".format(shared_variant))
    depends_on("netcdf-c{}".format(shared_variant), type="run", when="{}".format(shared_variant))
    depends_on("netcdf-fortran{}".format(shared_variant), type="run", when="{}".format(shared_variant))
    depends_on("parallel-netcdf{}".format(shared_variant), type="run", when="{}".format(shared_variant))
    depends_on("parallelio{}".format(shared_variant), type="run", when="{}".format(shared_variant))
    depends_on("nccmp", type="run")

    # Python
    depends_on("python@3.7:")

    # There is no need for install() since there is no code.
