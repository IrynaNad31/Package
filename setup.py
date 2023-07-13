from setuptools import setup, find_namespace_packages

setup(
    name='Ihomework',
    version='0.0.1',
    description='This is my first package',
    url='github.com/IrynaNadieina/Package',
    author='Iryna Nadieina',
    author_email='irinanadeina31@gmail.com',
    license='Apache 2.0',
    packages=find_namespace_packages(),
    entry_points={'console_scripts': ['Ihomework = clean_folder.clean:file_parser']}
)