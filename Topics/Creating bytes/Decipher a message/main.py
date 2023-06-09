original_message = input()
original_key = int(input())

message_temp = original_message.encode()
key_temp = original_key.to_bytes(2, byteorder='little')
key_bytes = key_temp[0] + key_temp[1]

message = []

for _, number in enumerate(message_temp):
    message.append(number + key_bytes)

int_to_bytes = bytes(message)

message_decoded = int_to_bytes.decode('utf-8')
print(message_decoded)
