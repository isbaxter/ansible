#!/bin/bash

# Run first Ansible playbook and log output
ansible-playbook -i /home/ansible/inventory.ini /home/ansible/Ubuntu-servers.yml > playback-updates.txt

# Check if the first playbook ran successfully
if [ $? -eq 0 ]; then
    echo "Ubuntu-servers.yml ran successfully."
else
    echo "Ubuntu-servers.yml encountered errors."
fi

# Run second Ansible playbook and log output
ansible-playbook notify.yml > playback-notify.txt

# Check if the second playbook ran successfully
if [ $? -eq 0 ]; then
    echo "notify.yml ran successfully."
else
    echo "notify.yml encountered errors."
fi