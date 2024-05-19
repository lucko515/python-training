# Anaconda Ecosystem Cheatsheet

## Installation

### Installing Anaconda
Download the Anaconda installer from the [official website](https://www.anaconda.com/products/distribution) and follow the instructions for your operating system.

### Installing Miniconda
Download Miniconda from the [official website](https://docs.conda.io/en/latest/miniconda.html) if you prefer a smaller installation and only want the essentials.

## Conda Commands

### Environment Management

#### Create a New Environment
```sh
conda create --name myenv
```

#### Create a New Environment with Specific Packages
```sh
conda create --name myenv python=3.8 numpy pandas
```

#### Activate an Environment
```sh
conda activate myenv
```

#### Deactivate an Environment
```sh
conda deactivate
```

#### List All Environments
```sh
conda env list
```

#### Remove an Environment
```sh
conda remove --name myenv --all
```

### Package Management

#### Install a Package
```sh
conda install package_name
```

#### Install a Specific Version of a Package
```sh
conda install package_name=1.2.3
```

#### Install Multiple Packages
```sh
conda install package1 package2 package3
```

#### Update a Package
```sh
conda update package_name
```

#### Update Conda
```sh
conda update conda
```

#### List Installed Packages
```sh
conda list
```

#### Remove a Package
```sh
conda remove package_name
```

#### Search for a Package
```sh
conda search package_name
```

### Sharing Environments

#### Export an Environment to a YAML File
```sh
conda env export > environment.yml
```

#### Create an Environment from a YAML File
```sh
conda env create -f environment.yml
```

## Jupyter Notebooks

### Installing Jupyter Notebook
```sh
conda install jupyter
```

### Running Jupyter Notebook
```sh
jupyter notebook
```

### Installing JupyterLab
```sh
conda install -c conda-forge jupyterlab
```

### Running JupyterLab
```sh
jupyter lab
```

## Conda-Forge

### Using Conda-Forge
Conda-Forge is a community-maintained collection of packages. To install packages from Conda-Forge, use the `-c conda-forge` flag.

#### Example
```sh
conda install -c conda-forge package_name
```

### Setting Conda-Forge as Default Channel
```sh
conda config --add channels conda-forge
conda config --set channel_priority strict
```

## Anaconda Navigator

Anaconda Navigator is a graphical user interface for managing your Conda environments and packages.

### Launching Anaconda Navigator
```sh
anaconda-navigator
```

## Additional Resources

- [Conda Documentation](https://docs.conda.io/projects/conda/en/latest/index.html)
- [Anaconda Documentation](https://docs.anaconda.com/)
- [Conda-Forge Documentation](https://conda-forge.org/docs/)
