import setuptools
import yunionclient

from yunionclient.openstack.common import setup

requires = setup.parse_requirements()


setuptools.setup(
    name="python-yunionclient",
    version=yunionclient.__version__,
    description="Client library for Yunion Cloud API",
    url='http://wiki.yunionyun.com/pages/viewpage.action?pageId=48989444',
    author='Yunion Technology',
    author_email='dev@yunionyun.com',
    packages=setuptools.find_packages(exclude=['tests', 'tests.*']),
    data_files=[],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    install_requires=requires,
    entry_points={
        'console_scripts': ['climc = yunionclient.shell:main']
    }
)
