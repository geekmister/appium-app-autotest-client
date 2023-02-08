"""
The file created by Geemkmister, at 2023-02-05 PM 15:37.

The project lanuch file.
"""


from managers import parser_manager, device, repository
from utils import logger


def run():
    # parser command
    parser = parser_manager.get_parser()
    args = parser.parse_args()

    # fetch device list
    devices = device.package_devices()

    # get test case repository books
    books = repository.get_tc_repo_books(args.path)

    # allocation workspace


if __name__ == "__main__":
    run()
