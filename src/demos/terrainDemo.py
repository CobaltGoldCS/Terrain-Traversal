from pychrono.core import ChSystemNSC, ChVector3d, ChCoordsysd
from pychrono.irrlicht import ChVisualSystemIrrlicht

import pychrono as chrono

from ..terrain import TTTerrain
from pathlib import Path

sys = ChSystemNSC()
vis = ChVisualSystemIrrlicht()
vis.AttachSystem(sys)
vis.SetWindowSize(1024, 768)
vis.SetWindowTitle("Terrain Demo")
vis.Initialize()
vis.AddSkyBox()
vis.AddCamera(ChVector3d(0, 8, 6))
vis.AddTypicalLights()

bmp = Path("terrain/patch_1.bmp").resolve()
terrain = TTTerrain(sys, str(bmp))
print(bmp.resolve())
terrain.Initialize()


while (vis.Run()):
    vis.BeginScene()
    vis.Render()
    vis.EndScene()
    sys.DoStepDynamics(0.01)
