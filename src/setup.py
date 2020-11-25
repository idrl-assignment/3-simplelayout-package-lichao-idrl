import setuptools

setuptools.setup(
    name="simplelayout-lichao-idrl", # 此处需要加账号
    version="0.0.1",
    packages=setuptools.find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    install_requires=["numpy", "scipy","argparse","pathlib","matplotlib"],
    entry_points = {
        "console_scripts":['simplelayout = simplelayout.__main__:main'],
    }
)