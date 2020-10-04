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

import math

import inkscapeMadeEasy.inkscapeMadeEasy_Base as inkBase
import inkscapeMadeEasy.inkscapeMadeEasy_Draw as inkDraw

class CreateMarkers(inkBase.inkscapeMadeEasy):

    def __init__(self):
        inkBase.inkscapeMadeEasy.__init__(self)

        self.arg_parser.add_argument("--tab", type=str, dest="tab", default="object")

        self.arg_parser.add_argument("--markerType", type=str, dest="markerType", default='dot')
        self.arg_parser.add_argument("--markerName", type=str, dest="markerName", default='myDot')

        self.arg_parser.add_argument("--makeCustomPathDef", type=str, dest="makeCustomPathDef", default='M -5,5 L 5,-5 M 5,5 L -5,-5')
        self.arg_parser.add_argument("--makeCustomLineWidth", type=float, dest="makeCustomLineWidth", default=1.0)

        self.arg_parser.add_argument("--scale", type=float, dest="scale", default=1)
        self.arg_parser.add_argument("--renameMode", type=str, dest="renameMode", default='2')

        self.arg_parser.add_argument("--markColor", type=str, dest="markColorOption", default='black')
        self.arg_parser.add_argument("--colorPickerMark", type=str, dest="colorPickerMark", default='0')

        self.arg_parser.add_argument("--lineColor", type=str, dest="lineColorOption", default='black')
        self.arg_parser.add_argument("--colorPickerLine", type=str, dest="colorPickerLine", default='0')

    def effect(self):

        so = self.options

        # sets the position to the viewport center, round to next 10.
        position = [self.svg.namedview.center[0], self.svg.namedview.center[1]]
        position[0] = int(math.ceil(position[0] / 10.0)) * 10
        position[1] = int(math.ceil(position[1] / 10.0)) * 10

        # root_layer = self.current_layer
        root_layer = self.document.getroot()
        # root_layer = self.getcurrentLayer()

        # sets colors. See inkDraw.color class for instructions.
        [markerColor, alpha] = inkDraw.color.parseColorPicker(so.markColorOption, so.colorPickerMark)
        [lineColor, alpha] = inkDraw.color.parseColorPicker(so.lineColorOption, so.colorPickerLine)

        if so.markerType == 'dot':
            nameMarkerDot = inkDraw.marker.createDotMarker(self, so.markerName + '_' + str(so.scale), RenameMode=int(so.renameMode),
                                                           scale=0.4 * so.scale, strokeColor=lineColor, fillColor=markerColor)
            lineStylePlot = inkDraw.lineStyle.set(lineWidth=1, lineColor=lineColor, markerStart=nameMarkerDot, markerEnd=nameMarkerDot)
            inkDraw.line.relCoords(root_layer, [[10, 0], [10, -10]], [position[0], position[1]], lineStyle=lineStylePlot)

        if so.markerType == 'ellipsis':
            startMarker, endMarker = inkDraw.marker.createElipsisMarker(self, so.markerName + '_' + str(so.scale), RenameMode=int(so.renameMode),
                                                                        scale=so.scale, fillColor=markerColor)
            lineStylePlot = inkDraw.lineStyle.set(lineWidth=1, lineColor=lineColor, markerStart=startMarker, markerEnd=endMarker)
            inkDraw.line.relCoords(root_layer, [[10, 0], [10, -10]], [position[0], position[1] + 5], lineStyle=lineStylePlot)

        if so.markerType == 'arrow1':
            startMarker, endMarker = inkDraw.marker.createArrow1Marker(self, so.markerName + '_' + str(so.scale), RenameMode=int(so.renameMode),
                                                                       scale=0.4 * so.scale, strokeColor=lineColor, fillColor=markerColor)
            lineStylePlot = inkDraw.lineStyle.set(lineWidth=1, lineColor=lineColor, markerStart=startMarker, markerEnd=endMarker)
            inkDraw.line.relCoords(root_layer, [[10, 0], [10, -10]], [position[0], position[1] + 10], lineStyle=lineStylePlot)

        if so.markerType == 'cross':
            nameMarkerDot = inkDraw.marker.createCrossMarker(self, so.markerName + '_' + str(so.scale), RenameMode=int(so.renameMode),
                                                           scale=0.4 *so.scale, strokeColor=lineColor)
            lineStylePlot = inkDraw.lineStyle.set(lineWidth=1, lineColor=lineColor, markerStart=nameMarkerDot, markerEnd=nameMarkerDot)
            inkDraw.line.relCoords(root_layer, [[10, 0], [10, -10]], [position[0], position[1]], lineStyle=lineStylePlot)

        if so.markerType == 'custom':
            markerPath = so.makeCustomPathDef
            markerTransform = 'scale(' + str(so.scale) + ')'
            Marker = inkDraw.marker.createMarker(self, so.markerName + '_' + str(so.scale), markerPath=markerPath, RenameMode=int(so.renameMode),
                                                 strokeColor=lineColor, fillColor=markerColor, lineWidth=so.makeCustomLineWidth,
                                                 markerTransform=markerTransform)
            lineStylePlot = inkDraw.lineStyle.set(lineWidth=1, lineColor=lineColor, markerStart=Marker, markerEnd=Marker)
            inkDraw.line.relCoords(root_layer, [[10, 0], [10, -10]], [position[0], position[1] + 20], lineStyle=lineStylePlot)


if __name__ == '__main__':
    markers = CreateMarkers()
    markers.run()
