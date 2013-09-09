# ansible-cfme

Sets up a proxy server for testing.

## ansible-cfme repository/structure

 * files - files and templates for use in playbooks/tasks
 * group_vars - customize deployment by setting/replacing variables
 * library - library of custom local ansible modules
 * tasks - snippets of tasks that should be included in plays
 * vars - os_release specific customizations

## Dependencies
 * [ansible-1.2](https://github.com/ansible/ansible) (or newer)

## Instructions
1. Clone this repo

        git clone https://github.com/mfalesni/ansible-squid-proxy-setup.git

2. Run the playbook:

        ansible-playbook -i inventory -e "ipaddr=<machine_ip_address>" site.yml

3. Drink coffee
## What the installer does
1. Updates the system
2. Reboots the machine
3. Installs and sets up Squid
4. Reboots again

## Issues and TODO
 * Work in progress

Please send me feedback at [mfalesni@redhat.com](mailto:mfalesni@redhat.com) with issues or suggestions. Pull requests encouraged!
