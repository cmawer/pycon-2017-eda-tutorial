# EDA Tutorial


This repo holds the contents developed for the tutorial, *Exploratory Data Analysis in Python*, presented at PyCon 2017 on May 17, 2017. 

We suggest setting up your environment and testing it (as detailed below) and then following along the video of the tutorial found [here](https://www.youtube.com/watch?v=W5WE9Db2RLU). 

As there was limited time for instruction, we also recommend pausing throughout and practicing some of the methods discussed as you go. 

We welcome any PRs with other demonstrations of how you would perform EDA on the provided datasets. 

## The datasets 

* [Redcard Dataset](https://osf.io/47tnc/)
* [Aquastat Dataset](http://www.fao.org/nr/water/aquastat/main/index.stm)

## Before the tutorial 

### Microsoft Azure option
If you don't want to deal with setting up your environment or have any problems with the below instructions, you can work through the tutorial through Microsoft Azure Notebooks by creating an account and cloning the tutorial library found [here](https://notebooks.azure.com/chloe/libraries/pycon-2017-eda-tutorial) (all of this is for free, forever). 

### Github option 

#### 1. Clone this repo
Clone this repository locally on your laptop. 
1. Go to the green **Clone or download** button at the top of the repository page and copy the https link. 
2. From the command line run the command: 

```bash
git clone https://github.com/cmawer/pycon-2017-eda-tutorial.git
```

#### 2. Set up your python environment 

##### Install conda or miniconda
We recommend using conda for managing your python environments. Specifically, we like miniconda, which is the most lightweight installation. You can install miniconda [here](https://conda.io/miniconda.html). However, the full [anaconda](https://www.continuum.io/downloads) is good for beginners as it comes with many packages already installed. 

##### Create your environment 

 Once installed, you can create the environment necessary for running this tutorial by running the following command from the command line in the `setup/` directory of this repository: 
 
```bash
conda update conda
```

then: 

```bash
conda env create -f environment.yml
```

 This command will create a new environment named `eda3`. 
 
 ##### Activate your environment
 To activate the environment you can run this command from any directory:
 
 `source activate eda3` (Mac/Linux)
 
 `activate eda3` (Windows)
 
 ##### Non-conda users 
 

If you are experienced in python and do not use conda, the `requirements.txt` file is available also in the `setup/` directory for pip installation. This was our environment frozen as is for a Mac. If using Windows or Linux, you may need to remove some of the version requirements. 
 
#### 3. Enable `ipywidgets`

 We will be using widgets to create interactive visualizations. They will have been installed during your environment setup but you still need to run the following from the commandline: 
 
```bash
jupyter nbextension enable --py --sys-prefix widgetsnbextension
```
 
#### 4. Test your python environment 
 
 Now that your environment is set up, let's check that it works. 
 
 1. Go to the `setup/` directory from the command line and start a Jupyter notebook instance: 
 
```bash
jupyter notebook
```

a lot of text should appear -- you need to leave this terminal running for your Jupyter instance to work.

 2. Assuming this worked, open up the notebook titled `test-my-environment.ipynb`

 3. Once the notebook is open, go to the `Cell` menu and select `Run All`. 
 
 4. Check that every cell in the notebook ran (i.e did not produce error as output). `test-my-environment.html` shows what the notebook should look like after running. 
 

