#!/bin/bash
set -e
targetDir=/lib/systemd/system
linkDir=/etc/systemd/system
echo "installing systemd files..."
for file in /usr/local/bin/greenLightAdapter/systemd/greenLightAdapter*
do
    if [[ -f $file ]]; then
        cp $file $targetDir
    fi
done
systemctl daemon-reload
if [[ -f $targetDir/greenLightAdapter-api.service ]]; then
    systemctl enable greenLightAdapter-api.service
fi
