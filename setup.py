from setuptools import setup, find_packages

setup(
    name="password-generator",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    entry_points={
        "console_scripts": [
            "generate-password=password_generator.__main__:main",
        ],
    },
)
