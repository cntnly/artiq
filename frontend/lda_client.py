#!/usr/bin/env python3

import argparse

from artiq.management.pc_rpc import Client


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--server', default="::1",
                        help="hostname or IP of the controller to connect to")
    parser.add_argument('-p', '--port', default=8890, type=int,
                        help="TCP port to use to connect to the controller")
    parser.add_argument('-a', '--attenuation', type=float,
                        help="attenuation value to set")
    args = parser.parse_args()

    remote = Client(args.server, args.port, "lda")

    try:
        if args.attenuation is None:
            print("Current attenuation: {}".format(remote.get_attenuation()))
        else:
            remote.set_attenuation(args.attenuation)
    finally:
        remote.close_rpc()

if __name__ == "__main__":
    main()