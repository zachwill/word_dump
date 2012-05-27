try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name="worddump",
    version="0.1",
    description="Dump disparate words.",
    keywords="word dump, metaphors, juxtapose",
    author="Zach Williams",
    author_email="hey@zachwill.com",
    url="https://github.com/zachwill/word_dump",
    license="MIT",
    packages=["worddump"],
    scripts=["wd"],
    install_requires=["termcolor"],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Topic :: Internet',
        'Topic :: Internet :: WWW/HTTP',
    ],
    test_suite="test.py",
    tests_require=["mock"]
)
