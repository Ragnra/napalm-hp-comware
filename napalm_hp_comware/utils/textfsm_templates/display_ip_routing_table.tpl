# Destinations : 400      Routes : 400
#
# Destination/Mask    Proto  Pre  Cost         NextHop         Interface
# 0.0.0.0           Static 60   0            15.115.1.1      Vlan1101
# 0.0.0.0          Direct 0    0            127.0.0.1       InLoop0
# 15.6.9.0/24         Static 60   0            15.100.1.11     Vlan21
# 15.6.15.0/24        Static 60   0            15.100.1.11     Vlan21
# 15.6.13.0/24        Static 60   0            15.100.1.11     Vlan21
# 15.6.13.52/30       Static 60   0            15.100.1.10     Vlan21
# 15.24.1.0/29        Direct 0    0            15.24.1.6       Vlan7
# 15.24.1.0/32        Direct 0    0            15.24.1.6       Vlan7
# 15.24.1.6/32        Direct 0    0            127.0.0.1       InLoop0
# 15.24.1.7/32        Direct 0    0            15.24.1.6       Vlan7
# 15.24.32.0/24       Static 60   0            15.100.1.10     Vlan21
# 15.24.36.0/24       Static 60   0            155.187.160.4   Vlan160
# 15.25.1.0/24        OSPF   150  1            15.100.2.2      Vlan1102
# 15.26.0.0/16        Static 60   0            0.0.0.0         NULL0
# 15.26.254.0/28      Direct 0    0            15.26.254.2     Vlan300
# 15.26.254.0/32      Direct 0    0            15.26.254.2     Vlan300s
Value Network (\d+\.\d+\.\d+\.\d+)
Value Prefix (\d{1,2})
Value Protocol (\S+)
Value Preference (\d+)
Value Cost (\d+)
Value Nexthop (\d+\.\d+\.\d+\.\d+)
Value Interface (\S+)

Start
  ^${Network}/?${Prefix}?\s+${Protocol}\s+${Preference}\s+${Cost}\s+${Nexthop}\s+${Interface} -> Record