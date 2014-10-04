from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='goldfinch',
      version='0.4',
      description='Use to make sure that filenames will always be valid- Now in Python 3 too',
      url='https://github.com/PerAkeMattias/goldfinch',
      author='Per Ake Mattias',
      author_email='PerAkeMattias@gmail.com',
      license='MIT',
      packages=['goldfinch'],
      zip_safe=True)
