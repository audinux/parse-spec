# parse-spec

Parsing RPM Spec files to generate json data

The `main.py` generates 2 json files (one pretty print, one minimized) from the folder `../fedora-spec/**/*.spec`.

The fields (parsed from the RPM spec) are be:
- name
- version
- url (of the source project)
- license
- summary
- description
- packages (list of packages names and summary)

For the "Tags", they are added as comment in the spec file:
```
...
# tags: foo, bar
# category: Synthesiser
# type: ..
...
```
Maybe other facets should be added. 


## Usage

1. Check the path line 44 in `main.py` 
2. Run `python main.py` 

For test, the application can read the `tests` directory, which contains a few folders.

To run on the full list of spec, clone the `fedora-spec` spec repo next to this repo.


## TODO

- add the `/*.spec` folder as a program argument
- Output more statistical analysis
- Add a mass modification feature


## Development

### Using python-rpm-spec

This repo embedded a modified copy of  https://github.com/bkircher/python-rpm-spec/ that adds support 
for `%description` ([submitted upstream](https://github.com/bkircher/python-rpm-spec/pull/42)) 
and `# Tags: ...` that we keep local to this repo, because these are non-standard.
