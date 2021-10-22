### I followed the following steps to run this

####Metadata Extraction Steps:
 - First install mysql server
 - run python setup.py --schema
 - create necessary dirs to store files, the pdf files which need to be analyzed
should be stored in pdf dir.
 - specify which labels to extract and their corresponding configurations
or key, value pairs, see, labels.json file.
 - run python setup.py

####New Metadata Learning and Extraction Steps:

- Figure out how, candidate labels were generated from existing files and used for training 
unseen labels?
- Try with a dummy file which has possible candidates and see if extracted data from it is stored 
in the intended columns in document table.
- Explore how "is_test" param works, current hypothesis is that, is_test flag defines
possible candidate document, needs verification!
