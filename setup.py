
from setuptools import setup

setup(
    package_dir={"":"/"},
    name='core',
    description='signal and frequency system generator',
    author='Matthew Finch',
    author_emails='finchrmatthew@gmail.com',
    packages=['core'],
    install_requires=[
        'dash==1.19.0',
        'dash-core-components==1.15.0',
        'dash-cytoscape==0.2.0',
        'dash-html-components==1.1.2',
        'dash-renderer==1.9.0',
        'dash-table==4.11.2',
        'Flask==1.1.2',
        'matplotlib==3.1.3',
        'gunicorn==20.0.4',
        'numpy==1.18.0',
        'scipy==1.4.1'
    ],
    zip_safe=False
)