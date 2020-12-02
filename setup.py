from setuptools import setup

setup(
    name = 'Lina',
    version = '1.0.0',
    url = 'https://github.com/TakutoYoshikai/lina.git',
    license = 'MIT LICENSE',
    author = 'Takuto Yoshikai',
    author_email = 'takuto.yoshikai@gmail.com',
    description = 'lina is a steganography program. It can hide a binary file or a text file into multiple png images.',
    install_requires = ['setuptools', "pycrypto"],
    packages = find_packages(where="src"),
    package_dir={"":"src"},
    entry_points={
        "console_scripts": [
            "lina = src.lina:main",
        ]
    }
)
