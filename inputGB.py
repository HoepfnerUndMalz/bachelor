#using Biophyton package for parsing GenBank files

from Bio import SeqIO
from Bio import GenBank

file_path = 'input/pc-0.gb'
genbank_object = SeqIO.read(file_path, 'gb')
print(genbank_object.id)

record_id = genbank_object.id
print(record_id)

record_name = genbank_object.name
print(record_name)

record_seq = genbank_object.seq
sequence_length = len(record_seq)
print(record_seq)
print(sequence_length)

record_description = genbank_object.description
print(record_description)

annotations = genbank_object.annotations
print(annotations)

# features of genome
features = genbank_object.features
print(features)
feature_types = [f.type for f in features]
print(feature_types)
feature_types2 = [feature.type for feature in features]
print(feature_types2)
feature_types2 = set(feature_types2)
feature_types2 = list(feature_types2)
print(feature_types2)

#feature location
feature_locations = [f.location for f in features]
print(feature_locations)

# print feature and location for promoter
promoter_index = feature_types.index('promoter')
promoter_location = feature_locations[promoter_index]
#print(promoter_index)
print(promoter_location)


promoter_index = feature_types.index('source')
promoter_location = feature_locations[promoter_index]
#start has to be raised by 1


print(type(promoter_location))
print(dir(promoter_location))
print(promoter_location)
print(promoter_location.start)
print(promoter_location.end)





# with open('input/pc-0.gb') as handle:
#     for record in GenBank.parse(handle):
#         print(record.accession)

# file1 = open('input/pc-0.gb')
# print(file1.read())
