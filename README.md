# Tips and Tools for Reproducible Projects with Python

So far you have learnt:

* how to analyze complex geospatial datasets
* how to write readable code
* how to write testable code
* how to write version-controlled code


Plan for today is to discuss:

* organizing project repositories
* using virtual environments
* creating modules
* building packages
* setting up automatic testing


### Directory Structure
---
* 	How should we structure our data science project repositories?
		
Example:


```
.
+-- data
|   +-- raw
|   +-- processed
|
+-- src
|   +-- PythonModules
|   +-- tests
|   
+-- notebooks
|   +-- exploratory
|   +-- expositionary
|
+-- references
|   +-- papers
|   +-- tutorials
|
+-- results 
+-- README.md
+-- LICENSE.txt
```

No one solution: adjust as the project evolves.

Comprehensive Project Templates:

* [Data Science Cookiecutter](https://drivendata.github.io/cookiecutter-data-science/#contributing) - Data Science Project Template
* [Shablona](https://github.com/uwescience/shablona) - Python Package Template


Exercise: 

* Reorganize the Geopandas Tutorial
   * fork  https://github.com/valentina-s/mobility-index
   * git clone fork_address
   * move all notebooks to a notebook folder
   * create a mobility_index folder which will store all the code
   * create a tests folder under mobility_index which stores the tests


### Distributions & Package Managers
---
Conda vs pip


What is [Conda](https://docs.conda.io/en/latest/)? 

* Anaconda is a Python distribution slightly different from the default Python distribution, and comes with its own package manager (conda).

* Conda packages come in the form of .whl files (wheel files). They are precompiled packages: i.e. they are compiled for each specific operating system. 
They are fast to install. (Installing Numpy from scratch takes forever compiling C code)
Miniconda is even faster to install as it is bare bones: better for deploying: have only what you need.

What is [pip](https://pip.pypa.io/en/stable/)?

Package manager for Python. Install packages from [PyPi](https://pypi.python.org/pypi). There are packages in pip which are not in conda. 


`pip install` vs `conda install`

```
pip freeze

conda list
```

There are also additional conda packages on [conda-forge](https://conda-forge.org/). You can install them by 

```
conda install -c conda-forge package_name 
```

and you can build your own.




### Virtual Environments
---
What is a Python virtual environment?

A folder with all Python executables and libraries and a link to them. Virtual environments take space!

Pure Python: [virtualenv](https://virtualenv.pypa.io/en/stable/), [pipenv](https://docs.pipenv.org/en/latest/)

Anaconda Python: [conda environment](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html) 

Create conda envs by:

```
conda create --name newEnv python=2 extra_packages
```

View environments:

```
conda env list
```

On Unix:

```
source activate newEnv
do stuff
conda install more_packages
source deactivate
```

On Windows:

```
activate newEnv
do stuff
conda install more_package
deactivate
```

Saving environments:

```
conda env export -f exported_env.yml
```

Load an environment from .yml file:

```
conda env create -f exported_env.yml
```


You can do the same thing with pip:

```
pip freeze > requirements.txt
pip install -r requirements.txt
```

We can see that the list of packages is pretty long (because of the dependencies), and quite specific. 

Sometimes you just want to list the ones which you need (and not specify the version). You can write create the following `requirements.txt` file:

```
geopandas
shapely
```

You can also use conda to install from a requirements file:

``` 
conda install --file requirements.txt
```

Jupyter Notebooks and virtual environments:

* Make sure to install Jupyter within virtual environment
* Run `jupyter notebook` within the activated environment

Setting up an environment switch within the Jupyter notebook:

https://ipython.readthedocs.io/en/stable/install/kernel_install.html

### More Virtualization
---
 
 * [Docker](https://www.docker.com/) 
 * [Vagrant](https://www.vagrantup.com/) 
 *  AWS public AMIs 
 *  friend's laptop



	
### Cross-platform Directory Paths
---

* Make paths independent of platform and all relative to directory structure

```python
	import os
	
	# current path
	current_path = os.getcwd()
	
	# join paths for Windows and Unix
	code_path = os.path.join(current_path, "src")
	
	# make sure paths/files exist before reading
	os.path_exists() 
	os.path.isfile()
```

### Modules & Packages
---


  * move functions from notebooks to a `.py` file
  * import the .py as a module
  
  ```
  import module_name
  module_name.function()
  ```
  
  ```
  import module_name as mod 
  mod.function()
  ```

  ```   
  from module_name import myFunction
  function()
  ```

  * order of importing modules
  	* first checks system and Python modules
	* checks local directory or modules in added system paths
	
  * relative imports
  
  ```
  from ..module import  
  ```
	
  * reloading modules (Python 3)   
  ```
  from imp import reload
  reload(module_name)
  ```
     
  * install module as a package
  	 * create a [setup.py](https://packaging.python.org/tutorials/distributing-packages/#setup-py) file
  
  * run the setup.py file
  	
  ```
  python setup.py install package_name
  ```
  and you will be able to import the package from anywhere!
    
  * subpackages
     *	put `__init__.py` in every folder
    
	```
	.
	+-- package   
	|+-- __init__.py
	|
	+-- subpackage
        	|
           	+-- __init__.py
           	|
           	+-- module.py
	``` 
	 
	 
     	```
	    from subpackage import module
	```
     
  * [git submodules](https://github.com/blog/2104-working-with-submodules) 
  	- add external github repos to your github project


### Testing
---
* Locally 
	* [nose](http://nose.readthedocs.io/en/latest/)

	```
	conda install nose
	```

	For each function in library.py write a test function:

	```
	+-- src
	|   +-- library.py
	|   +-- tests
	|       +-- test_library.py
	```

	Run the tests:

	```
	nosetests
	``` 
In practice, we most probably we will forget to run nosetests after every change we make in the code, luckily, we can do it automatically using continuous integration.

* Remotely:
	*  [Travis-CI](https://travis-ci.org/) (free for public repos)
		* specification by a [travis.yml](https://github.com/scikit-learn/scikit-learn/blob/master/.travis.yml)
	*  [AppVeyor (for Windows)](https://www.appveyor.com/) 
	*  [CircleCI](https://circleci.com/)
	*  [Wercker](http://www.wercker.com/) (based on [Docker](https://www.docker.com/) containters)
	*  [Jenkins](https://jenkins.io/) - need to configure it

	
	Exercise: let's set up Travis-CI for the Mobility Index project. 
	
	* log in to Travis-CI with your github account
	* search for the repository you want to activate with travis and switch it on
	* write a `.travis.yml` specifying the build requirements and tests
	
	[Travis-CI Tutorial](https://docs.travis-ci.com/user/tutorial/)

	Types of tests:
	
	* unit testing
	* integration testing
	* regression testing
	* functional testing 


	
	Test Coverage - [Coveralls](https://coveralls.io/)


  	Exercise(extra): explore how you can set up automatic coverage check
  

### Editors
---

* [PyCharm](https://www.jetbrains.com/pycharm/) - integration with GitHub
* [Atom](https://atom.io/) - coloring in Github (extra packages)
* [JupyterLab](https://) (web based -> can run on server)
* [Spyder](https://pythonhosted.org/spyder/) Matlab-like IDE
  

### Documentation
---
  * [Nbconvert](https://nbconvert.readthedocs.io/en/latest/) - to pdf, to html
  * [Reveal.js](http://lab.hakim.se/reveal-js/#/):  Jupyter notebook -> slides  ([Instructions](http://veekaybee.github.io/presentations-the-hard-way/))
  * [css styles for notebook](https://github.com/transcranial/jupyter-themer)
  * [Sphinx](http://www.sphinx-doc.org/en/stable/), [readthedocs](https://readthedocs.org/), ... (automatically generate documentation, integrate with CI)  
  * [gh-pages](https://pages.github.com/) - project website based on Jekyll
  * [Binder (of notebooks)](http://mybinder.org/) (free sharing of github jupyter notebooks)
  * [Jupyter Hub](https://jupyterhub.readthedocs.io/en/latest/) + [Kubernetes](https://kubernetes.io/) - sharing reliably with many people
  * [SageMathCloud - CoCalc](http://blog.sagemath.com/cocalc/2017/05/20/smc-is-now-cocalc.html)
  

### Extra Resources
---

[Hitchhikers Guide for packaging](https://the-hitchhikers-guide-to-packaging.readthedocs.io/en/latest/)


### Survey
---
[Survey](https://tinyurl.com/2019ProjectOrgEtc)







