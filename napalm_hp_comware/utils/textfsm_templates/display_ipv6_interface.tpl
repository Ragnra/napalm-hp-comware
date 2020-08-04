#GigabitEthernet1/0/22 current state :UP
#Line protocol current state :UP
#IPv6 is enabled, link-local address is FE80::BAAF:67FF:FE22:C47E
#  Global unicast address(es):
#    2A02:D200::5:A, subnet is 2A02:D200::5:0/112
#  Joined group address(es):
#    FF02::12
#    FF02::1:FF05:0
#    FF02::1:FF05:A
#    FF02::1:FF22:C47E
#    FF02::2
#    FF02::1
#  MTU is 1500 bytes
#  ND DAD is enabled, number of DAD attempts: 1
#  ND reachable time is 30000 milliseconds
#  ND retransmit interval is 1000 milliseconds
#  Hosts use stateless autoconfig for addresses
#IPv6 Packet statistics:
#  InReceives:                   1595
#  InTooShorts:                  0
#  InTruncatedPkts:              0
#  InHopLimitExceeds:            0
#  InBadHeaders:                 0
Value Interface (\S+)
Value Admin (\S+)
Value Oper (UP|DOWN|UP\(s\)|DOWN\(s\))
Value LinkLocal (\S+)
Value List Addresses (\S+)
Value List Subnets (\S+)
Value List Prefixes (\S+)
Value List GroupAddresses (\S+)

Start
  ^${Interface} current state :${Admin}
  ^Line protocol current state :${Oper}
  ^IPv6 is enabled, link-local address is ${LinkLocal}
  ^  Global unicast address -> Unicast
  ^  Joined group address -> Multicast
  ^  MTU -> Record

Unicast
  ^    ${Addresses}, subnet is ${Subnets}/${Prefixes}
  ^  Joined group address -> Multicast
  ^  \S -> Start

Multicast
  ^    ${GroupAddresses}
  ^  MTU -> Record
  ^  \S -> Start

EOF