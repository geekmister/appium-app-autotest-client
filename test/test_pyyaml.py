import yaml

from common import utils


def load_yaml(stream):

    obj = yaml.load(stream=stream, Loader=yaml.CLoader)
    utils.Logger.debug(obj)


if __name__ == "__main__":
    yaml_stream = open("../TestCaseRepository/TestYaml.yaml", "r")
    load_yaml(yaml_stream)