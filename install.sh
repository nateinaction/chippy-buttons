#!/bin/bash
path=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )
service="chippy-buttons.service"

sudo cp "$path/$service" /lib/systemd/system/
sudo chmod 644 "/lib/systemd/system/$service"
sudo systemctl daemon-reload
sudo systemctl enable "$service"
sudo systemctl start "$service"
