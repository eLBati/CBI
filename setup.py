from distutils.core import setup

setup(name='cbi',
      version='0.2',
      packages=['cbi'],
      description='CBI flows wrapper',
      author='Lorenzo Battistini',
      author_email='lorenzo.battistini@domsense.com',
      url='https://code.launchpad.net/~openobject-italia-core-devs/openobject-italia/cbi',
      classifiers=[
         'Development Status :: 4 - Beta',
         'Environment :: Plugins',
         'Intended Audience :: Developers',
         'Intended Audience :: Information Technology',
         'License :: OSI Approved :: GNU General Public License (GPL)',
         'Operating System :: OS Independent',
         'Programming Language :: Python',
         'Topic :: Office/Business',
      ],
      long_description=open('README.txt').read(),
      license='GPL-3',
     )
