#!/usr/bin/env python
# -*- coding: utf-8 -*-

import usb
import struct
import cStringIO
import sys
import os
import time
"""
base on pyusb 0.4:
    https://pyusb.svn.sourceforge.net/svnroot/pyusb/branches/0.4/tests/pytest.py

Author:
    caicry@gmail.com

date: 
    2012-03-24
    
thanks for dnw tools info:
    http://www.linuxidc.com/Linux/2012-01/51071.htm
    http://www.arm9board.net/wiki/index.php?title=Dnw4Linux
    http://code.google.com/p/supervivi-transfer-tool

LICENSE:
    GPLV2
"""
class DNWError(Exception):
    def __init__(self, value):
        self.value = value
        
    def __str__(self):
        return repr(self.value)
        
        
class DNW():
    MINI2440_idVendor=0x5345
    MINI2440_idProduct=0x1234
    def __init__(self, idVendor = 0x5345, idProduct = 0x1234, address=0x30000000, debug=False, progress_func=None):
        self.idVendor = idVendor
        self.idProduct = idProduct
        self.address = address
        self.devhandle = False
        self.progress_func = progress_func

        # find device
        dev = self.GetDev()
        if dev == None:
            raise DNWError("Can't Found USB, Vendor:%X Product:%X" %(idVendor, idProduct))
        self.devhandle = dev.open()
        self.devhandle.claimInterface(0)

    def __del__(self):
        if self.devhandle:
            del self.devhandle


    def GetDev(self, debug=None):
        for bus in usb.busses():
            for dev in bus.devices:
                if debug:
                    print "  idVendor: %d (0x%04x) idProduct: %d (0x%04x)" % (dev.idVendor, dev.idVendor, dev.idProduct, dev.idProduct)
                if (dev.idVendor == self.idVendor and
                    dev.idProduct == self.idProduct):
                    return dev
        return None

    def calc_checksum(self, data):
        sum = 0
        for i in data:
            sum += struct.unpack('B', i)[0]
        sum = ((sum << 16)>> 16)
        return sum & 0xffff

    def OnProgress(self, progress):
        """
        progress = (totalen, l, speed, progress)
        """
        if self.progress_func:
            self.progress_func(progress)

    def DownloadFile(self, path, endpoint=0x3):
        """
        dnw protocol
        [4 byte address] + [4 byte length] + [data] + [2 byte chksum]
        NOTE: unsigned long 8 bit in AMD64 and 4 bit in X86
        """
        content = open(path).read()
        address = struct.pack("I", self.address)
        length = struct.pack("I", len(content)+10)
        checksum = struct.pack("H", self.calc_checksum(address + length + content))

        inp = cStringIO.StringIO(address + length + content + checksum)

        write_data = inp.read(512)
        totalen = len(content) + 10
        l=0
        print "FileName:%s length:%d Byte" % (path, totalen)
        start_time = time.time()
        while write_data:
            l += len(write_data)
            self.devhandle.bulkWrite(endpoint, write_data, 1000)
           
            end_time=time.time() 
            progress = (l*100/float(totalen))
            speed = l/(end_time - start_time)/1024
            progress_data = (totalen, l, speed, progress)
            
            sys.stdout.write("\rTotalen:%d WriteLen:%d Speed:%.2f progress:%%%d "% (totalen, l, speed, progress))
            sys.stdout.flush()

            self.OnProgress(progress_data)
            write_data = inp.read(512)

        inp.close()
        print "\nDone.."
        
    def UploadFile(self, path, endpoint=0x81):
        """
        Upload Protocol
        dnw send first 0x10a0 byte Info:
        
        [ 0x20 Byte Nand Flash Info] + [0x18 Byte Upload Info]
        struct flashInfo {
          u32 type,
          u32 flags,
          u32 size,
          u32 erasesize,
          u32 oobblock,
          u32 oobsize,
          u32 ecctype,
          u32 eccsize,
        };
        
        struct backupInfo {
          u32 startaddress,
          u32 endaddress,
          u32 backupoob,
          u32 chekcbad,
          u32 backuptotalen,
          u32 resverd,
          u32 pktsize,
        }
        
                
        Backup Information:
           Start Addr       : 0x0
           End Addr         : 0x4000000
           bBackupOOB       : 1
           bCheckBad        : 1
           dwBackupTotalLen : 0x4200000
           dwReservedBlks   : 20
           dwEPInPktSize    : 32

        """
        if os.path.isfile(path):
            os.remove(path)
        info = self.devhandle.bulkRead(endpoint, 0x10a0, 2000)
        data = struct.unpack("16I", "".join("%c" % c for c in info[0:64]))
        totalen = data[12]
        uploadlen = 0
        
        f = open(path, "wb")
        start_time = time.time()
        while  uploadlen < totalen:
            data = self.devhandle.bulkRead(endpoint, 2048 * 8, 2000) 
            if len(data) == 0:
                break;
            for c in data:
                f.write("%c" % c)
            end_time = time.time()
            uploadlen += len(data)
            progress = uploadlen * 100 / float(totalen)
            speed = uploadlen / (end_time - start_time) / 1024
            sys.stdout.write("\rtotalen:%d uploadlen:%d progress:%%%d speed:%.2fKB" % (totalen, uploadlen, progress, speed))
            progress_data = (totalen, uploadlen, speed, progress)
            self.OnProgress(progress_data)
            
        # read again
        try:
            data = self. devhandle.bulkRead(endpoint, 2048 * 8, 2000)
        except:
            pass
        
        f.close()
        os.chmod(path, 077)
        print "Done" 


if __name__ == '__main__':
            
        
    if len(sys.argv) != 2:
        print "dnw.py file"
        sys.exit(1)
        
    dnw = DNW(debug=True)
    #dnw.DownloadFile(sys.argv[1])

    dnw.UploadFile(sys.argv[1])
