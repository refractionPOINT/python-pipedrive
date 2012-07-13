from setuptools import setup, find_packages

setup(
    name='python-pipedrive',
    version="0.1.0",
    license="MIT",

    install_requires = [
        "httplib2",
    ],

    description='Light wrapper around Pipedrive API',
    long_description=open('README.md').read(),

    author='Jonathan Scott',
    author_email='jonathanscott1989@gmail.com',

    url='https://github.com/jscott1989/python-pipedrive',
    download_url='https://github.com/jscott1989/python-pipedrive/downloads',

    include_package_data=True,

    packages=['pipedrive'],

    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ]
)