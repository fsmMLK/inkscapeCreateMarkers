#!/usr/bin/python

# --------------------------------------------------------------------------------------
#
#    createMarkers: - Inkscape extension to assist creating new markers with
#                     custom shape and colors.
#
#    Copyright (C) 2016 by Fernando Moura
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# --------------------------------------------------------------------------------------

import os
import inkex
import inkscapeMadeEasy_Base as inkBase
import inkscapeMadeEasy_Draw as inkDraw
import math

#---------------------------------------------


class CreateMarkers(inkBase.inkscapeMadeEasy):

    def __init__(self):
        inkBase.inkscapeMadeEasy.__init__(self)

        self.OptionParser.add_option("--tab", action="store", type="string", dest="tab", default="object")

        self.OptionParser.add_option("--makeDot", action="store", type="inkbool", dest="makeDot", default=False)
        self.OptionParser.add_option("--makeEllipsis", action="store", type="inkbool", dest="makeEllipsis", default=False)
        self.OptionParser.add_option("--makeArrow1", action="store", type="inkbool", dest="makeArrow1", default=False)
        self.OptionParser.add_option("--makeCustom", action="store", type="inkbool", dest="makeCustom", default=False)

        self.OptionParser.add_option("--makeDotName", action="store", type="string", dest="makeDotName", default='myDot')
        self.OptionParser.add_option("--makeEllipsisName", action="store", type="string", dest="makeEllipsisName", default='myEllip')
        self.OptionParser.add_option("--makeArrow1Name", action="store", type="string", dest="makeArrow1Name", default='myArrow')
        self.OptionParser.add_option("--makeCustomName", action="store", type="string", dest="makeCustomName", default='myCustom')

        self.OptionParser.add_option("--makeCustomPathDef", action="store", type="string", dest="makeCustomPathDef", default='M -5,5 L 5,-5 M 5,5 L -5,-5')
        self.OptionParser.add_option("--makeCustomLineWidth", action="store", type="float", dest="makeCustomLineWidth", default=1.0)

        self.OptionParser.add_option("--scale", action="store", type="float", dest="scale", default=1)
        self.OptionParser.add_option("--renameMode", action="store", type="string", dest="renameMode", default='2')

        self.OptionParser.add_option("--markColor", action="store", type="string", dest="markColorOption", default='black')
        self.OptionParser.add_option("--colorPickerMark", action="store", type="string", dest="colorPickerMark", default='0')

        self.OptionParser.add_option("--lineColor", action="store", type="string", dest="lineColorOption", default='black')
        self.OptionParser.add_option("--colorPickerLine", action="store", type="string", dest="colorPickerLine", default='0')

    def effect(self):

        so = self.options

        # sets the position to the viewport center, round to next 10.
        position = [self.view_center[0], self.view_center[1]]
        position[0] = int(math.ceil(position[0] / 10.0)) * 10
        position[1] = int(math.ceil(position[1] / 10.0)) * 10

        #root_layer = self.current_layer
        root_layer = self.document.getroot()
        #root_layer = self.getcurrentLayer()

        # sets colors. See inkDraw.color class for instructions.
        [markerColor, alpha] = inkDraw.color.parseColorPicker(so.markColorOption, so.colorPickerMark)
        [lineColor, alpha] = inkDraw.color.parseColorPicker(so.lineColorOption, so.colorPickerLine)

        if so.makeDot:
            nameMarkerDot = inkDraw.marker.createDotMarker(self, so.makeDotName + '_' + str(so.scale), RenameMode=int(so.renameMode), scale=0.4 * so.scale, strokeColor=lineColor, fillColor=markerColor)
            lineStylePlot = inkDraw.lineStyle.set(lineWidth=1, lineColor=lineColor, markerStart=nameMarkerDot, markerEnd=nameMarkerDot)
            inkDraw.line.relCoords(root_layer, [[10, 0], [10, -10]], [position[0], position[1]], lineStyle=lineStylePlot)

        if so.makeEllipsis:
            startMarker, endMarker = inkDraw.marker.createInfLineMarker(self, so.makeEllipsisName + '_' + str(so.scale), RenameMode=int(so.renameMode), scale=so.scale, fillColor=markerColor)
            lineStylePlot = inkDraw.lineStyle.set(lineWidth=1, lineColor=lineColor, markerStart=startMarker, markerEnd=endMarker)
            inkDraw.line.relCoords(root_layer, [[10, 0], [10, -10]], [position[0], position[1] + 5], lineStyle=lineStylePlot)

        if so.makeArrow1:
            startMarker, endMarker = inkDraw.marker.createArrow1Marker(self, so.makeArrow1Name + '_' + str(so.scale), RenameMode=int(so.renameMode), scale=0.4 * so.scale, strokeColor=lineColor, fillColor=markerColor)
            lineStylePlot = inkDraw.lineStyle.set(lineWidth=1, lineColor=lineColor, markerStart=startMarker, markerEnd=endMarker)
            inkDraw.line.relCoords(root_layer, [[10, 0], [10, -10]], [position[0], position[1] + 10], lineStyle=lineStylePlot)

        if so.makeCustom:
            markerPath = so.makeCustomPathDef
            markerTransform = 'scale(' + str(so.scale) + ')'
            Marker = inkDraw.marker.createMarker(self, so.makeCustomName + '_' + str(so.scale), markerPath=markerPath, RenameMode=int(so.renameMode), strokeColor=lineColor, fillColor=markerColor, lineWidth=so.makeCustomLineWidth, markerTransform=markerTransform)
            lineStylePlot = inkDraw.lineStyle.set(lineWidth=1, lineColor=lineColor, markerStart=Marker, markerEnd=Marker)
            inkDraw.line.relCoords(root_layer, [[10, 0], [10, -10]], [position[0], position[1] + 20], lineStyle=lineStylePlot)

if __name__ == '__main__':
    markers = CreateMarkers()
    markers.affect()
