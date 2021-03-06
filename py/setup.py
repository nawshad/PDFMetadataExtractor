from settings import Settings
from argparse import ArgumentParser
from extract import extract_pdf_data
from pdf_classes import *
import os


if __name__ == "__main__":
    parser = ArgumentParser(description='Set up database')
    parser.add_argument('--schema', help='install the schema', action='store_true')
    parser.add_argument('--settings', help='the path to the settings file',
                           default=None)

    args = parser.parse_args()
    settings = Settings(args.settings)
    metadata = settings.map_tables()


    if args.schema:
        #Just install the schema.
        metadata.create_all(settings.engine())
    else:
        #Extract all of the PDFs in the pdf directory to the database.
        session = settings.session()
        pdf_dir = settings.get_directory('pdf')
        print("pdf_dir:", pdf_dir)
        existing = [fn[0] for fn in session.query(Document.filename)]
        print("Existing:", existing)
        labels = settings.load_labels()
        print("labels:", labels)
        for filename in os.listdir(pdf_dir):
            if filename not in existing:
                file_labels = labels.get(filename, {})
                try:
                    with open(os.path.join(pdf_dir, filename), "rb") as fp:
                        print("Document", extract_pdf_data(fp, settings.test_proportion, file_labels, session))
                except Exception as e:
                    session.rollback()
                    print (filename, e)

        #query=Document.update().values(Document.is_test=1)

