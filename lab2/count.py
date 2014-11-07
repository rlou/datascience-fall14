import pandas as pd
import avro
from avro.datafile import DataFileReader, DataFileWriter
from avro.io import DatumReader, DatumWriter
reader = DataFileReader(open("countries.avro", "r"), DatumReader())

countries = pd.DataFrame.from_records(reader)

temp = countries[countries['population']>10000000]
count = temp['name'].count()

print count
