# %UCASE_CLASS% karton service

Analyse %UCASE_CLASS% from files with Karton.

**Author**: cocoapuck

**Maintainers**: cocoapuck

## Usage

### Build local pip


`python3 setup.py bdist_wheel`


### Create service


`sudo nano /usr/lib/systemd/system/mwdb-karton-%CLASS%.service`


### Contents of /usr/lib/systemd/system/mwdb-karton-%CLASS%.service


```
[Unit]
Description=Karton System
After=network.target

[Service]
User=sadmin
Group=sadmin
WorkingDirectory=/opt/karton
Environment="PATH=/opt/karton/.karton/bin"
ExecStart=/opt/karton/.karton/bin/karton-%CLASS%
ExecReload=/bin/kill -s HUP $MAINPID
KillMode=mixed
TimeoutStopSec=5
PrivateTmp=true

[Install]
WantedBy=multi-user.target
```


### Systemd commands


`sudo systemctl daemon-reload`
`sudo systemctl enable mwdb-karton-%CLASS%`
`sudo systemctl start mwdb-karton-%CLASS%`


### MWDB Attributes


Add `%CLASS%` as an attribute in MWDB


### Other


Review code in `%CLASS%.py` and verify command, comsumer and producer filters.