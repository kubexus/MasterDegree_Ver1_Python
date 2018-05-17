import serial


def test_nlfsr(state, x):
    period = 2**len(state) - 1
    initial = state[:]
    i = 0
    while True:
        i += 1
        feedback = int(state[0]) ^ (int(state[x[0]]) & int(state[x[1]])) ^ int(state[x[2]]) ^ int(state[x[3]]) ^ int(state[x[4]]) ^ int(state[x[5]])
        state = state[1:] + str(feedback)
        if state == initial:
            break
        if i > period:
            break
    if i == period:
        return True
    else:
        return False


def change(x):
    for i in range(0, 35):
        if x == bytes([i]):
            return i


if __name__ == '__main__':
    ser1 = serial.Serial('/dev/ttyUSB0', 115200)
    res_file = open('results', 'w')
    while True:
        out = ''
        x = ser1.read(1)
        if x == bytes([0xff]):
            while True:
                x = ser1.read(1)
                if x == bytes([0xfe]):
                    out += '\n'
                    break
                out += str(change(x))
                out += ' '
        res_file.write(out)
        res_file.flush()