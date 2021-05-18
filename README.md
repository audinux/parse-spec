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
