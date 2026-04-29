import struct, math, random, os

RATE = 44100

def write_wav(filename, samples):
    n = len(samples)
    data = struct.pack('<' + 'h' * n, *[max(-32768, min(32767, int(s))) for s in samples])
    with open(filename, 'wb') as f:
        f.write(b'RIFF')
        f.write(struct.pack('<I', 36 + len(data)))
        f.write(b'WAVE')
        f.write(b'fmt ')
        f.write(struct.pack('<IHHIIHH', 16, 1, 1, RATE, RATE * 2, 2, 16))
        f.write(b'data')
        f.write(struct.pack('<I', len(data)))
        f.write(data)

def boom():
    dur = 0.4
    n = int(RATE * dur)
    samples = []
    for i in range(n):
        t = i / RATE
        freq = 80 * math.exp(-t * 15)
        env = math.exp(-t * 8)
        samples.append(32000 * env * math.sin(2 * math.pi * freq * t))
    return samples

def chit():
    dur = 0.05
    n = int(RATE * dur)
    return [32000 * random.uniform(-1, 1) * math.exp(-i / n * 6) for i in range(n)]

def tick():
    dur = 0.08
    n = int(RATE * dur)
    samples = []
    for i in range(n):
        t = i / RATE
        env = math.exp(-t * 40)
        samples.append(32000 * env * (random.uniform(-1, 1) * 0.5 + math.sin(2 * math.pi * 400 * t) * 0.5))
    return samples

def tiss():
    dur = 0.2
    n = int(RATE * dur)
    return [32000 * random.uniform(-1, 1) * math.exp(-i / n * 3) for i in range(n)]

def clap():
    dur = 0.15
    n = int(RATE * dur)
    samples = []
    for i in range(n):
        t = i / RATE
        env = math.exp(-t * 20) + 0.3 * math.exp(-t * 8)
        samples.append(32000 * env * random.uniform(-1, 1))
    return samples

def bloop():
    dur = 0.3
    n = int(RATE * dur)
    samples = []
    for i in range(n):
        t = i / RATE
        freq = 300 * math.exp(-t * 5)
        env = math.exp(-t * 6)
        samples.append(32000 * env * math.sin(2 * math.pi * freq * t))
    return samples

os.makedirs('sounds', exist_ok=True)
write_wav('sounds/boom.wav', boom())
write_wav('sounds/chit.wav', chit())
write_wav('sounds/tick.wav', tick())
write_wav('sounds/tiss.wav', tiss())
write_wav('sounds/clap.wav', clap())
write_wav('sounds/bloop.wav', bloop())
print("Done!")
