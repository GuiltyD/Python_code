from struct import Struct
record_struct = Struct('<iii')
with open('text.bin','rb') as f:
    chunks = iter(lambda :f.read(record_struct.size),b'')
    print(tuple(record_struct.unpack(chunk) for chunk in chunks))
