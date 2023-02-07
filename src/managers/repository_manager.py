"""
Created by Geemkmister, at 2023-02-05 PM 16:19

The module is manage AppRepository and TestCaseRepository and custom it path.

Features:
    1. get_tc_repo_books get test case repository books
"""


import os

from utils import logger


def app_repo_iterator(path="../AppRepository"):
    """
    Desc: iterable app repository, default ../AppRepository
    Params:
        path | app repository root path
    """
    pass


def get_tc_repo_books(path):
    """
    Desc:
        1. get test case repository books
    Params:
        path | test case repository root path
    Todo:
        1. need add error judgment
    """

    if path == "":
        logger.error("The input path is not null")
        return None

    # test case repository books
    books = {"root": path, "readme": "", "childs": []}

    tree = os.walk(top=path, topdown=True, onerror=None, followlinks=False)
    for root, dirs, files in tree:
        if root == path:
            books["readme"] = os.path.join(root, "readme.yaml")
            for item in dirs:
                books["childs"].append(item)
        else:
            child = root[root.rfind("/") + 1:]
            books[child] = []
            for item in files:
                books[child].append(os.path.join(root, item))

    return books


if __name__ == "__main__":
    pass
