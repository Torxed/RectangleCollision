from setuptools import setup, find_packages

classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Developers',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]

setup(
  name='RectangleCollision',
  version='0.0.0.1',
  description='A basic collision module',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',
  author='shadow00dev',
  author_email='twistcharlievlogs@gmail.com',
  license='MIT',
  classifiers=classifiers,
  keywords='collision',
  packages=find_packages(),
  install_requires=['']
)