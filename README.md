# Launch chrome on debug mode

launch chrome on mac on debug mode:
```
--remote-debugging-port=9222 --user-data-dir=remote-profile
```

on MacOS, chrome can be launched from `/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome`

as in:

```
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222 --user-data-dir=remote-profile
```

run test script to check the actual driver is the debug chrome instance:

```
python test.py
```
