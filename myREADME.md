### Steps

#### Metadata Extraction Steps:

 - First install db server (I used mysql)
 - run python setup.py --schema
 - create necessary dirs under root dir to store files, the pdf files which need to be analyzed
should be stored in pdf dir.
 - specify which labels to extract and their corresponding configurations
or key, value pairs, see, labels.json file.
 - run python setup.py

#### TODO: New Metadata Learning and Extraction Steps:

- Figure out how candidate labels were generated from existing files and used for training 
unseen labels?
- Explore how "is_test" param works, current hypothesis is that, is_test flag defines
possible candidate document, needs testing.
