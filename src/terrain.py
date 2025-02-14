from pychrono.vehicle import RigidTerrain, Patch, GetDataFile
from pychrono.core import ChSystem, ChContactMaterialNSC,ChContactMaterial, ChCoordsysd, ChQuaterniond, ChVector3d, ChColor

import pychrono as chrono
from pathlib import Path

TERRAIN_TEXTURE  = str(Path("terrain/terrainTexture.jpg").resolve())

class TTTerrain(RigidTerrain):

    def __init__(self, system: ChSystem, path: str, *args):
        super().__init__(system, *args)
        patch = self.AddPatch(
            self.contact_material_one(),
            ChCoordsysd(ChVector3d(0,0,0), ChQuaterniond(0,0,0,1)),
            path, 50.0, 50.0, 0.0, 3.0
        )
        patch.SetColor(ChColor(1.0,0.5,0))
        patch.SetTexture(str(Path("terrain/terrainTexture.jpg").resolve()), 6.0,6.0)
    
    def contact_material_one(self) -> ChContactMaterialNSC:
        material = ChContactMaterialNSC()
        material.SetFriction(0.9)
        material.SetRestitution(0.01)
        return material