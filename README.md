# Ideityfy app
> Where is your god now?
Show this app a deity and it will tell you who your god is.  
Currently this only works with 
1. God of mercy
2. Monkey god
3. Happy god

# This project consists of 4 steps
## 1. Collection phase
move to the preprocessor directory  
`cd preprocessor`  
download using command  
`googleimagesdownload -cf google_download_config.json`  
prepare processed dataset by running through the process_images.ipynb notebook

## 2. Training phase
Trainig is performed on google cloud using a K80 GPU.  
Training was done through transfer learning using the ResNet-50 model with the last layer retrained to classify the new categories.  
code to train the model is at /preprocess/run_transfer_model.py  
results from validation is at /preprocess/transfer_learning_output.txt The model had a test accuracy of 73%.

## 3. App phase
Requirements for launching on heroku can be found in requirements.txt. The CPU version of PyTorch was specified because the GPU version was too large (heroku has a limit of 500mb). The code to run the app is in app.py, and model code in src/ideityfier.py.
