from setuptools import setup

setup(
    name='pdf_organizer',
    version='0.1',
    description='A simple PDF sorting tool',
    author='Brian McFee',
    author_email='brian.mcfee@nyu.edu',
    url='http://github.com/bmcfee/pdf_organizer',
    download_url='http://github.com/bmcfee/pdf_organizer/releases',
    long_description="""\
        A simple PDF sorting tool
    """,
    scripts=['pdf_organizer', 'aspect_mover'],
    classifiers=[
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Programming Language :: Python",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Utilities",
    ],
    keywords='pdf',
    license='GPL',
    install_requires=[
        'PyPDF2',
    ],
)
