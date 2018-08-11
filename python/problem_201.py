'''
PBM is a simple file format for transmitting black and white images.  Initially there was the "plain" PBM format, which allows images to be specified entirely in printable characters, following this layout:

  * "P1\n" = magic number and newline.
  * "<width> <height>\n" = image dimensions in decimal, followed by newline.
  * List of integers describing the pixel values.  1 is black and 0 is white.

Here is an example of a 6x5 image (67 bytes):

P1
6 5
0 1 1 1 1 1
0 1 1 1 1 0
0 1 1 1 0 0
0 1 1 0 0 0
0 1 0 0 0 0

Since this plain text format is very inefficient, most people use the binary format instead, which follows this layout:

  * "P4\n" = magic number and newline.
  * "<width> <height>\n" = image dimensions in decimal, followed by newline.
  * List of bytes that describe the pixel values.  Most significant bit of the first byte specifies the leftmost pixel, 1 bit is black and 0 bit is white.
  * Bytes are padded with zero bits such that the start of each scanline always falls on byte boundary.

Here is the same image as the earlier example, but in binary (12 bytes):

P4
6 5
|xp`@

Note how the 5 rows are encoded in 5 bytes:
| = 0x7c = 0b01111100
x = 0x78 = 0b01111000
p = 0x70 = 0b01110000
` = 0x60 = 0b01100000
@ = 0x40 = 0b01000000


Given a plain PBM file, convert it to binary PBM.

http://netpbm.sourceforge.net/doc/pbm.html
'''

def g(a):
  z=a.split('\n');r='P4\n'+z[1]+'\n';c=z[2:]
  for b in c:r+=''.join([chr(int((b[i:i+16]+'0'*7).replace(' ','')[:8],base=2)) for i in range(0,len(b),16)])
  return r



def main():
    print(g("P1\n53 25\n0 1 1 1 1 1 0 1 0 1 1 1 1 0 1 1 0 1 1 1 0 1 1 1 0 1 1 1 0 1 1 1 0 1 1 1 1 1 0 1 0 1 1 1 1 1 0 1 0 1 1 1 1\n0 1 1 1 1 1 0 1 0 1 1 1 1 0 1 1 0 1 1 1 1 1 1 0 0 1 1 0 1 1 1 1 0 1 1 1 1 0 1 1 0 1 1 1 0 1 1 1 0 1 1 1 1\n0 1 1 1 1 1 1 0 0 1 0 1 1 1 1 1 0 1 1 1 1 1 0 1 0 1 1 1 0 1 1 1 0 1 1 1 0 1 1 1 0 1 1 1 1 0 1 1 0 1 1 1 1\n0 0 1 1 1 1 1 1 0 1 1 0 1 1 1 1 0 0 1 1 1 1 1 1 0 1 1 1 1 0 1 1 0 1 1 1 1 1 0 1 0 1 1 1 1 1 1 0 0 1 1 1 1\n0 1 0 1 1 1 1 1 0 1 1 0 1 1 1 1 0 1 1 1 0 1 1 1 0 1 0 1 1 1 1 1 0 0 1 1 1 1 1 1 0 1 1 0 1 1 1 1 0 1 1 1 1\n0 0 1 1 1 1 1 1 0 1 0 1 1 1 1 1 0 1 1 1 0 1 1 1 0 0 1 1 1 1 1 1 0 0 1 1 1 1 1 1 0 1 1 0 1 1 1 1 0 1 1 1 1\n0 1 1 1 1 0 1 1 0 1 1 1 1 1 1 0 0 1 1 1 1 1 0 1 0 1 1 1 1 1 1 0 0 0 1 1 1 1 1 1 0 1 1 1 1 0 1 1 0 1 1 1 1\n0 1 1 1 1 1 1 0 0 1 1 1 1 1 1 0 0 0 1 1 1 1 1 1 0 1 1 1 1 1 0 1 0 1 1 1 1 1 0 1 0 1 1 1 1 1 0 1 0 1 1 1 1\n0 1 1 1 1 1 0 1 0 1 0 1 1 1 1 1 0 1 1 1 1 1 0 1 0 1 1 1 1 1 1 0 0 1 1 1 1 0 1 1 0 1 1 1 1 1 1 0 0 1 1 1 1\n0 1 1 1 1 0 1 1 0 1 1 1 1 1 1 0 0 1 1 1 1 1 0 1 0 1 1 1 1 1 1 0 0 0 1 1 1 1 0 1 0 1 1 1 1 1 1 0 0 1 1 1 1\n0 1 1 1 0 1 1 1 0 1 1 1 0 1 1 1 0 0 1 1 1 1 1 1 0 1 1 0 1 0 1 1 0 1 0 1 1 1 1 1 0 0 1 1 1 1 1 1 0 1 1 1 1\n0 1 1 1 1 1 0 1 0 0 1 1 1 1 1 1 0 1 1 1 0 1 1 1 0 1 1 1 1 1 1 0 0 1 1 1 1 1 0 1 0 1 0 1 1 1 1 1 0 1 1 1 1\n0 1 1 1 0 1 1 1 0 1 1 1 1 1 1 0 0 1 1 1 1 1 1 0 0 1 1 1 0 1 0 0 0 0 1 0 0 0 1 0 0 1 1 1 0 1 1 1 0 1 1 1 1\n0 1 1 1 1 1 1 0 0 1 0 1 1 1 1 1 0 1 1 1 1 1 0 1 0 1 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 1 0 1 1 1 1 0 1 1 1 1\n0 0 1 1 1 1 1 1 0 1 1 0 1 1 1 1 0 1 1 1 1 1 1 0 0 1 0 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 1 0 1 0 1 1 0 1 1 1 1\n0 1 1 1 1 1 1 0 0 1 1 1 0 1 1 1 0 1 1 1 1 1 0 0 0 0 1 0 0 0 0 0 0 1 0 0 1 1 0 0 0 1 0 0 0 0 1 1 0 1 1 1 1\n0 1 1 1 1 1 1 0 0 1 1 1 0 1 1 1 0 1 1 1 0 0 0 0 0 0 1 0 0 0 1 0 0 0 1 0 0 0 0 1 0 1 0 1 0 1 0 1 0 1 1 1 1\n0 1 1 1 1 1 0 1 0 1 1 1 0 1 1 1 0 1 1 1 0 0 0 0 0 1 0 0 1 0 0 0 0 0 1 0 0 1 0 0 0 1 0 0 0 1 0 0 0 1 1 1 1\n0 1 1 1 0 1 1 1 0 1 0 1 1 1 1 1 0 1 0 0 0 0 0 0 0 1 0 0 0 0 1 1 0 1 0 0 1 0 0 0 0 0 1 1 0 0 0 1 0 1 1 1 1\n0 1 1 1 1 1 1 0 0 1 1 1 1 1 1 0 0 1 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 1 0 0 1 0 0 0 0 1 1 1\n0 1 1 0 1 1 1 1 0 1 1 1 0 1 1 1 0 0 1 0 0 1 0 0 0 1 0 0 1 0 0 0 0 1 0 0 1 0 0 1 0 1 0 0 0 0 0 1 0 1 0 1 1\n0 1 1 1 0 1 1 1 0 1 1 1 1 1 0 1 0 1 0 0 1 0 0 0 0 1 0 0 0 0 0 0 0 1 0 0 0 0 1 0 0 0 1 0 0 0 0 0 0 1 0 1 1\n0 1 0 1 1 1 1 1 0 1 1 0 1 1 1 1 0 1 0 0 0 0 0 1 0 1 0 0 1 0 1 0 0 0 1 0 0 0 0 0 0 0 1 0 0 0 0 0 0 1 0 0 1\n0 1 1 1 1 1 1 0 0 1 1 1 1 1 1 0 0 1 0 0 0 0 1 0 0 1 0 0 0 0 0 0 0 1 0 0 0 0 1 0 0 0 1 0 1 0 0 0 0 0 1 0 1\n0 1 1 1 1 0 1 1 0 1 1 1 1 1 0 0 0 0 1 1 1 0 0 0 0 1 0 0 0 0 1 0 0 0 1 0 0 0 0 0 0 1 0 0 0 0 0 0 0 1 0 0 1\n"	))
    #print(g("P1\n6 5\n0 1 1 1 1 1\n0 1 1 1 1 0\n0 1 1 1 0 0\n0 1 1 0 0 0\n0 1 0 0 0 0\n"))



if __name__ == '__main__':
    main()