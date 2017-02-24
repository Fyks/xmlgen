def asq():
    ip = open('ip')
    ethernetIpAddress = ip.readline()[0:-1]
    ethernetSubnetMask = ip.readline()[0:-1]
    print('    <IPoverEthernet ethernetIpAddress=' +
          '\"' + ethernetIpAddress +
          '\"' + ' ethernetSubnetMask=' +
          '\"' + ethernetSubnetMask + '\"' + ' />')
    pass
