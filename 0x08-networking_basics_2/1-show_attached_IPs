#!/usr/bin/env bash
# displays all active IPv4 IPs on the machine it's executed on.
ifconfig | awk '$1 == "inet" { print $2}'
