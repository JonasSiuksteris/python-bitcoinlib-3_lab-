from bitcoin.rpc import RawProxy

p = RawProxy()

print('Enter transaction ID:')
txid = input()

#IDs for reference :
#"4410c8d14ff9f87ceeed1d65cb58e7c7b2422b2d7529afc675208ce2ce09ed7d"
#"0627052b6f28912f2703066a912ea577f2ce4da4caa5a5fbd8a57286c345c2f2"

raw_tx = p.getrawtransaction(txid)

decoded_tx = p.decoderawtransaction(raw_tx)

outvalue = 0
for output in decoded_tx['vout']:
    outvalue = outvalue + output['value']

invalue = 0
for input in decoded_tx['vin']:
    raw_txin = p.getrawtransaction(input['txid'])
    decoded_txin = p.decoderawtransaction(raw_txin)
    vout = decoded_txin['vout']
    invalue = invalue + vout[input['vout']]['value']

print(invalue - outvalue)