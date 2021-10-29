### Steps:

#### Metadata Extraction Steps:

 - First install db server (I used mysql)
 - run python setup.py --schema
 - create necessary dirs under root dir to store files, the pdf files which need to be analyzed
should be stored in pdf dir.
 - specify which labels to extract and their corresponding configurations
or key, value pairs, see, labels.json file.
 - run python setup.py

#### New Metadata Learning and Extraction Steps:

- While extracting data from pdf at last step, you can specify is_test flag = 1
in labels.json so to mark that document to be used to 
test the regressor if it extracts correctly the values 
from similar fields.
- You should create a model.json file and put that inside model
dir where you specify model configs [Need to find how it looks like],
take help from original README file.
- Run train.py which finds the candidates (or features, or fields, e.g. "Patient Name") and their values from the 
extracted data stored in db, save it in csv folder (for later training and avoiding extracting
feature name and values from the scratch).
- The model will be saved in model folder, the model can be tested
using scripts in test folder.

#### Questions:

- How that learned model is used later? -- See 
schema.py to get more insight, roughly it seems that
it uses an already learnt model to identify a member of
predefined field at settings file.

