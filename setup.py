import setuptools
import webcamd as wd

with open('README.md', 'r') as file:
    long_description = file.read()

setuptools.setup(
    name=wd.APP_NAME,
    version=wd.APP_VERSION,
    author=wd.APP_AUTHOR,
    maintainer=wd.MAINTAINER_NAME,
    maintainer_email=wd.MAINTAINER_EMAIL,
    license=wd.APP_LICENSE,
    description=wd.APP_DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    url=wd.APP_URL,
    project_urls={
        'Documentation': 'https://github.com/dmitri-mcguckin/webcamd/blob/main/README.md',
        'Bug Tracking': 'https://github.com/dmitri-mcguckin/webcamd/issues'
    },
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Software Development :: User Interfaces",
        "Topic :: System :: Monitoring",
        "Topic :: System :: Networking :: Monitoring :: Hardware Watchdog"
    ],
    install_requires=[
        "opencv-python == 4.5.3.56",
        "PIL-Tools == 1.1.0"
    ],
    extras_require={
        "dev": [
            "setuptools",
            "wheel",
            "flake8",
            "twine",
            "sphinx",
            "sphinx_rtd_theme",
        ]
    },
    python_requires='>=3.9.0',
    entry_points={
        "console_scripts": [
            f'{wd.APP_NAME} = webcamd.__main__:main'
        ]
    }
)
