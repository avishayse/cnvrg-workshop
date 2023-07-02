# :rocket: **Setup Instructions**

## :penguin: **Windows Subsystem for Linux (WSL)**

1. Update the WSL: 
    ```bash
    wsl --update
    ```
2. List the WSL distributions: 
    ```bash
    wsl --list -o
    ```
3. Set the default WSL version: 
    ```bash
    wsl --set-default-version 1
    ```
4. Install Ubuntu: 
    ```bash
    wsl --install -d Ubuntu
    ```
5. Boot Ubuntu: 
    ```bash
    wsl -d Ubuntu
    ```

## :snake: **Python Installation**

1. Install required software: 
    ```bash
    sudo apt install software-properties-common
    ```
2. Add Python PPA: 
    ```bash
    sudo add-apt-repository ppa:deadsnakes/ppa
    ```
3. Update the system: 
    ```bash
    sudo apt update
    ```
4. Install Python 3.10: 
    ```bash
    sudo apt install python3.10
    ```
5. Install pip for Python 3: 
    ```bash
    sudo apt install python3-pip
    ```

## :gear: **cnvrgv2 Installation**

1. Install cnvrgv2: 
    ```bash
    pip install cnvrgv2
    ```
2. :warning: **Note:** Close the terminal and start again to load the home environment.

## :key: **cnvrg Login**

1. Login to cnvrg: 
    ```bash
    pip install cnvrgv2 login -d https://app.amkxwwqhc3fyyo9din8cvnd.cloud.cnvrg.io -t <token> -e <email>
    ```

## :file_folder: **cnvrg Dataset Creation**

1. Create a dataset: 
    ```bash
    cnvrgv2 dataset create --name=test_dataset
    ```
2. Navigate to your local state and run the command: 
    ```bash
    cnvrgv2 dataset put -f ./test_dataset/
    ```

:checkered_flag: **Done.**
