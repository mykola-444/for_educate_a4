import yaml
import argparse
import sys


def main(number, other_number, output):
    result = number * other_number
    print(f'The result is {result}', file=output)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-n1', type=int, help='A number', default=3)
    parser.add_argument('-n2', type=int, help='Another number', default=3)

    parser.add_argument('-c', dest='config', type=argparse.FileType('r'),
                        help='config file in YAML format',
                        default='config.yaml')
# name of file must be STR
    parser.add_argument('-o', dest='output', type=argparse.FileType('w'),
                        help='output file',
                        default=sys.stdout)
# here default output is  sys_command

    args = parser.parse_args()
    if args.config:
        config = yaml.load(args.config)
        # Transforming values into integers
        args.n1 = config['ARGUMENTS']['n1']
        args.n2 = config['ARGUMENTS']['n2']

    main(args.n1, args.n2, args.output)
