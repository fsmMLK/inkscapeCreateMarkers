# createMarkers
Inkscape extension to assist creating new markers with custom shape and colors.

<img src="docs/images/Examples.png" alt="Drawing" style="width: 300px;"/>

# Usage

This extension is presented in two tabs. The **Config** tab allows you set most of the options of your marker, while the **Color** tab allows you to select both stroke and filling colors.

<img src="docs/images/Screen_01.png" alt="Config" style="width: 300px;"/>
<img src="docs/images/Screen_02.png" alt="Color" style="width: 300px;"/>

### The Config tab

This tab is divided in three sections, on the first section **Predefined types**, you can create three predefined markers:

 - **Dot**: similar to some of the standard markers present in Inkscape, but you can choose the filling and stroke colors  independently
 - **Ellipsis**: this marker differs from Inkscape's standard marker (InfiniteLine) since the dots in this marker will follow the line width of your line (if scale factor is set to 1.0)
 - **Arrow1**: similar to Inkscape's standard Arrow1 marker, but you can choose the filling and stroke colors independently

<img src="docs/images/predefined_types.png" alt="Drawing" style="width: 300px;"/>

To create them, you just have to check the respective checkbox (you can check more than one). For each predefined marker you can give one nameID. Please see below how to configure its behavior when the extensions is faced with conflicting marker nameIDs.

In the second section **Custom type** you  can define your own custom markers. To do so, you must provide a valid SVG path's 'd' attribute. Please check any SVG reference on syntax, e.g., <https://developer.mozilla.org/en-US/docs/Web/SVG/Tutorial/Paths>. **Attention** This extension will not check the syntax of your definition. Luckily, providing an invalid attribute does not cause serious crashes, therefore you can activate the 'Live preview' checkbox to help you.

In the third section **General config settings** you can adjust the scale of your marker and the behavior in case of conflicting nameIDs (names already taken). You have three options:

  - **Do not modify the marker:**. If the nameID is already taken by another marker, the extension quits without modifying the marker
  - **Overwrites definition:**. If the nameID is already taken by another marker, the extension overwrites the marker. **Attention:** This will modify all instances of that marker in your document!
  - **Add suffix number to nameID:** If the nameID is already taken by another marker, Adds a suffix _nXXXXX, where XXXXX is a number that guarantees that nameID+_nXXXXX is unique.


### The Color tab

This tab is divided in two sections, the first refer to the filling color while the second to the stroke color.

In both cases, you can select a few predefined colors in the color drop down menu. Or select  **none** to set no color (transparent).

You can also select **use color picker** to choose the color from the color picker widget. **Attention:** the color selected in the color picker widget will be used **ONLY** if you select **use color picker** in the drop down menu. 

<img src="docs/images/Default_colors.png" alt="Color" style="width: 300px;"/>

### Observations

1- If you create more than one marker at once, then they will all share the same filling and stroke colors

2- One small line segment is created when you run the extension so that you can visualize the marker. This is specially useful when you check the 'Live preview' box.

3- The system of coordinates of the marker depends on the point under consideration. The following figure presents the coordinate system for all start, mid and end points. **Remember that +y points down in Inkscape!**

<img src="docs/images/marker_Orientation.png" alt="Drawing" style="width: 600px;"/>

# Behind the scene.

Behind the scenes, this extension is using employing inkscapeMadeEasy  <https://github.com/fsmMLK/inkscapeMadeEasy> extesnion. It uses mainly two classes defined in inkscapeMadeEasy_Draw.py to manage colors and create markers.

# Examples

<img src="docs/images/Examples.png" alt="Drawing" style="width: 300px;"/>


Blue cross: `M -3,3 L 3,-3 M 3,3 L -3,-3`

Smile boy: `M -5,0  a 5 5 0 1 1 10 0 a 5 5 0 1 1 -10 0 M -2,-3 v 2  M 2,-3 v 2  M -3,0  a 2 2 0 1 0 6 0 z`

Pac Boy: `M 4,3  a 5,5 0 0 1 -4 2 a 5,5 0 0 1 0,-10 a 5 ,5 0 0 1 4,2 L 0,0 z`

Ghosty (small): `M -5,0  a 5,5 0 0 1 10 0 l 0 6 l -2.5,-2.5 -2.5,2.5 -2.5,-2.5 -2.5,2.5 z M -2,1 l -0 -3 M 2,1 l -0 -3`

Ghosty (large): The same, but with different colors and scale factor

# Installation and requirements

This extension was partially developed in inkscape 0.48 and partially in 0.91 in Linux (Kubuntu 12.04 and 14.04). It should work on both versions of Inkscape. Also, they should work in differente OSs too as long as all requirements are installed.

This extension requires another extension to run, inkscapeMadeEasy <https://github.com/fsmMLK/inkscapeMadeEasy>, which contains several backstage methods and classes.

In order to use createMarkers extension, you must also download inkscapeMadeEasy files and put them both inside Inkscape's extension directory. Please refer to inkscapeMadeEasy installation instructions. In the end you must have the following files and directories in your Inkscape extension directory.

```
inkscape/extensions/
            |-- inkscapeMadeEasy_Base.py
            |-- inkscapeMadeEasy_Draw.py
            |-- inkscapeMadeEasy_Plot.py
            |-- textextLib
            |   |-- __init__.py
            |   |-- basicLatexPackages.tex
            |   |-- textext.inx
            |   |-- textext.py
            |
            |-- createMarkers.py
            `-- createMarkers.inx
```

