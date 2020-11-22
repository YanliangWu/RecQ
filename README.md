# CSIT 5210 Project 

[Incomplete] This is the code base forked from 

## Environment Setup

### MacOS/Linux

Since this repository is still using python 2 and tensorflow 1, we need some extra configuration to make this work. Follow these steps to setup your envirnoment:
1. Install anaconda https://www.anaconda.com/products/individual

2. Open anaconda navigator (Not the terminal)
    1. Click "Environments"
    2. Click "Import"
    3. Select file "environment.yaml" in this directory and click "Import"
    
3. After everything is done, open your newly created environment and launch a terminal

4. Go to `/main` and execute 
    ```
    python main.py
    ```
    
5. Select D5/D7 model to check running status

### Windows

Open anaconda navigator (Not the terminal)

1. Click "Environments"
2. Click "Import"
3. Select file "environment.yaml" in this directory and click "Import"

Use `pip install` to install tensorflow packages in `./tensorflow` package. 

1. After everything is done, open your newly created environment and launch a terminal

2. Go to `/main` and execute 

   ```
   python main.py
   ```

3. Select D5/D7 model to check running status


### Dataset Preprocessing
If you want to preprocess data to train negative datasets, use the script in `tool/negativeReview.py` 

## Things to notice before training the models 
### RSGAN 
If you want to run new dataset on RSGAN model, you need to manually create a negative review set before feeding it to training model. For example, for douban dataset, any data that is under rating 3 is consider as negative review. Name the file as `[model]_n.txt` and put it to the same directory with original rating data. 