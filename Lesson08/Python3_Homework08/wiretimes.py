import struct
from datetime import datetime
f = open('wireshark.bin', 'rb')
f.seek(24) # To ignore header of the File ( 6 * 4bytes each)
result = []
while True:
    try:
        # result will store first and second values of the packet (each of 4 bytes)
        result.append((struct.unpack('I', f.read(4))[0], struct.unpack('I', f.read(4))[0]))
        f.read(4) # move 4 bytes ahead ignoring incl_len
        f.seek(f.tell()+4+struct.unpack('I', f.read(4))[0]) # move forward the length of the packet bytes to reach start of the next packet.
    except struct.error:
        break
f.close()
#print(result)
for i, k in result:
    print(datetime.fromtimestamp(i).strftime('%Y-%m-%d %H:%M:%S'), k)
