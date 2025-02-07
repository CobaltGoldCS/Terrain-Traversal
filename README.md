# Autonomous Terrain Traversal in Project Chrono

## Installing PyChrono
You must use anaconda (or miniconda) to install PyChrono. These steps will create a python environment with all required dependencies to run Project Chrono using python. This environment is ~6GB of disk space.
1. Install the <a href=https://www.anaconda.com/download>Anaconda</a> python distribution

2. Open a Git Bash terminal as administrator

3. Run `conda config --add channels https://conda.anaconda.org/conda-forge`

4. Run `conda create -n chrono-tt python=3.10.16 -y`

5. Run `source activate base` then `conda activate chrono-tt`

6. Run `./installDeps.sh`

7. Verify the installation was successful by running `python demo.py`