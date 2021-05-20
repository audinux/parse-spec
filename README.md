# parse-spec
Parsing RPM Spec files to generate json data

The `main.py` will generate 2 json files (one pretty print, one minimized) from the folder `test/`.

The fields (parsed from the RPM spec) would be:
- name
- version
- url (of the source project)
- license
- summary
- description
- packages (list of packages names)

For the "Facets", they will be added as comment in the spec file:
```
...
# tags: foo, bar
# category: Synthesiser
...
```
Maybe other facets should be added. We start with tags and we will see what is useful to filter.


## Using python-rpm-spec

This repo embedded a modified copy of  https://github.com/bkircher/python-rpm-spec/ that adds support 
for `%description` ([submitted upstream](https://github.com/bkircher/python-rpm-spec/pull/42)) 
and `# Tags: ...` that we keep local to this repo, because these are non-standard.

## TODO

- parse the `# tags: ..` and other non-standard fields 
- add the folder as a program argument