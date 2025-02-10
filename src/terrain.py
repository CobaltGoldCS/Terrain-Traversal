from pychrono.vehicle import RigidTerrain, Patch
from pychrono.core import ChSystem, ChContactMaterialNSC,ChContactMaterial, ChCoordsysd

import pychrono as chrono
from pathlib import Path

class TTTerrain(RigidTerrain):

    def __init__(self, system: ChSystem, path: str, *args):
        super().__init__(system, *args)
    
    def contact_material_one(self) -> ChContactMaterialNSC:
        material = ChContactMaterialNSC()
        material.SetRollingFriction(0.2)
        material.SetStaticFriction(0.6)
        return material