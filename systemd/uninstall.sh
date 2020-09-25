#!/bin/bash
set -e
targetDir=/lib/systemd/system
linkDir=/etc/systemd/system
echo "uninstalling systemd files..."
if [[ -f $targetDir/greenLightAdapter-api.service ]]; then
    systemctl disable greenLightAdapter-api.service
fi
for file in /usr/local/bin/greenLightAdapter/systemd/greenLightAdapter*
do
    if [[ -f $file ]]; then
        rm -f $targetDir/${file##*/}
        rm -f $linkDir/${file##*/}
    fi
done
systemctl daemon-reload
