# parse-spec
Parsing RPM Spec files to generate json data

Try to use https://github.com/bkircher/python-rpm-spec for standard fields.

The Json to generate is not fixed yet, but should look like:
```
[
{"name":"BambooTracker","version":"0.4.6","url":"https://github.com/rerrahkr/BambooTracker","license":"GPL","summary":"BambooTracker is a music tracker for the Yamaha YM2608 sound chip","category":"","tags":[],"type":[],"description":"BambooTracker is a music tracker for the Yamaha YM2608 (OPNA) sound chip which was used in NEC PC-8801/9801 series computers."},
{"name":"BatLib","version":"0.1","url":"https://github.com/supercollider-quarks/BatLib","license":"Creative Commons Attribution-ShareAlike 4.0 International Public License","summary":"Various helper classes I use, and external methods my other Quarks use.","category":"","tags":[],"type":[],"description":"Various helper classes I use, and external methods my other Quarks use."},
...
]
```

The fields (parsed from the RPM spec) would be:
- name
- version
- url (of the source project)
- license
- summary
- description

For the "Facets", they will be added as comment in the spec file:
```
...
# tags: foo, bar
# category: Synthesiser
...
```
Maybe other facets should be added. We start with tags and we will see what is useful to filter.


## Using python-rpm-spec

Beware there are multiple other packages called `pyrpm`! 
You MUST not install `pyrpm`, but `python-rpm-spec`! 

- `pip install python-rpm-spec`  
- `from pyrpm.spec import Spec ...` in the code

Very counterintuitive!
