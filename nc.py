#!/usr/bin/env python
#
# description:
# minimalist netcat-like
# ./nc.py -i data.bin <server ip>
# ./nc.py -o foo.bin
#
# author:
# fab <fdevaux@wyplay.com>
#

import socket
import sys
from functools import partial

import itertools

def main():
    from optparse import OptionParser
    parser = OptionParser(usage = '%prog [server] <file option> [options]')
    parser.add_option("-i", dest="in_file",  default=None, help="read data from FILE", metavar="FILE")
    parser.add_option("-o", dest="out_file", default=None, help="write data to FILE", metavar="FILE")
    parser.add_option("-p", dest="port", default=2727, type='int', help="use port PORT", metavar="PORT")
    parser.add_option("-s", dest="chunk_size", default=4096, type='int', help="specify the size of chunks")
    parser.add_option("-c", dest="cycle", default=False, action="store_true", help="cycle mode: loop forever")
    (options, args) = parser.parse_args()

    in_file = options.in_file
    out_file = options.out_file

    if len(args) > 1 or bool(in_file) == bool(out_file):
        parser.error('Incorrect arguments, try --help')

    while True:
        if not args:
            # listen
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            sock.bind( ('', options.port))
            sock.listen(1)
            conn, addr = sock.accept()
        else:
            # connect
            SERVER = args[0]
            conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            conn.connect( (SERVER, options.port) )

        # bind generic descriptors
        if in_file:
            if in_file == '-':
                in_fd = sys.stdin
            else:
                in_fd = open(in_file, 'rb')
            out_fd = conn.makefile('wb', options.chunk_size)
        else:
            in_fd = conn.makefile('rb', options.chunk_size)

            if out_file == '-':
                out_fd = sys.stdout
            else:
                out_fd = open(out_file, 'wb')

        try:
            import worm
            anim = worm.animate
        except ImportError:
            i = itertools.cycle('|/-\\')
            if hasattr(i, 'next'):
                it = i.next
            else:
                it = partial(next, i)
            anim = lambda: [sys.stdout.write('\r%s'%it()), sys.stdout.flush()]

        # copy operation
        while True:
            data = in_fd.read(options.chunk_size)
            if not data:
                break
            out_fd.write(data)

            if out_fd is not sys.stdout:
                anim()

        in_fd.close()
        out_fd.close()
        if not options.cycle:
            break

main()
