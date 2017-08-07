"""Handle main configuration for the Central server."""
from hydra import Resource
from rdflib import Namespace
from flock_controller.settings import CENTRAL_SERVER_NAMESPACE
from flock_controller.settings import DRONE1_NAMESPACE, DRONE2_NAMESPACE, DRONE3_NAMESPACE, DRONE4_NAMESPACE
from flock_controller.settings import IRI_CS, IRI_DRONE1, IRI_DRONE2, IRI_DRONE3, IRI_DRONE4


global CENTRAL_SERVER, DRONE1, DRONE2, DRONE3, DRONE4
CENTRAL_SERVER = Namespace(CENTRAL_SERVER_NAMESPACE)
# print(CENTRAL_SERVER)
DRONE1 = Namespace(DRONE1_NAMESPACE)
DRONE2 = Namespace(DRONE2_NAMESPACE)
DRONE3 = Namespace(DRONE3_NAMESPACE)
DRONE4 = Namespace(DRONE4_NAMESPACE)
# print(DRONE1)

global RES_CS, RES_DRONE1, RES_DRONE2, RES_DRONE3, RES_DRONE4
RES_CS = Resource.from_iri(IRI_CS)
RES_DRONE1 = Resource.from_iri(IRI_DRONE1)
RES_DRONE2 = Resource.from_iri(IRI_DRONE2)
RES_DRONE3 = Resource.from_iri(IRI_DRONE3)
RES_DRONE4 = Resource.from_iri(IRI_DRONE4)


def gen_State(drone_id, battery, direction, position, sensor_status, speed):
    """Generate a State objects."""
    state = {
        "@type": "State",
        "DroneID": drone_id,
        "Battery": battery,
        "Direction": direction,
        "Position": position,
        "Status": sensor_status,
        "Speed": speed,
    }
    return state


# Some general Functions
def ordered(obj):
    """Sort json dicts and lists within."""
    if isinstance(obj, dict):
        return sorted((k, ordered(v)) for k, v in obj.items())
    if isinstance(obj, list):
        return sorted(ordered(x) for x in obj)
    else:
        return obj
