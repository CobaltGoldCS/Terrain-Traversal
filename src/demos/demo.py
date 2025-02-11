from pychrono.core import ChSystemNSC, ChBody, ChVector3d, ChLinkLockRevolute, ChRealtimeStepTimer, ChFramed, ChColor, ChCoordsysd, CH_PI, ChFunctionConst, ChLinkLockPointLine, ChLinkMotorRotationSpeed, QUNIT
from pychrono.irrlicht import ChVisualSystemIrrlicht, drawGrid, drawSegment, drawCircle

sys = ChSystemNSC()

my_body_A = ChBody()
sys.AddBody(my_body_A)
my_body_A.SetFixed(True)
my_body_A.SetName("Ground-Truss")


my_body_B = ChBody()
sys.AddBody(my_body_B)
my_body_B.SetPos(ChVector3d(1, 0, 0))
my_body_B.SetMass(10)
my_body_B.SetName("Crank")

my_body_C = ChBody()
sys.AddBody(my_body_C)
my_body_C.SetPos(ChVector3d(4, 0, 0));
my_body_C.SetMass(50)
my_body_C.SetName("Rod")


my_link_BC = ChLinkLockRevolute();
my_link_BC.SetName("RevJointCrankRod");
my_link_BC.Initialize(my_body_B, my_body_C, ChFramed(ChVector3d(2, 0, 0)));
sys.AddLink(my_link_BC);


my_link_CA = ChLinkLockPointLine();
my_link_CA.SetName("TransJointRodGround");
my_link_CA.Initialize(my_body_C, my_body_A, ChFramed(ChVector3d(6, 0, 0)));
sys.AddLink(my_link_CA);


my_link_AB = ChLinkMotorRotationSpeed();
my_link_AB.Initialize(my_body_A, my_body_B, ChFramed(ChVector3d(0, 0, 0)));
my_link_AB.SetName("RotationalMotor");
sys.AddLink(my_link_AB);
my_speed_function = ChFunctionConst(CH_PI);
my_link_AB.SetSpeedFunction(my_speed_function);

vis = ChVisualSystemIrrlicht();
vis.AttachSystem(sys);
vis.SetWindowSize(800, 600);
vis.SetWindowTitle("Simple slider-crank example");
vis.Initialize();
vis.AddLogo();
vis.AddSkyBox();
vis.AddCamera(ChVector3d(0, 0, -6));
vis.AddTypicalLights();

realtime_timer = ChRealtimeStepTimer()
time_step = 0.01;

while (vis.Run()):

    vis.BeginScene();

    vis.Render();

    drawGrid(vis, 0.5, 2);
    vis.GetGUIEnvironment().drawAll();

    drawSegment(vis, my_link_BC.GetMarker1().GetAbsCoordsys().pos,
                        my_link_CA.GetMarker1().GetAbsCoordsys().pos, ChColor(0, 1, 0));
    drawSegment(vis, my_link_AB.GetFrame2Abs().GetCoordsys().pos,
                        my_link_BC.GetMarker1().GetAbsCoordsys().pos, ChColor(0, 0, 0));
    drawCircle(vis, 0.1, ChCoordsysd(ChVector3d(0, 0, 0), QUNIT));

    sys.DoStepDynamics(time_step);
    realtime_timer.Spin(time_step);

    vis.EndScene();
