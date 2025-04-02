
import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='nose',
    version="1.0.0",
    author='cielavenir',
    author_email='cielartisan@gmail.com',
    description='fake nose redirecting to nose2',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/cielavenir/nose-nose2-proxy',
    keywords='nose nose2',
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Topic :: Software Development',
    ],
    packages=setuptools.find_packages(),
    # python_requires=">=2.7",
    install_requires=[
        'nose2',
    ],
)
