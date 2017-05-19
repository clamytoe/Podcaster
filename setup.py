from setuptools import setup


setup(
    name='Podcaster',
    version='1.0',
    py_modules=[
        'main',
        'podcaster.podcaster',
        'podcaster.models',
        'podcaster.utils.utils',
    ],
    install_requires=[
        'click',
        'feedparser',
        'SQLAlchemy',
    ],
    entry_points='''
        [console_scripts]
        podcaster=main:main
    ''',
)
