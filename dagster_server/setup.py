from setuptools import find_packages, setup

setup(
    name="dagster_server",
    packages=find_packages(exclude=["dagster_server_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud"
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
