# River Trash Detection <!-- omit in toc -->

Trash detection and navigation done using NVIDIA Jetson Nano.

- [Setting up Jetson Nano](#setting-up-jetson-nano)
  - [JupyterLab](#jupyterlab)
  - [Connect to Wi-Fi](#connect-to-wi-fi)
  - [Install TensorFlow 2](#install-tensorflow-2)
  - [Re-train the model (if needed)](#re-train-the-model-if-needed)
  - [Classifying images](#classifying-images)
- [Setting up on Windows](#setting-up-on-windows)
  - [Re-train the model (if needed)](#re-train-the-model-if-needed-1)
  - [Classifying images](#classifying-images-1)

## Setting up Jetson Nano

1. Connect Jetson Nano to 5V DC input through the mains.
2. Switch on the power.
3. Connect the microUSB cable to the computer.

### JupyterLab

1. Wait for about 30 to 60 seconds.
2. Navigate to http://192.168.55.1:8888.

### Connect to Wi-Fi

1.  Open the terminal.
2.  Find the list of available Wi-Fi networks.

        nmcli d wifi list

3.  To connect to the access point 'hmm', use the following command:

        nmcli d wifi connect hmm password pwpw

### Install TensorFlow 2

1.  Install and upgrade to the latest version of pip.

        pip install --upgrade pip

2.  Install system packages required by TensorFlow:


        sudo apt-get update
        sudo apt-get install libhdf5-serial-dev hdf5-tools libhdf5-dev zlib1g-dev zip libjpeg8-dev liblapack-dev libblas-dev gfortran

3.  Install and upgrade `pip3`.

        sudo pip3 install -U pip testresources setuptools

4.  Install the Python package dependencies.

        sudo pip3 install -U numpy==1.16.1 future==0.17.1 mock==3.0.5 h5py==2.9.0 keras_preprocessing==21.0.5 keras_applications==1.0.8 gast==0.2.2 futures protobuf pybind11

### Re-train the model (if needed)

1.  Navigate to the folder with the repository and run the following command:

        bash train.sh

### Classifying images

1.  Unzip `training_dataset.zip` and place it within the repository's folder.
2.  Open any Python terminal.
3.  Navigate to the folder with the respository and run the following command:

        python classify_list.py

4.  `classify_list.py` is a Python script which runs a loop to classify 30 images, from `testing1.jpg` to `testing30.jpg`
5.  The classification results will appear in the terminal as they are completed.

## Setting up on Windows

1.  Open any Python terminal.
2.  Install TensorFlow.

        pip install tensorflow

3.  Git clone this repository and navigate to the folder with the repository.

### Re-train the model (if needed)

1.  If you have Git installed, navigate to the folder with the repository and run the following command:

        train.sh

2.  Otherwise, run Windows PowerShell as Administrator.
3.  Type the following command to allow scripts to run and press Enter:

        Set-ExecutionPolicy RemoteSigned

4.  Type A and press Enter (if applicable).
5.  Navigate to the folder with the respository and run the following command:

        .\train.sh

### Classifying images

1.  Unzip `training_dataset.zip` and place it within the repository's folder.
2.  Open any Python terminal.
3.  Navigate to the folder with the respository and run the following command:

        python classify_list.py

4.  `classify_list.py` is a Python script which runs a loop to classify 30 images, from `testing1.jpg` to `testing30.jpg`
5.  The classification results will appear in the terminal as they are completed.
6.  The results of the classification would be written to `Outputs.txt`.
