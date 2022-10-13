from setuptools import setup

setup(
    name="{{package_name}}",
    version="0.0.2",
    description="Package description",
    author="Kinetix",
    author_email="sam@kinetix.tech",
    packages=["{{package_name}}"],
    install_requires=[
    ],
    extras_require={
        "dev" : ["pytest"]
    },
)
