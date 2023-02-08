"""
Created by Geemkmister, at 2023-02-05 PM 16:19

The module is manage AppRepository and repository and custom it path.

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
    Desc: get test case repository books
    Params:
        path, test case repository root path
    Todo:
        1. need add error judgment
    """

    logger.info("get test case repository books...")

    if path is None or path == "":
        logger.error("The input path is not null")
        return None

    # test case repository books
    books = {"readme": os.path.join(path, "readme.yaml"), "android": [], "iOS": []}

    # generate android test case books
    for root, dirs, files in os.walk(
            top=os.path.join(path, "android"), topdown=True, onerror=None, followlinks=False):
        if root == os.path.join(path, "android"):
            for item in dirs:
                group = {"name": item, "cases": []}
                books["android"].append(group)
            break
    for i in range(len(books["android"])):
        for root, dirs, files in os.walk(
                top=os.path.join(path, "android/" + books["android"][i]["name"]),
                topdown=True, onerror=None, followlinks=False):
            if root == os.path.join(path, "android/" + books["android"][i]["name"]):
                for item in files:
                    books["android"][i]["cases"].append(item)

    # generate iOS test case books
    for root, dirs, files in os.walk(top=os.path.join(path, "iOS"),
                                     topdown=True, onerror=None, followlinks=False):
        if root == os.path.join(path, "iOS"):
            for item in dirs:
                group = {"name": item, "cases": []}
                books["iOS"].append(group)
            break
    for i in range(len(books["iOS"])):
        for root, dirs, files in os.walk(
                top=os.path.join(path, "iOS/" + books["iOS"][i]["name"]),
                topdown=True, onerror=None, followlinks=False):
            if root == os.path.join(path, "iOS/" + books["iOS"][i]["name"]):
                for item in files:
                    books["iOS"][i]["cases"].append(item)

    logger.info(books)
    return books


if __name__ == "__main__":
    pass