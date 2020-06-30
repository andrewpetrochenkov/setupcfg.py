import setuptools

setuptools.setup(
    name='setupcfg',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)
