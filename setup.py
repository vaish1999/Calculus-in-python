from distutils.core import setup
setup(
  name = 'pythcalculus',         
  packages = ['pythcalculus'],   
  version = '0.1',      
  license='GPL 2.0',        
  description = 'Integrate and Differentiate over here!',   
  author = 'Vaishakh Nargund',                  
  author_email = 'vaishakh.nargund1999@gmail.com',      
  url = 'https://github.com/vaish1999/Calculus-in-python',  
  download_url = 'https://github.com/vaish1999/Calculus-in-python/archive/v1.0.tar.gz',   
  keywords = ['calculus', 'python', 'differentiate','integrate','derivative'],   
  install_requires=[           
          'math',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',     
    'Intended Audience :: Developers',     
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',   
    'Programming Language :: Python :: 3',      
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
