import sys

from cmd import SpsCmdList

class SpsCmd:
    @staticmethod
    def main(args):
        sps_cmd_list = SpsCmdList(args[1])
        sps_cmd_list.run()


if __name__ == "__main__":
    SpsCmd.main(sys.argv)