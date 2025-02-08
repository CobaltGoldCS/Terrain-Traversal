#!/bin/bash

echo "conda install -c conda-forge mkl=2020 -y"
conda install -c conda-forge mkl=2020 -y

echo "conda install -c conda-forge numpy=1.24.0 -y"
conda install -c conda-forge numpy=1.24.0 -y

echo "conda install -c conda-forge irrlicht=1.8.5 -y"
conda install -c conda-forge irrlicht=1.8.5 -y

echo "conda install -c conda-forge pythonocc-core=7.4.1 -y"
conda install -c conda-forge pythonocc-core=7.4.1 -y

echo "conda install -c nvidia/label/cuda-11.7.0 cuda-toolkit -y"
conda install -c nvidia/label/cuda-11.7.0 cuda-toolkit -y

echo "conda install -c conda-forge glfw -y"
conda install -c conda-forge glfw -y

echo "conda install -c projectchrono pychrono -y"
conda install -c projectchrono pychrono -y

echo "conda install -c conda-forge pythonocc-core=7.8.1 -y"
conda install -c conda-forge pythonocc-core=7.8.1 -y
