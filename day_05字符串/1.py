zfc=input('please input:')
sz=0
zm=0
ts=0
for i in zfc:
    if zfc.isdigit():
        sz+=1
    elif zfc.isalnum():
        zm+=1
    else:
        ts+=1
print(f'sz:{sz}zm:{zm}ts:{ts}')

