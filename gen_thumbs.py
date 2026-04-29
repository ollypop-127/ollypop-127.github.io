import struct, zlib, os

def make_png(width, height, r, g, b):
    def chunk(name, data):
        c = zlib.crc32(name + data) & 0xffffffff
        return struct.pack('>I', len(data)) + name + data + struct.pack('>I', c)

    ihdr = struct.pack('>IIBBBBB', width, height, 8, 2, 0, 0, 0)
    raw = b''
    for y in range(height):
        raw += b'\x00' + bytes([r, g, b] * width)
    idat = zlib.compress(raw)

    return b'\x89PNG\r\n\x1a\n' + chunk(b'IHDR', ihdr) + chunk(b'IDAT', idat) + chunk(b'IEND', b'')

thumbs = {
    'gdi.png':      (180, 100, 80),
    'cs.png':       (80, 120, 180),
    'vm.jpeg':      (160, 140, 100),
    'green.png':    (80, 160, 80),
    'bomb.png':     (200, 80, 80),
    'love.png':     (180, 80, 120),
    'nba.jpeg':     (80, 80, 200),
    'larb.jpg':     (200, 160, 80),
    'tni.jpg':      (120, 80, 160),
    'eotb.png':     (100, 180, 180),
    'sp.jpeg':      (100, 160, 200),
    'vp.png':       (180, 120, 60),
    'closet.png':   (220, 160, 180),
    'sheet.png':    (160, 200, 120),
    'playlist.png': (120, 160, 220),
    'records.png':  (80, 80, 80),
    'matrix.png':   (60, 100, 160),
    'tamu.png':     (80, 0, 0),
}

os.makedirs('thumbs', exist_ok=True)
for name, (r, g, b) in thumbs.items():
    path = f'thumbs/{name}'
    with open(path, 'wb') as f:
        f.write(make_png(48, 30, r, g, b))
    print(f'  {path}')

print("Done!")
