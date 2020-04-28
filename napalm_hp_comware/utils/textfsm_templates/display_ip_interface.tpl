# 
# HP Comware v7.x 'display ip interface' 
# 
#
#Vlan-interface1 current state: UP
#Line protocol current state: UP
#Internet Address is 10.0.0.1/24 Primary
#Broadcast address: 10.0.0.255
#The Maximum Transmit Unit: 1500 bytes
#input packets : 0, bytes : 0, multicasts : 0
#output packets : 38737, bytes : 2015915, multicasts : 0
#TTL invalid packet number:         0
#ICMP packet input number:          0
#  Echo reply:                      0
#  Unreachable:                     0
#  Source quench:                   0
#  Routing redirect:                0
#  Echo request:                    0
#  Router advert:                   0
#  Router solicit:                  0
#  Time exceed:                     0
#  IP header bad:                   0
#  Timestamp request:               0
#  Timestamp reply:                 0
#  Information request:             0
#  Information reply:               0
#  Netmask request:                 0
#  Netmask reply:                   0
#  Unknown type:                    0
Value INTERFACE (\S+)
Value INTERFACE_STATE (UP|DOWN|ADM|Stby)
Value INTERFACE_PROTOCOL_STATE (UP|DOWN|UP\(s\)|DOWN\(s\))
Value IP_ADDRESS (\d+\.\d+\.\d+\.\d+)
Value PREFIX_LENGTH (\d{1,2})

Start
  #^${INTERFACE}\scurrent\sstate:\s${INTERFACE_STATE}
  ^Line protocol current state: ${INTERFACE_PROTOCOL_STATE}

Interface_rec
  ^Line protocol current state: ${INTERFACE_PROTOCOL_STATE}
  ^Internet Address is ${IP_ADDRESS}/${PREFIX_LENGTH}

EOF