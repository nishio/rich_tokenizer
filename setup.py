from setuptools import setup

setup(name='rich_tokenizer',
      version='0.1',
      description='wrapper of MeCab',
      url='http://github.com/nishio/rich_tokenizer/',
      author='NISHIO Hirokazu',
      author_email='nishio.hirokazu@gmail.com',
      license='MIT',
      packages=['rich_tokenizer'],
      install_requires=['mecab-python3==0.996.5'],
      zip_safe=True)
