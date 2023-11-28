from PySide6.Qt3DCore import Qt3DCore

from PySide6.QtGui import QVector3D, QQuaternion
from PySide6.Qt3DExtras import Qt3DExtras

class Q3dViewer(Qt3DExtras.Qt3DWindow):

    def __init__(self) -> None:
        super().__init__()

        # Camera
        self.camera().lens().setPerspectiveProjection(45, 16 / 9, 0.1, 1000)
        self.camera().setPosition(QVector3D(0, 0, 40))
        self.camera().setViewCenter(QVector3D(0,0,0))

        # camera controls
        self.create_scene()
        self.camController = Qt3DExtras.QOrbitCameraController(self.rootEntity)
        self.camController.setLinearSpeed(50)
        self.camController.setLookSpeed(180)
        self.camController.setCamera(self.camera())

        self.show()

    def create_scene(self):
        self.rootEntity = Qt3DCore.QEntity()

        # material
        self.material = Qt3DExtras.QPhongMaterial(self.rootEntity)

        # torus
        self.torusEntity = Qt3DCore.QEntity(self.rootEntity)
        
        self.torusMesh = Qt3DExtras.QTorusMesh()
        self.torusMesh.setRadius(5)
        self.torusMesh.setMinorRadius(1)
        self.torusMesh.setRings(100)
        self.torusMesh.setSlices(20)

        self.torusTransform = Qt3DCore.QTransform()
        self.torusTransform.setScale3D(QVector3D(1.5, 1.0, 0.5))
        self.torusTransform.setRotation(QQuaternion.fromAxisAndAngle(QVector3D(1, 0, 0), 30))

        self.torusEntity.addComponent(self.torusMesh)
        self.torusEntity.addComponent(self.torusTransform)
        self.torusEntity.addComponent(self.material)