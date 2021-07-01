import Modules.Config as cf
import Modules.Mirror as Mirror
import include.ImagePlane as ImagePlane
import include.OpticalSystem as OpticalSystem
import Modules.Foil as Foil
# import Modules.Filament as Filament
import numpy as np


def GetGeometry():

    M0 = Mirror.PlaneMirror(
        normal=cf.M0['normal'], R=cf.M0['R'], name=cf.M0['name'])

    Md = Mirror.DiffMirror(R=cf.Md['R'], name=cf.Md['name'])

    M1 = Mirror.ParaMirror(f=cf.M1['f'], H=cf.M1['H'], D=cf.M1['D'],
                           rough=cf.M1['rough'], name=cf.M1['name'])

    M2 = Mirror.ParaMirror(f=cf.M2['f'], H=cf.M2['H'], D=cf.M2['D'],
                           rough=cf.M1['rough'], name=cf.M2['name'])

    M3 = Mirror.ParaMirror(f=cf.M3['f'], H=cf.M3['H'], D=cf.M3['D'],
                           rough=cf.M1['rough'], name=cf.M3['name'])

    M4 = Mirror.ParaMirror(f=cf.M4['f'], H=cf.M4['H'], D=cf.M4['D'],
                           rough=cf.M1['rough'], name=cf.M4['name'])

    image = ImagePlane.ImagePlane(R=cf.camera['R'], name=cf.camera['name'])

    foil = Foil.CalibrationFoil(normal=np.array([[0., 1., 0.]]), diam=50.,
                hole_dist=7., hole_diam=1.2, name=cf.foil['name'], cross=cf.background['cfoil'])

    # Shift the mirror and camera in small distances
    # cf.M1['X'][0,0] += shift
    # cf.M2['X'][0,0] += shift
    # cf.M3['X'][0,0] += shift
    # cf.M4['X'][0,0] += shift
    # cf.camera['X'][0,0] += shift

    # cf.M2['X'][0,1] += shift
    # cf.M3['X'][0,1] += shift
    # cf.M4['X'][0,1] += shift
    # cf.camera['X'][0,1] += shift

    # cf.M3['X'][0,0] += shift
    # cf.M4['X'][0,0] += shift
    # cf.camera['X'][0,0] += shift

    # cf.M4['X'][0,1] += shift
    # cf.camera['X'][0,1] += shift
    #
    # cf.camera['X'][0,0] += shift
    M0.Place(X=cf.M0['X'], angles=cf.M0['angles'], yrot=cf.M0['yrot'])
    Md.Place(X=cf.Md['X'], angles=cf.Md['angles'], yrot=cf.Md['yrot'])
    M1.Place(X=cf.M1['X'], angles=cf.M1['angles'])
    M2.Place(X=cf.M2['X'], angles=cf.M2['angles'])
    M3.Place(X=cf.M3['X'], angles=cf.M3['angles'])
    M4.Place(X=cf.M4['X'], angles=cf.M4['angles'])
    foil.Place(X=cf.foil['X'], angles=cf.foil['angles'])
    image.Place(X=cf.camera['X'], angles=cf.camera['angles'])

    system = OpticalSystem.OpticalSystem()
    system.AddComponent(M4)
    system.AddComponent(M3)
    system.AddComponent(M2)
    system.AddComponent(M1)
    # system.AddComponent(M0)
    system.AddComponent(Md)
    # system.AddComponent(foil)
    system.AddComponent(M1)
    system.AddComponent(M2)
    system.AddComponent(M3)
    system.AddComponent(M4)
    system.AddComponent(image)
    return system
