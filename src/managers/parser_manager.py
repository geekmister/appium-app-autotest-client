"""
The module created by Geemkmister, at 2023-02-05 PM 15:40.

This is a command parser.

Features:
    1. get_parser get cmd parser;
"""


import argparse


def get_parser():
    """
    Desc: get cmd parser
    Params:
        None
    """
    parser = argparse.ArgumentParser(description="Appium app autotest cmd resolver.")
    parser.add_argument("--path", type=str, required=True, help="Test case repository root path.")

    return parser
