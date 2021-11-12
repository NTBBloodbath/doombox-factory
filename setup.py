from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='doombox-factory',
    packages=['factory'],
    version='1.0.0',
    license='MIT',
    author='NTBBloodbath',
    author_email='bloodbathalchemist@protonmail.com',
    url='https://github.com/NTBBloodbath/doombox-factory',
    description='convert any image to the doombox pallete!',
    long_description=long_description,
    long_description_content_type="text/markdown",
    entry_points={'console_scripts': ['doombox-factory= factory.__main__:main']},
    include_package_data=True,
    install_requires=['image-go-nord', 'rich'],
    keywords=['doombox', 'cli', 'doombox-factory', 'wallpaper', 'image', 'image-go-nord', 'palette', 'factory', 'nord'],
)
