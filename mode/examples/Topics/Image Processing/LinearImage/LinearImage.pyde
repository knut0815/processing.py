"""
Linear Image.

Click and drag mouse up and down to control the signal.
Press and hold any key to watch the scanning.
"""
img = loadImage("sea.jpg")
direction = 1
signal = 0.0


def setup():
    global img
    img = loadImage("sea.jpg")
    size(640, 360)
    stroke(255)
    img.loadPixels()
    loadPixels()


def draw():
    global signal, direction
    if signal > img.height - 1 or signal < 0:
        direction = direction * -1
    if mousePressed:
        signal = abs(mouseY % img.height)
    else:
        signal += (0.3 * direction)
    if keyPressed:
        set(0, 0, img)
        line(0, signal, img.width, signal)
    else:
        signalOffset = int(signal) * img.width
        for y in range(img.height):
            listCopy(img.pixels, signalOffset, pixels, y * width, img.width)
        updatePixels()


def listCopy(src, srcPos, dst, dstPos, length):
    dst[dstPos:dstPos + length] = src[srcPos:srcPos + length]
