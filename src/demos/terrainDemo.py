from pychrono.core import ChVector3d, ChCoordsysd
from pychrono.irrlicht import ChVisualSystemIrrlicht
from pychrono.vehicle import ChWheeledVehicleVisualSystemIrrlicht, HMMWV_Full
import pychrono.vehicle as veh


import pychrono as chrono

from ..terrain import TTTerrain
from pathlib import Path


hmmwv = veh.HMMWV_Full()
hmmwv.SetInitPosition(ChCoordsysd(ChVector3d(0,0,0.5), chrono.ChQuaterniond(1, 0, 0, 0)))
hmmwv.Initialize()
hmmwv.SetChassisFixed(False)

hmmwv.SetChassisVisualizationType(veh.VisualizationType_PRIMITIVES)
hmmwv.SetSuspensionVisualizationType(veh.VisualizationType_PRIMITIVES)
hmmwv.SetSteeringVisualizationType(veh.VisualizationType_PRIMITIVES)
hmmwv.SetWheelVisualizationType(veh.VisualizationType_PRIMITIVES)
hmmwv.SetTireVisualizationType(veh.VisualizationType_PRIMITIVES)

hmmwv.GetSystem().SetCollisionSystemType(chrono.ChCollisionSystem.Type_BULLET)

vis = ChWheeledVehicleVisualSystemIrrlicht()
vis.AttachSystem(hmmwv.GetSystem())
vis.SetWindowSize(1280, 1024)
vis.SetWindowTitle("Terrain Demo")
vis.SetChaseCamera(chrono.ChVector3d(0.0, 0.0, 1.75), 6.0, 0.5)
vis.Initialize()
vis.AddTypicalLights()
vis.AddSkyBox()
vis.AttachVehicle(hmmwv.GetVehicle())

bmp = Path("terrain/patch_1.bmp").resolve()
terrain = TTTerrain(hmmwv.GetSystem(), str(bmp))
terrain.Initialize()

step_size = 3e-3;

while (vis.Run()):
    time = hmmwv.GetSystem().GetChTime()

    vis.BeginScene()
    vis.Render()
    vis.EndScene()
    terrain.Advance(step_size)
    hmmwv.Advance(step_size)
    vis.Advance(step_size)

    terrain.Synchronize(time)

