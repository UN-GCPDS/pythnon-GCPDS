import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
   README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
<<<<<<< HEAD
    name='gcpds-utils',
    version='0.1a0',
    packages=['gcpds.utils'],
=======
    name='gcpds',
    version='0.1a0',
>>>>>>> 38fc044e1da32068176d2a17e510389dc2afa2b5

    author='Yeison Cardona',
    author_email='yencardonaal@unal.edu.co',
    maintainer='Yeison Cardona',
    maintainer_email='yencardonaal@unal.edu.co',

    download_url='',

<<<<<<< HEAD
    install_requires=['numpy',
                      'scipy',
                      'matplotlib',
                      'mne',
                      'tables',

                      'jinja2',
                      'colorama',
                      'sphinx',
                      'ipython',
                      'tqdm',

                      ],

    scripts=[
       "cmd/gcpds_distutils",
    ],


=======
    install_requires=['gcpds-utils',
                      'gcpds-entropies',
                      ],

>>>>>>> 38fc044e1da32068176d2a17e510389dc2afa2b5
    include_package_data=True,
    license='Simplified BSD License',
    description="",
    zip_safe=False,

    long_description=README,
    long_description_content_type='text/markdown',

    python_requires='>=3.6',

    classifiers=[
       'Development Status :: 4 - Beta',
       'Intended Audience :: Developers',
       'Intended Audience :: Education',
       'Intended Audience :: Healthcare Industry',
       'Intended Audience :: Science/Research',
       'License :: OSI Approved :: BSD License',
       'Programming Language :: Python :: 3.7',
       'Programming Language :: Python :: 3.8',
       'Topic :: Scientific/Engineering',
       'Topic :: Scientific/Engineering :: Artificial Intelligence',
       'Topic :: Scientific/Engineering :: Human Machine Interfaces',
       'Topic :: Scientific/Engineering :: Medical Science Apps.',
       'Topic :: Software Development :: Embedded Systems',
       'Topic :: Software Development :: Libraries',
       'Topic :: Software Development :: Libraries :: Application Frameworks',
       'Topic :: Software Development :: Libraries :: Python Modules',
       'Topic :: System :: Hardware :: Hardware Drivers',
    ],

)
