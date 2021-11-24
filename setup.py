from setuptools import setup

with open('PyPI.md', 'r', encoding="utf-8") as readme:
    long_description = readme.read()

setup(
name = 'simple_progress_bar',         
  packages = ['simple_progress_bar'],  
  version = '0.1.2',     
  license='MIT',        
  description = 'Simple progress bar util for console apps in python', 
  long_description=long_description,
  long_description_content_type='text/markdown',
  author = 'Marcelo Landim',                   
  author_email = 'marcelolandim85@gmail.com',      
  url = 'https://github.com/mLandim/simple_progress_bar',   
  project_urls={
        "Issues": "https://github.com/mLandim/simple_progress_bar/issues",
  },
  python_requires=">=3.6",
  keywords = ['PROGRESS', 'BAR', 'PROGRESSBAR', 'CONSOLE', 'TERMINAL'],   
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3.6',
  ],
)