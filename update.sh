#!/bin/bash

# Set PATH for cron environment
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

# Define the absolute path to ansible-playbook
ANSIBLE_PLAYBOOK=/usr/bin/ansible-playbook  # Adjust this path if ansible-playbook is located elsewhere

# Run first Ansible playbook and log output
$ANSIBLE_PLAYBOOK --verbose -i /home/ansible/inventory.ini /home/ansible/Ubuntu-servers.yml > /home/ansible/playback-updates.txt

# Check if the first playbook ran successfully
if [ $? -eq 0 ]; then
    echo "Ubuntu-servers.yml ran successfully."
else
    echo "Ubuntu-servers.yml encountered errors."
fi

# Run second Ansible playbook and log output
$ANSIBLE_PLAYBOOK /home/ansible/notify.yml > /home/ansible/playback-notify.txt

# Check if the second playbook ran successfully
if [ $? -eq 0 ]; then
    echo "notify.yml ran successfully."
else
    echo "notify.yml encountered errors."
fi

# Run the Python script to convert logs to HTML
/usr/bin/python3 /home/ansible/txt2www.py >> /home/ansible/txt2www.log 2>&1

# Check if the Python script ran successfully
if [ $? -eq 0 ]; then
    echo "txt2www.py ran successfully."
else
    echo "txt2www.py encountered errors."
fi