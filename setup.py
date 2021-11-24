from distutils.core import setup

setup(
name = 'simple_progress_bar',         
  packages = ['simple_progress_bar'],  
  version = '0.1',     
  license='MIT',        
  description = 'Simple progress bar util for console apps in python',  
  author = 'Marcelo Landim',                   
  author_email = 'marcelolandim85@gmail.com',      
  url = 'https://github.com/mLandim',   
  download_url = 'https://github.com/mLandim/simple_progress_bar/archive/v_01.tar.gz',   
  keywords = ['PROGRESS', 'BAR', 'PROGRESSBAR', 'CONSOLE'],   
  install_requires=[],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',      
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)