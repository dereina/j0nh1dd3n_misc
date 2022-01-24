import argparse

parser = argparse.ArgumentParser(description="")

# Optional argument
parser.add_argument('-cp', '--config_path', type=str, default='config.yaml', help="path to the configuration file")
parser.add_argument("-pc", "--pre_classify", action="store_true",
                    help="pre classify before object detection between target classes")
args = parser.parse_args()
print(args)
print(args.config_path)