# Create VLAN eth1.100 (assume we have a NIC eht1 whose IP is 192.168.0.127)
sudo ip link add link eth1 name eth1.100 type vlan id 100
sudo ip addr add 192.168.0.128/24 brd 192.168.0.127 dev eth1.100
sudo ip link set dev eth1.100 up
sudo ip link set dev eth1.100 down
ip link delete eth1.100
