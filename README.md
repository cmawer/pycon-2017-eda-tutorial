# EDA Tutorial

## The datasets 

* [Redcard Dataset](https://osf.io/47tnc/)
* [Aquastat Dataset](http://www.fao.org/nr/water/aquastat/main/index.stm)

## Before the tutorial 

### 1. Clone this repo
Clone this repository locally on your laptop. 
1. Go to the green **Clone or download** button at the top of the repository page and copy the https link. 
2. From the command line run the command: 

```bash
git clone https://github.com/cmawer/pycon-2017-eda-tutorial.git
```

### 2. Set up your python environment 

#### Install conda or miniconda
We recommend using conda for managing your python environments. Specifically, we like miniconda, which is the most lightweight installation. You can install miniconda [here](https://conda.io/miniconda.html). However, the full [anaconda](https://www.continuum.io/downloads) is good for beginners as it comes with many packages already installed. 

#### Create your environment 

 Once installed, you can create the environment necessary for running this tutorial by running the following command from the command line in the `setup/` directory of this repository: 
 
```bash
conda update conda
```

then: 

```bash
conda env create -f environment.yml
```

 This command will create a new environment named `eda3`. If you are on Windows or run into errors, try:
 
 ```bash
 conda env create -f environment-noversions.yml
 ```
 
 If that still doesn't work:
  
 ```bash
 conda env create -f environment-basic.yml
 ```
 
 If that doesn't work, you'll have to trouble shoot! 
 
 #### Activate your environment
 To activate the environment you can run this command from any directory:
 
 `source activate eda3` (Mac/Linux)
 
 `activate eda3` (Windows)
 
 #### Non-conda users 
 

If you are experienced in python and do not use conda, the `requirements.txt` file is available also in the `setup/` directory for pip installation.
 
### 3. Enable `ipywidgets`

 We will be using widgets to create interactive visualizations. They will have been installed during your environment setup but you still need to run the following from the commandline: 
 
```bash
jupyter nbextension enable --py --sys-prefix widgetsnbextension
```
 
### 4. Test your python environment 
 
 Now that your environment is set up, let's check that it works. 
 
 1. Go to the `setup/` directory from the command line and start a Jupyter notebook instance: 
 
```bash
jupyter notebook
```

a lot of text should appear -- you need to leave this terminal running for your Jupyter instance to work.

 2. Assuming this worked, open up the notebook titled `test-my-environment.ipynb`

 3. Once the notebook is open, go to the `Cell` menu and select `Run All`. 
 
 4. Check that every cell in the notebook ran (i.e did not produce error as output). `test-my-environment.html` shows what the notebook should look like after running. 
 
### 5. Prepare the backup option

If there were errors upon running your notebook (or during any step prior), feel free to ask for help before from your fellow classmates on slack in the operating system channel relevant to you. 

However, in an effort to keep this tutorial about EDA and not python package installation, if you cannot get the notebook to run prior to Wednesday, please sign up for an account on [Azure Notebooks](https://notebooks.azure.com/) where we will provide a library that can be cloned and ran in the cloud without any setup or installation. 

We recommend everyone sign up just in case problems are ran into during the tutorial. 
