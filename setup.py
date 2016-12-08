from setuptools import find_packages, setup

install_requires = [
    'factory-boy==2.7.0',
    'wagtail',
]

docs_require = [
    'sphinx>=1.4.0',
]

tests_require = [
    'pytest-django==3.1.2',
    'pytest-pythonpath==0.7.1',
    'psycopg2',

    'isort==4.2.5',
    'flake8==3.0.3',
    'flake8-blind-except==0.1.1',
    'flake8-debugger==1.4.0',
]

with open('README.rst') as fh:
    long_description = fh.read()

setup(
    name='wagtail_factories',
    version='0.0.1',
    description='Factory boy classes for wagtail',
    long_description=long_description,
    author="Michael van Tellingen",
    author_email="michaelvantellingen@gmail.com",
    url='https://www.github.com/mvantellingen/wagtail-factories/',
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require={
        'docs': docs_require,
        'test': tests_require,
    },
    entry_points={},
    package_dir={'': 'src'},
    packages=find_packages('src'),
    include_package_data=True,
    license='MIT',
    classifiers=[
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
    zip_safe=False,
)
