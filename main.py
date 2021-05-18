from pyrpm.spec import Spec, replace_macros
import json
from pathlib import Path


def parse_spec(file_name, packages):
    """
    Parse a spec file and append the packages to the list
    IF there was only one package per file, it would be simpler to return the data
    :param file_name:
    :param packages: list that will be updated
    :return: the updated liste
    """
    package = {}
    spec = Spec.from_file(file_name)
    print("Spec Name: " + spec.name + " ; Version: " + spec.version + " ; License: " + spec.license
          + " ; URL: " + spec.url + " ; Summary: " + spec.summary)
    package["license"] = spec.license
    package["url"] = spec.url
    package["name"] = spec.name
    # TODO call some function to parse the description ...
    # TODO call some function to parse the tags in comments ...
    packages.append(package)

    for package in spec.packages:
        print(f'{package.name}: {package.summary if hasattr(package, "summary") else spec.summary}')
        # Not used yet ...

    return packages


if __name__ == '__main__':

    current_dir = "."
    packages = []
    print("\nFor each directory in \"" + current_dir + "\" , read the spec file")
    path_list = Path(current_dir).glob('**/*.spec')
    for path in path_list:
        # because path is object not string
        path_in_str = str(path)
        print("  File: " + path_in_str)
        packages = parse_spec(path_in_str, packages)

    print("  output a json file")
    print(json.dumps(packages))
