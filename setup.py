from setuptools import find_packages, setup

setup(
    name="pymodel",
    version="0.1",
    packages=find_packages(),
    install_requires=["alembic", "sqlalchemy"],
    extra_require={"dev": ["black", "isort"]},
)
