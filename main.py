
from space_network_lib import *

network1=SpaceNetwork(2)
sat1=Satellite("TWS1",100)
sat2=Satellite("TWS2",200)
message=Packet("12 knots to the right",sat1,sat2)
network1.attempt_transmission(message)