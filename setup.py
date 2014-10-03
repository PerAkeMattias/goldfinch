from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='goldfinch',
      version='0.3',
      description='Use to make sure that filenames will always be valid',
      url='https://github.com/PerAkeMattias/goldfinch',
      author='Per Ake Mattias',
      author_email='PerAkeMattias@gmail.com',
      license='MIT',
      packages=['goldfinch'],
      zip_safe=True)
