# greenLightAdapter

A tool to manually or automatically manage rooms and users in BigBlueButton and Greenlight via rest api.
You can manage multiple users, rooms and sharing of rooms.
...

The application mainly features one mode:

* daemon mode (running in the background and whatching for changes and events to execute)

## installation

to install...
*  please clone the repository to /user/local/bin:

```
        git clone https://github.com/coderDem/greenLightAdapter.git /usr/local/bin/greenLightAdapter
```

* install the python packages required... (you can use the shell script for ubuntu if you want)

```
        /usr/local/bin/greenLightAdapter/python_packages_setup.sh
```

```
        apt -y install python3-pip
        apt -y install python3-psycopg2
        pip3 install -r /usr/local/bin/greenLightAdapter/python_packages.txt
```

* install the systemd startup scripts...

```
        /usr/local/bin/greenLightAdapter/systemd/install.sh
```

* start the processors...

```
        systemctl start greenLightAdapter
```

* to stopp...

```
        systemctl stop greenLightAdapter.target
```

## getting started
to understand how greenLightAdapter works and to have a first impression, please keep the following facts in mind and follow these steps:

* you need at least one BigBlueButton server and Greelnlight configured via api or config file.

* execute a first command via the commandline to see if it works. slCli.py -m [-s bbb_server_id] gives you information about the running meetings on your server. If you do not specify a server_id the id bbb is used. If you gave your first bbb server the id bbb you do not have to specify -s server_id for this command.

