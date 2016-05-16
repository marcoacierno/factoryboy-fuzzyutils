from setuptools import setup, find_packages


setup(
    name='fuzzy_utils',
    version='1.6',
    keywords=['factory_boy', 'fuzzy', 'utils'],
    description='Additional fuzzy classes for Factory boy',
    author='Marco Acierno',
    author_email='marcoaciernoemail@gmail.com',
    packages=find_packages(),
    install_requires=['factory_boy'],
    url='https://github.com/marcoacierno/factoryboy-fuzzyutils',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',

        'Intended Audience :: Developers',

        'License :: OSI Approved :: MIT License',

        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Testing',
        'Topic :: Software Development :: Libraries :: Python Modules',

        'Operating System :: OS Independent',

        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
