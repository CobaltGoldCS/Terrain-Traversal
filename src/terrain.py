from pychrono.vehicle import RigidTerrain, Patch, GetDataFile
from pychrono.core import ChSystem, ChContactMaterialNSC,ChContactMaterial, ChCoordsysd

import pychrono as chrono
from pathlib import Path

class TTTerrain(RigidTerrain):

    def __init__(self, system: ChSystem, path: str, *args):
        super().__init__(system, *args)
        patch = self.AddPatch(self.contact_material_one(), ChCoordsysd(), path, 600.0, 600.0, 0.0, 100.0)
        patch.SetTexture(GetDataFile("terrain/textures/tile4.jpg"), 200, 200)
    
    def contact_material_one(self) -> ChContactMaterialNSC:
        material = ChContactMaterialNSC()
        material.SetRollingFriction(0.2)
        material.SetStaticFriction(0.6)
        return material