"""
The file created by Geemkmister, at 2023-02-05 PM 15:37.

The project lanuch file.
"""


from managers import parser_manager
from utils import logger

def run():
    # fetch device list
    # get test case repository books
    # allocation workspace
    pass

if __name__ == "__main__":
    parser = parser_manager.get_parser()
    args = parser.parse_args()
    logger.debug(args.path)
