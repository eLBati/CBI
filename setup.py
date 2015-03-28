from distutils.core import setup

setup(name='cbi',
      version='0.2',
      package_dir={'cbi': 'src'},
      packages=['cbi'],
      description='CBI flows wrapper',
      author='Lorenzo Battistini',
      author_email='lorenzo.battistini@agilebg.com',
      url='https://github.com/eLBati/CBI',
      classifiers=[
         'Development Status :: 3 - Alpha',
         'Environment :: Plugins',
         'Intended Audience :: Developers',
         'Intended Audience :: Information Technology',
         'License :: OSI Approved :: GNU General Public License (GPL)',
         'Operating System :: OS Independent',
         'Programming Language :: Python',
         'Topic :: Office/Business',
      ],
      long_description=open('README.rst').read(),
      license='GPL-3',
     )
