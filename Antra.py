from bitcoin.rpc import RawProxy
import hashlib
import sys
from struct import pack, unpack, unpack_from
from binascii import unhexlify


p = RawProxy()

print('Enter block height:')
blockheight = int(input())

#IDs for reference :
#"277316"
#"593468"
#"125552"

# Get the block hash of block with height 277316
blockhash = p.getblockhash(blockheight)

# Retrieve the block by its hash
block = p.getblock(blockhash)

version = pack('<I', block['version']).encode('hex_codec')

prev_hash = block['previousblockhash'].decode('hex')
prev_hash = prev_hash[::-1].encode('hex_codec')

merkle_root = unhexlify(block['merkleroot'])
merkle_root = merkle_root[::-1].encode('hex_codec')

timestamp = pack('<I', block['time']).encode('hex_codec')

bits = pack('<I', int(block['bits'], 16)).encode('hex_codec')

nonce = pack('<I', block['nonce']).encode('hex_codec')


header_hex = (version + prev_hash + merkle_root + timestamp + bits + nonce)
headerByte = header_hex.decode('hex')
hash = hashlib.sha256(hashlib.sha256(headerByte).digest()).digest()
hash = hash[::-1].encode('hex_codec')

print(hash)

if hash == block['hash']:
    print("hash is correct")
else:
    print("hash is incorrect")