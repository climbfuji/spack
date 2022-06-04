# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
import os


class Metplus(Package):
    """
    METplus is a verification framework that spans a wide range of temporal 
    (warn-on-forecast to climate) and spatial (storm to global) scales.
    """

    homepage = "https://dtcenter.org/community-code/metplus"
    url = "https://github.com/dtcenter/METplus/archive/refs/tags/v4.1.0.tar.gz"

    maintainers = ['kgerheiser']

    version('4.1.1', sha256='81c03474f57cef6c7196d65fba6427365fd761578d99804c6c367f21a29b8ced')
    version('4.1.0', sha256='4e4d74be64c9c57b910824ebefff42eb3a9bb7e8e325d86b7a3f7fdd59d3e45d')
    version('4.0.0', sha256='650c65b0cf1f1993209e69e469903c83fb4ae3c693060d8392fc1dece52493e2')
    version('3.1.1', sha256='d137420c56b2736b09ab713300f25c16e1d6fe523d3f3e4d811471aed83b0d85')

    variant('tcmpr_plotter', default=False, description='Enable TCMPRPlotter.')
    variant('series_analysis', default=False, description='Enable CyclonePlotter wrapper.')
    variant('cycloneplotter', default=False, description='Enable CyclonePlotter wrapper.')
    variant('makeplots', default=False, description='Enable MakePlots Wrapper.')
    variant('plotdataplane', default=False, description='Generate images from Postscript output.')

    depends_on('met+python', type=('run'))
    depends_on('py-python-dateutil', type=('run'))

    depends_on('py-cartopy', when='+makeplots', type=('run'))
    depends_on('py-matplotlib', when='+cycloneplotter', type=('run'))
    depends_on('py-cartopy', when='+cycloneplotter', type=('run'))

    depends_on('r', when='+tcmpr_plotter', type=('run'))
    depends_on('imagemagick', when='+series_analysis', type=('run'))
    depends_on('imagemagick', when='+plotdataplane', type=('run'))

    def install(self, spec, prefix):
        if spec.satisfies('@4.0.0:'):
            conf = 'defaults.conf'
        else:
            conf = 'metplus_system.conf'

        metplus_config = FileFilter(
            join_path('parm', 'metplus_config', conf))

        met_prefix = spec['met'].prefix
        metplus_config.filter(r'MET_INSTALL_DIR = /path/to',
                              'MET_INSTALL_DIR = {}'.format(met_prefix))

        install_tree(self.stage.source_path, prefix)

    def setup_run_environment(self, env):
        env.prepend_path('PATH', self.prefix.ush)
