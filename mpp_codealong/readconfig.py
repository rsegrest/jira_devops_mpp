import config


def read_config_file():
    cfg = config.Config('configuration/jira.cfg')
    return cfg


if __name__ == "__main__":
    print(read_config_file())
