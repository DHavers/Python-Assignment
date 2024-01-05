#E.coli Protein Secretion Prediction

This is a project created in python that can be used to predict which E. coli protein secretion system (or none at all) are used for a protein based on its amino acid sequence. This can be applied in research when trying to design constructs for secretion via a particular system, to validate the designed sequence before time and money are spent producing it. Additionally this code could be adapted for other organisms secretion systems if an appropriate method of categorising the different proteins to a secretion system in the training set can be achieved. 

To run: 
	1. Download the python script in this repository along with the E. coli example data via this URL: https://github.com/DHavers/Python-Assignment
	2. Run the programme and edit the input sequence in section for "lab_sequence" to your sequence of interest to gain insight into what secretion system this protein is likely to use
	3. If investigating a different organism be sure to input different datasets to train the model, and alter the motif search to identify the respective secretion systems before progressing through the pipeline to prediction

Library installations

To run this project, you need to install following dependencies:
	- pandas 
	- matplotlib 
	- biopython
	- scikit-learn
	- seaborn

You can installing them using the following command:
```bash 
pip install pandas matplotlib biopython scikit-learn seaborn
```bash
Library details: 
	- pandas (import pandas as pd): enables efficient data manipulation and analysis by providing data structures like DataFrame
	- matplotlib (import matplotlib.pyplot as plt): can be used to create visulisations in python
	- Biopython (from Bio.SeqUtils import ProtParam): a collection of biological computation tools, including functions for working with protein sequences 
	- Scikit-learn (from sklearn.ensemble import RandomForrestClassifier, from sklearn.model_selection import train_test_split, from sklearn.metrics import accuracy_score): a machine learning library that provides tools for data analysis 
	- seaborn (import seaborn as sns): a statistical data visulisation tool 
	- numpy (import numpy as np): a useful package for computing in python, supporting large arrays and matrices and mathmatical functions 

