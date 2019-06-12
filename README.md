# Fantasy Name Generator
A Python 3 script to train a recurrent neural network on a corpus of fantasy creature names and generate new names from that corpus. It uses textgenrnn and is heavily inspired by [Max Woolf's](http://minimaxir.com/) [pokemon-ai repo](https://github.com/minimaxir/pokemon-ai). The dataset comes from the [pathfinder SRD](http://www.d20pfsrd.com/bestiary/tools/monster-filter).

The name of this repo is technically a misnomer. You can use any dataset you want, so really this could be a name generator for anything! 

Just have a csv with a Name column in the data folder, set the parameters (mainly model name and paths) in the ..._config.py files at the top of the directory, and run fantasycreature_training.py and fantasycreature_generate.py. The former will create the model and output the weights, vocab, and model parameters and store them in the config folder, and the latter will generate 100 names from the model outputted into a text file at the top of the directory.

I wrote this code in windows, and was running into some bugs when trying to run the code in the git bash terminal, but when running through a python interpreter it works fine.

### Requirements
This repo requires the pandas and textgenrnn packages to be installed in python 3. Textgenrnn also has requirements that must be met.

### Usage
1. Use the provided dataset or place your own .csv file with a Name column in the data folder.
2. Change the parameters in fantasycreature_pretrain_config.py and fantasycreature_generate_config.py.
3. Run the fantasycreature_training.py script from the main directory in a python interpreter to train the model.
4. Run the fantasycreature_generate.py script from the main directory in a python interpretor to generate 500 names.

### Limitations
At least on my windows machine, the code does not seem to run properly when called in a git bash terminal.

Besides changing the dataset and path information in the configurations script, all other changes, such as parameter changes to the model, must be made in the training script.
