import pexpect
from itertools import permutations

name = "david"

for perm in range(1000):

    p = pexpect.spawn("./access")

    p.expect("Please enter your name:\r\n")

    p.sendline(name)

    p.expect(name + ", please enter your PIN:\r\n")

    p.sendline(str(perm) + '8')

    p.readline()

    result = p.readline()

    print(result)

    if 'Success' in str(result):
        print(str(perm) + '8')
        break
