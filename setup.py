from setuptools import find_packages, setup
setup(
    name='simplecloudfunlocaltest',
    packages=find_packages(include=['simplecloudfunlocaltest']),
    version='0.1.0',
    description='Funcion para explicar en el data hub',
    author='Marco Ycaza',
    license='MIT',
    install_requires=['flask','google-cloud'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
    entry_points={
        "console_scripts": [
            "sff=simplecloudfunlocaltest._cli:_cli",
        ]
    },
)