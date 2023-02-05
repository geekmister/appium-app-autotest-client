import yaml


def load_yaml(stream):

    obj = yaml.load(stream=stream, Loader=yaml.CLoader)
    utils.Logger.debug(obj)


if __name__ == "__main__":
    yaml_stream = open("../resources/TestCaseRepository/TestYaml.yaml", "r")
    load_yaml(yaml_stream)