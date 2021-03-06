import pip
from subprocess import call
from sys import version
import argparse

version_modifier = version[0]

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--cert', dest='certificate')

    args = parser.parse_args()

    for dist in pip.get_installed_distributions():
        cmd_args = ["python{}".format(version_modifier), "-m", "pip",
                    "install", "--user", "--upgrade", dist.project_name]
        if args.certificate:
            cmd_args.insert(1, '--cert')
            cmd_args.insert(2, args.certificate)
        call(cmd_args)
