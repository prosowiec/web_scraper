from distutils.core import setup


setup(name='Polish Amazon webscraper',
      version='0.9',
      description='Scraps images, descriptiones and technical specs; with custom GUI',
      author='Łukasz Janikowski',
      author_email='lukasz.janikowski.inw@gmail.com',
      packages=[
        'PyQt5', 
        'requests',
        'beautifulsoup4',
        'defaultdict'
        'wget'],
     )