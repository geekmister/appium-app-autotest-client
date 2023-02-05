"""
Created by Geemkmister, at 2023-02-05 PM 16:19

The module is manage AppRepository and TestCaseRepository and custom define it path.

Features
"""


import os;

from 


def app_repo_iterator(path="../AppRepository"):
    """
    Desc: iterable app repository, default ../AppRepository
    Params: 
        path | app repository root path
    """
    pass


def tc_repo_iterator(path="../TestCaseRepository"):
    """
    Desc: iterable test case repository, default ../TestCaseRepository
    Params:
        path | test case repository root path
    """

    structure = os.walk(top=path, topdown=True, onerror=None, followlinks=False);
    for root, dirs, files in structure:
        logger.debug(root);
        logger.debug(dirs);
        logger.debug(files);


if __name__ == "__mian__":
    tc_repo_iterator();
