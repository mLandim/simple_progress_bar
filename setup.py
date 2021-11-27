from setuptools import setup

with open('README.md', 'r') as readme:
    long_description = readme.read()

setup(
  name = 'simple_progress_bar',
  version = '0.0.4',  
  license='MIT',        

  description = 'Simple progress bar for your console apps in python', 
  long_description=long_description,
  long_description_content_type='text/markdown',     
  
  py_modules=['simple_progress_bar'],  
  package_dir={'':'src'},
  
  author = 'Marcelo Landim',                   
  author_email = 'marcelolandim85@gmail.com',      
  url = 'https://github.com/mLandim/simple_progress_bar',   
  project_urls={
        "Bug Report": "https://github.com/mLandim/simple_progress_bar/issues",
  },

  python_requires=">=3.6",
  keywords = ['progress', 'bar', 'progress-bar', 'console', 'terminal'],   
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',  
    'Programming Language :: Python :: 3', 
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Operating System :: OS Independent'
  ],
  extras_require ={
    "dev":[
      "tox>=3.24",
      "check-manifest>=0.47"
      "wheel"
    ]
  }

)