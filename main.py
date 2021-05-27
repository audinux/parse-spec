"""Python application to read a directory of spec files and output a json file

Currently it output one element per spec file.
Later we could add one element (or sub-element) per package.

"""
from typing import Dict, List, Any, Union

from analyse import Analysis
from spec import Spec, replace_macros
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
    output["version"] = replace_macros(spec.version, spec)
    output["summary"] = replace_macros(spec.summary, spec)
    output["license"] = spec.license
    output["url"] = spec.url
    if build_description(spec) is not None:
        output["description"] = build_description(spec)
    if spec.tag is not None:
        output["tag"] = [x.strip() for x in spec.tag.split(',')]
    if spec.type is not None:
        output["type"] = [x.strip() for x in spec.type.split(',')]
    if spec.category is not None:
        output["category"] = [x.strip() for x in spec.category.split(',')]
    output["packages"] = []
    for package in spec.packages:
        output["packages"].append(package.name)

    return output


def build_description(spec):
    """
    Manage description:
     - Remove redundant text when it copies the summary
     - Add Packages descriptions when there are lots of packages
     :param spec
     :return description or None
    """
    if spec.description is not None:
        description = str(spec.description.replace(spec.summary, '').removeprefix(".").removeprefix(",").strip())
        pkg_desc = []
        for package in spec.packages:
            if package.is_subpackage and not (package.name.endswith("-doc") or package.name.endswith("-devel"))\
                    and package.summary is not None:
                pkg_desc.append(replace_macros(package.name, spec) + ": " + replace_macros(package.summary, spec))
        if len(pkg_desc) > 1:
            description = description + "\n\nExtra packages:\n - " + "\n - ".join(pkg_desc)
        if description:
            return description.rstrip()
    return None


if __name__ == '__main__':

    current_dir = "../fedora-spec"      # replace by "." to use the current directory and the spec in tests/
    rpm_spec: list[dict[str, Union[Union[str, None, list[Any]], Any]]] = []
    print("\nFor each directory in \"" + current_dir + "\" , read the RPM spec file")
    path_list = Path(current_dir).glob('**/*.spec')
    for path in path_list:
        path_in_str = str(path)
        print("  File: " + path_in_str, end=" \t\t")
        if path.name in ["nwjs.spec"]:  # Some .spec are strange!
            print("Excluded!!")
        else:
            rpm_spec.append(parse_spec(path_in_str))

    print("  Output a json file")
    with open("search-data.pretty.json", "w") as write_file_pp:
        json.dump(rpm_spec, write_file_pp, indent=2)
    with open("search-data.json", "w") as write_file_min:
        json.dump(rpm_spec, write_file_min)

    print("\n\n** Data Analysis **")
    a = Analysis(rpm_spec)
    print(" Used only once:")
    print(" * Categories : " + " | ".join(sorted(a.get_lonely("category"))))
    print(" * Types      : " + " | ".join(sorted(a.get_lonely("type"))))
    print(" * Tag        : " + " | ".join(sorted(a.get_lonely("tag"))))
