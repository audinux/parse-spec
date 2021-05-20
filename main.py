"""Python application to read a directory of spec files and output a json file

Currently it output one element per spec file.
Later we could add one element (or sub-element) per package.

"""
from spec import Spec
import json
from pathlib import Path


def parse_spec(file_name):
    """
    Parse a spec file and append the packages to the list
    Even if there are multiple packages, only one element will be returned
    :param file_name:
    :return: the element data
    """
    output = {}
    spec = Spec.from_file(file_name)
    print(" ; Spec Name: " + spec.name)
    output["name"] = spec.name
    output["summary"] = spec.summary
    output["license"] = spec.license
    output["url"] = spec.url
    output["description"] = spec.description.rstrip()
    output["packages"] = []
    for package in spec.packages:
        output["packages"].append(package.name)

    # TODO call some function to parse the tags in comments ...

    return output


if __name__ == '__main__':

    current_dir = "."
    rpm_spec = []
    print("\nFor each directory in \"" + current_dir + "\" , read the RPM spec file")
    path_list = Path(current_dir).glob('**/*.spec')
    for path in path_list:
        path_in_str = str(path)
        print("  File: " + path_in_str, end=" \t\t")
        rpm_spec.append(parse_spec(path_in_str))

    print("  output a json file")
    with open("search-data.pretty.json", "w") as write_file_pp:
        json.dump(rpm_spec, write_file_pp, indent=2)
    with open("search-data.json", "w") as write_file_min:
        json.dump(rpm_spec, write_file_min)
