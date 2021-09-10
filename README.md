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

Other tags are used, but not yet parsed:
```
# GUIToolkit: Qt4, Fltk, GTK3, SWT ...
# LastSourceUpdate: 2020, 2005
```
Might be replaced by a `tag: Legacy` or `tag: Obsolete`   

## Usage

Run `python main.py <path to spec files>`  a glob is used to scan sub-folders `**/*.spec`.

For test, the application can read the `tests` directory, which contains a few folders. Run `python main.py .` 

To run on the full list of spec, clone the `fedora-spec` spec repo next to this repo. Run `python main.py ../fedora-spec`


## TODO

- Output more statistical analysis
- Add a mass modification feature


## Development

### Using python-rpm-spec

This repo embedded a modified copy of  https://github.com/bkircher/python-rpm-spec/ that adds support 
for `%description` ([submitted upstream](https://github.com/bkircher/python-rpm-spec/pull/42)) 
and `# Tags: ...` that we keep local to this repo, because these are non-standard.
