from scalecodec.type_registry import load_type_registry_file
from substrateinterface import SubstrateInterface

substrate = SubstrateInterface(
    url='ws://161.97.148.207:7949',
    type_registry=load_type_registry_file('app/type_registry/custom_types.json'),
)

# block_hash = substrate.get_chain_finalised_head()
block_hash = '0x3a00e167626324048e63034906df81b8a6c1402abcdc5f8ffa1b3ed045e3c048'

extrinsics = substrate.get_block_extrinsics(block_hash=block_hash)
print('Extrinsics:', [extrinsic.value for extrinsic in extrinsics])

events = substrate.get_events(block_hash)
print("Events:", events)

#print("Metadata: ",substrate.get_block_metadata(block_hash=block_hash))
print("Metadata: ",substrate.get_block_runtime_version(block_hash))
