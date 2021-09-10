""" Analyse the Meta-data
 report on potential error and statistics

 Should create an object, using the data as parameter
  - that generates internal structure containing stats
 The main program could call specific function to extract data
   get_lonely
   get_redundant

To use like this:
    with open("redundant.json", "w") as write_file:
        json.dump(analyse.get_redundant(), write_file, indent=2)

See http://jsdatav.is/chap07.html

"""
from typing import Any, Union


class Analysis:
    """ The Goal is to parse the data only once
    """
    count = {"tag": {}, "type": {}, "category": {}}

    def __init__(self, rpm_spec: [dict[str, Union[Union[str, None, list[Any]], Any]]]):
        for spec in rpm_spec:
            for tag_typ in ["tag", "type", "category"]:
                if tag_typ in spec:
                    for tag in spec[tag_typ]:
                        if tag in self.count[tag_typ]:
                            self.count[tag_typ][tag] += 1
                        else:
                            self.count[tag_typ][tag] = 1

    def get_lonely(self, tag_typ) -> [str]:
        # return filter(lambda x: x[1] == 1, self.count_tag.items())
        return [key for (key, value) in self.count[tag_typ].items() if value < 2]
