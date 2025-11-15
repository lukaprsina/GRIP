from setuptools import setup

setup(
    name="vendor-grip",
    version="0.0.1",
    packages=["grip"],
    package_dir={"grip": "."},
    include_package_data=True,
    install_requires=["numpy", "torch"],
)
