import unittest


def isInNetblock(ipaddr, netblock):
    ipaddr = isIPAddress(ipaddr)
    netip, mask = isNetblock(netblock)
    if not ipaddr or not netblock:
        raise
    if ipaddr & mask == netip & mask:
        return True
    return False

def isIPAddress(ipaddr):
    abcd = ipaddr.split('.')
    result = []
    if len(abcd) != 4:
        return False
    for a in abcd:
        try:
            i=int(a)
        except ValueError:
            return False
        if i <0 or i > 255:
            return False
        result.append(i)
    return convert(result)

def isNetblock(netblock):
    unfold = netblock.split('/')
    if len(unfold) !=2:
        return False
    ipaddr = isIPAddress(unfold[0])
    if not ipaddr:
        return False
    try:
        mask = int(unfold[1])
    except ValueError:
        return False
    if mask < 0 or mask > 32:
        return False
    return (ipaddr, convertmask(mask))

def convert(ipaddr):
    return (ipaddr[0]<<24) + (ipaddr[1]<<16) + (ipaddr[2]<<8) + ipaddr[3]

def convertmask(mask):
    return (2**32-1)^(2**(32-mask)-1)

class simpletest(unittest.TestCase):
    def setUp(self):
        pass
    
    def testisNetblock(self):
        tests = {
            '1.1.1.1/24': (16843009, 4294967040),
            'abc.123.43.5/2/3': False,
            '1.1.1.1.1/32': False,
            }
        for k,v in tests.iteritems():
            self.assertEqual(isNetblock(k), v)
    
    def testisIPAddress(self):
        tests = {
            '1.1.1.1': 16843009,
            'abc.123.43.5': False,
            '1.1.1.1.1': False,
            }
        for k,v in tests.iteritems():
            self.assertEqual(isIPAddress(k), v)

    # def testconvert(self):
        

    def testisInNetblock(self):
        self.assertEqual(isInNetblock('192.168.1.1', '192.168.1.2/24'), True)

if __name__ == '__main__':
    unittest.main()