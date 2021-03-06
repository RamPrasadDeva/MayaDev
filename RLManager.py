import sys
from RenderLayers import EnvirLayer, CharLayer


class RLManager(object):
    def __init__(self):
        pass

    def createEnvirLayer(self, layerName):
        layer = EnvirLayer(layerName)
        layer.turnOffCharLights()
        layer.turnOffAllChar(False)
        layer.createAllEnvirCollection()
        layer.switchToLayer()

    def createCharLayer(self, layerName):
        layer = CharLayer(layerName)
        layer.turnOffEnvirLights()
        layer.turnOffAllEnvir(True)
        layer.createAllCharCollection()
        layer.switchToLayer()

    def createCustomEnvirLayer(self, layerName, isCutoutChecked):
        layer = EnvirLayer(layerName)
        layer.turnOffCharLights()

        # toggle only Envir cutout
        layer.turnOffAllEnvir(isCutoutChecked)

        layer.createCustomEnvirCollection(isCutoutChecked)
        layer.turnOffAllChar(False)
        layer.switchToLayer()

    def createCustomCharLayer(self, layerName, isCutoutChecked):
        layer = CharLayer(layerName)
        layer.turnOffEnvirLights()
        layer.turnOffAllEnvir(True)

        # toggle only Char cutout
        layer.turnOffAllChar(isCutoutChecked)

        layer.createCustomCharCollection(isCutoutChecked)
        layer.switchToLayer()