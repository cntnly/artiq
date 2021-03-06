#!/usr/bin/env python3.5

from setuptools import setup, find_packages
import sys

import versioneer


if sys.version_info[:3] < (3, 5, 1):
    raise Exception("You need Python 3.5.1+")


# Depends on PyQt5, but setuptools cannot check for it.
requirements = [
    "sphinx", "sphinx-argparse", "asyncserial", "numpy", "scipy",
    "python-dateutil", "prettytable", "h5py",
    "quamash", "pyqtgraph", "pygit2", "aiohttp",
    "llvmlite_artiq", "pythonparser", "python-Levenshtein",
    "lit", "OutputCheck",
]

scripts = [
    "artiq_browser=artiq.frontend.artiq_browser:main",
    "artiq_client=artiq.frontend.artiq_client:main",
    "artiq_compile=artiq.frontend.artiq_compile:main",
    "artiq_coreanalyzer=artiq.frontend.artiq_coreanalyzer:main",
    "artiq_coreconfig=artiq.frontend.artiq_coreconfig:main",
    "artiq_corelog=artiq.frontend.artiq_corelog:main",
    "artiq_ctlmgr=artiq.frontend.artiq_ctlmgr:main",
    "artiq_dashboard=artiq.frontend.artiq_dashboard:main",
    "artiq_influxdb=artiq.frontend.artiq_influxdb:main",
    "artiq_master=artiq.frontend.artiq_master:main",
    "artiq_mkfs=artiq.frontend.artiq_mkfs:main",
    "artiq_rpctool=artiq.frontend.artiq_rpctool:main",
    "artiq_run=artiq.frontend.artiq_run:main",
    "artiq_flash=artiq.frontend.artiq_flash:main",
    "lda_controller=artiq.frontend.lda_controller:main",
    "novatech409b_controller=artiq.frontend.novatech409b_controller:main",
    "pdq2_client=artiq.frontend.pdq2_client:main",
    "pdq2_controller=artiq.frontend.pdq2_controller:main",
    "thorlabs_tcube_controller=artiq.frontend.thorlabs_tcube_controller:main",
]

setup(
    name="artiq",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    author="M-Labs / NIST Ion Storage Group",
    author_email="sb@m-labs.hk",
    url="https://m-labs.hk/artiq",
    description="A control system for trapped-ion experiments",
    long_description=open("README.rst").read(),
    license="GPL",
    install_requires=requirements,
    extras_require={},
    dependency_links=[
        "git+https://github.com/m-labs/pyqtgraph.git@develop#egg=pyqtgraph",
        "git+https://github.com/m-labs/llvmlite.git@artiq#egg=llvmlite_artiq"
    ],
    packages=find_packages(),
    namespace_packages=[],
    include_package_data=True,
    ext_modules=[],
    entry_points={
        "console_scripts": scripts,
    }
)
