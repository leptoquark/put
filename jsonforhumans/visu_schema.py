from json_schema_for_humans.generate import generate_from_filename
from json_schema_for_humans.generation_configuration import GenerationConfiguration
from os.path import join, basename
from glob import glob

WORK_DIR = '../schemi'
SCHEMA_FILE = "art4-bis-v1.0.0.schema.json"
OUTPUT_FILE = "index.html"

config = GenerationConfiguration(copy_css=False, expand_buttons=True)

# generate_from_filename(join(WORK_DIR, SCHEMA_FILE), join(WORK_DIR, OUTPUT_FILE), config=config)

for fpath in glob(join(WORK_DIR, "*.json")):
    print(f"{fpath}")
    ofile = join(WORK_DIR, basename(fpath).replace('.json', '.html'))
    generate_from_filename(fpath, ofile, config=config)
    print (ofile)