# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Crtm(CMakePackage):
    """The Community Radiative Transfer Model (CRTM) package.
    The CRTM is composed of four important modules for gaseous transmittance,
    surface emission and reflection, cloud and aerosol absorption and
    scattering, and a solver for a radiative transfer."""

    homepage = "https://www.jcsda.org/jcsda-project-community-radiative-transfer-model"
    git = "https://github.com/JCSDA/crtm.git"
    url = "https://github.com/JCSDA/crtm/archive/refs/tags/v2.3.0.tar.gz"

    maintainers(
        "BenjaminTJohnson",
        "t-brown",
        "edwardhartnett",
        "AlexanderRichert-NOAA",
        "Hang-Lei-NOAA",
        "climbfuji",
    )
    variant(
        "fix", default=False, description='Download CRTM coeffecient or "fix" files (several GBs).'
    )
    variant(
        "build_type",
        default="RelWithDebInfo",
        description="CMake build type",
        values=("Debug", "Release", "RelWithDebInfo", "MinSizeRel"),
    )

    depends_on("cmake@3.15:")
    depends_on("git-lfs")
    depends_on("netcdf-fortran", when="@2.4.0:")
    depends_on("netcdf-fortran", when="@v2.3-jedi.4")
    depends_on("netcdf-fortran", when="@v2.4-jedi.1")
    depends_on("netcdf-fortran", when="@v2.4-jedi.2")
    depends_on("netcdf-fortran", when="@v2.4.1-jedi")
    depends_on("netcdf-fortran", when="@v3.0.0-rc.1")

    depends_on("crtm-fix@2.3.0_emc", when="@2.3.0 +fix")
    depends_on("crtm-fix@2.4.0_emc", when="@2.4.0 +fix")

    depends_on("ecbuild", type=("build"), when="@v2.3-jedi.4")
    depends_on("ecbuild", type=("build"), when="@v2.4-jedi.1")
    depends_on("ecbuild", type=("build"), when="@v2.4-jedi.2")
    depends_on("ecbuild", type=("build"), when="@v2.4.1-jedi")
    depends_on("ecbuild", type=("build"), when="@v3.0.0-rc.1")

    version("v3.0.0-rc.1", sha256="b7f8c251168bcc3c29586ee281ed456e3115735d65167adcbcf4f69be76b933c")
    version("v2.4.1-jedi", sha256="fd8bf4db4f2a3b420b4186de84483ba2a36660519dffcb1e0ff14bfe8c6f6a14")
    # REL-2.4.0_emc (v2.4.0 ecbuild does not work)
    version("2.4.0", commit="5ddd0d6")
    # Uses the tip of REL-2.3.0_emc branch
    version("2.3.0", commit="99760e6")
    # JEDI applications so far use these versions
    # Branch release/crtm_jedi
    version("v2.3-jedi.4", commit="bfede42")
    # Branch release/crtm_jedi_v2.4.0
    version("v2.4-jedi.1", commit="8222341")
    version("v2.4-jedi.2", commit="62831cb")

    def url_for_version(self, version):
        if self.spec.satisfies("@v3") or version >=  Version("3.0.0"):
            return "https://github.com/JCSDA/crtmv3/archive/refs/tags/{}.tar.gz".format(version)
        else:
            return "https://github.com/JCSDA/crtm/archive/refs/tags/{}.tar.gz".format(version)
