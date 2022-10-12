import os
import math
import random
import pyautogui
import subprocess
from system_hotkey import SystemHotkey
import time
time.sleep(5)

# Playing around with pyautogui and SystemHotkey packages in Paint

pyautogui.FAILSAFE = False


# pyautogui.PAUSE = 0.5

def abort(self):
    print("ABORT")
    os._exit(0)


# Generate n x,y points of a circle of radius r
def PointsInCircum(r, n=100):
    return [(math.cos(2 * math.pi / n * x) * r, math.sin(2 * math.pi / n * x) * r) for x in range(0, n + 1)]


# Move cursor to center of screen, return coordinates (reduces repetition)
def moveToCenter():
    screenWidth, screenHeight = pyautogui.size()
    centerX = screenWidth / 2
    centerY = screenHeight / 2
    pyautogui.moveTo(centerX, centerY)
    return centerX, centerY


# Draw a shape of radius r (with a shape tool selected)
def drawShape(r):
    x, y = moveToCenter()
    pyautogui.moveRel(-r, -r)
    pyautogui.mouseDown()
    pyautogui.moveRel(r * 2, r * 2)
    pyautogui.mouseUp()
    moveToCenter()


# Draw three square spirals to test out pyautogui
def draw_test():
    pickRandomBrush()
    centerX, centerY = moveToCenter()
    distance = 200
    origDistance = distance
    while distance > 0:
        pyautogui.dragRel(distance, 0)
        distance -= 5
        pyautogui.dragRel(0, distance)
        pyautogui.dragRel(-distance, 0)
        distance -= 5
        pyautogui.dragRel(0, -distance)
    pyautogui.moveTo(centerX - origDistance, centerY)
    distance = origDistance
    while distance > 0:
        pyautogui.dragRel(distance, 0)
        distance -= 5
        pyautogui.dragRel(0, distance)
        pyautogui.dragRel(-distance, 0)
        distance -= 5
        pyautogui.dragRel(0, -distance)
    pyautogui.moveTo(centerX - origDistance, centerY - origDistance)
    distance = origDistance
    while distance > 0:
        pyautogui.dragRel(distance, 0)
        distance -= 5
        pyautogui.dragRel(0, distance)
        pyautogui.dragRel(-distance, 0)
        distance -= 5
        pyautogui.dragRel(0, -distance)


# Early experiment with pyautogui: Draw Captain America's shield using individual brush strokes
# Usage: call with a radius value with a brush tool selected in Paint.
# Try tweaking the radius and NumPoints in PointsInCircum for interesting effects!
# Simplified version is below (draw_shield)
def draw_circle(radius, numPoints):
    screenWidth, screenHeight = pyautogui.size()
    centerX = screenWidth / 2
    centerY = screenHeight / 2
    pyautogui.moveTo(centerX, centerY)
    pyautogui.click()
    points = PointsInCircum(radius, numPoints)
    pyautogui.click(x=830, y=62)
    for idx, val in enumerate(points):
        x, y = val
        pyautogui.moveTo(centerX, centerY)
        pyautogui.dragRel(x, y)
        points.reverse()
        x, y = points[idx]
        pyautogui.moveTo(centerX, centerY)
        pyautogui.dragRel(x, y)
        points.reverse()
    pyautogui.click(x=764, y=84)
    points = PointsInCircum(radius * 0.90, numPoints)
    for idx, val in enumerate(points):
        x, y = val
        pyautogui.moveTo(centerX, centerY)
        pyautogui.dragRel(x, y)
        points.reverse()
        x, y = points[idx]
        pyautogui.moveTo(centerX, centerY)
        pyautogui.dragRel(x, y)
        points.reverse()
    pyautogui.click(x=830, y=62)
    points = PointsInCircum(radius * 0.80, numPoints)
    for idx, val in enumerate(points):
        x, y = val
        pyautogui.moveTo(centerX, centerY)
        pyautogui.dragRel(x, y)
        points.reverse()
        x, y = points[idx]
        pyautogui.moveTo(centerX, centerY)
        pyautogui.dragRel(x, y)
        points.reverse()
    pyautogui.click(x=764, y=84)
    points = PointsInCircum(radius * 0.70, numPoints)
    for idx, val in enumerate(points):
        x, y = val
        pyautogui.moveTo(centerX, centerY)
        pyautogui.dragRel(x, y)
        points.reverse()
        x, y = points[idx]
        pyautogui.moveTo(centerX, centerY)
        pyautogui.dragRel(x, y)
        points.reverse()
    pyautogui.click(x=830, y=62)
    points = PointsInCircum(radius * 0.60, numPoints)
    for idx, val in enumerate(points):
        x, y = val
        pyautogui.moveTo(centerX, centerY)
        pyautogui.dragRel(x, y)
        points.reverse()
        x, y = points[idx]
        pyautogui.moveTo(centerX, centerY)
        pyautogui.dragRel(x, y)
        points.reverse()
    pyautogui.click(x=941, y=60)
    points = PointsInCircum(radius * 0.40, numPoints)
    for idx, val in enumerate(points):
        x, y = val
        pyautogui.moveTo(centerX, centerY)
        pyautogui.dragRel(x, y)
        points.reverse()
        x, y = points[idx]
        pyautogui.moveTo(centerX, centerY)
        pyautogui.dragRel(x, y)
        points.reverse()


# Wrapper function showing standard usage of draw_circle
def drawCircle():
    draw_circle(400, 300)


# Improved method to draw Captain America's shield using pyautogui.
# Switches colors in course of drawing each line, rather than painting and painting over
# draw_circle looks better, but draw_shield is much more efficient
def draw_shield(radius, numPoints):
    pyautogui.click(x=689, y=67)
    centerX, centerY = moveToCenter()
    points = PointsInCircum(radius, numPoints)
    points90 = PointsInCircum(radius * 0.90, numPoints)
    points80 = PointsInCircum(radius * 0.80, numPoints)
    points70 = PointsInCircum(radius * 0.70, numPoints)
    points60 = PointsInCircum(radius * 0.60, numPoints)
    points50 = PointsInCircum(radius * 0.50, numPoints)
    for idx in range(0, len(points)):
        x, y = points50[idx]
        pyautogui.click(x=941, y=60)
        pyautogui.moveTo(centerX, centerY)
        pyautogui.dragRel(x, y)
        x, y = pyautogui.position()
        x, y = points60[idx]
        pyautogui.dragRel(x, y)
        x, y = pyautogui.position()
        pyautogui.click(x=764, y=84)
        pyautogui.moveTo(x, y)
        x, y = points70[idx]
        pyautogui.dragRel(x, y)
        x, y = pyautogui.position()
        pyautogui.click(x=830, y=62)
        pyautogui.moveTo(x, y)
        x, y = points80[idx]
        pyautogui.dragRel(x, y)
        x, y = pyautogui.position()
        pyautogui.click(x=764, y=84)
        pyautogui.moveTo(x, y)
        x, y = points90[idx]
        pyautogui.dragRel(x, y)
        x, y = pyautogui.position()
        pyautogui.click(x=830, y=62)
        pyautogui.moveTo(x, y)
        x, y = points[idx]
        pyautogui.dragRel(x, y)
    pyautogui.click(x=764, y=84)
    pyautogui.click(x=421, y=102)
    pyautogui.click(x=733, y=68)
    pyautogui.click(x=764, y=84)
    moveToCenter()
    drawShape(radius * 0.50)


# Wrapper function showing standard usage of draw_shield
def drawShield():
    moveToCenter()
    pyautogui.click(x=689, y=67)
    draw_shield(80, 100)


# Simple test to do some recursive drawing
def draw_node(step, centerX, centerY):
    pyautogui.moveTo(centerX, centerY)
    radius = random.randrange(10, 200, 1)
    numSpokes = random.randrange(5, 100, 1)
    points = PointsInCircum(radius, numSpokes)
    for x, y in points:
        pyautogui.dragRel(x, y)
        pyautogui.moveTo(centerX, centerY)
    if step > 0:
        gen_Point = random.randrange(0, len(points) - 1, 1)
        x, y = points[gen_Point]
        pyautogui.dragRel(x, y)
        newStep = step - 1
        newCenterX, newCenterY = pyautogui.position()
        draw_node(newStep, newCenterX, newCenterY)


# Kick off recursive draw_node from the center of the screen
def complexDrawing():
    centerX, centerY = moveToCenter()
    draw_node(centerX, centerY, 100, 5)


# Select a random color from the color bar
def pickRandomColor():
    colorX = [805, 831, 854, 872, 894, 920, 942, 959]
    colorY = [59, 81]
    colXIdx = random.randrange(0, len(colorX), 1)
    colYIdx = random.randrange(0, 2, 1)
    pyautogui.click(colorX[colXIdx], colorY[colYIdx])
    return colXIdx, colYIdx


# Select a random shape tool from the "Shapes" dialog
def pickRandomShape():
    moveToCenter()
    pyautogui.click()
    shapeXIdx = random.choice([396, 421, 442, 461, 480, 498])
    shapeYIdx = random.choice([66, 85, 102])
    pyautogui.click(shapeXIdx, shapeYIdx)
    return shapeXIdx, shapeYIdx


# Select a random brush type from the "Brushes" menu
def pickRandomBrush():
    moveToCenter()
    pyautogui.click()
    located = locate_Click('BrushMenu.png')
    if not located:
        locate_Click('BrushMenu2.png')
    brushX = [332, 373, 417, 463]
    brushY = [135, 181, 211]
    brushXIdx = random.randrange(0, len(brushX))
    brushYIdx = random.randrange(0, len(brushY))
    if brushXIdx > 0 and brushYIdx > 0:
        brushYIdx = 0
    pyautogui.moveTo(brushX[brushXIdx], brushY[brushYIdx])
    pyautogui.click(clicks=2, interval=0.25)
    return brushXIdx, brushYIdx


# My personal favorite recursive web drawing function, iterates upon draw_node above (adds range checking,
# increases numSpokes as we approach base case)
def draw_Otra(step, centerX, centerY, radius, numSpokes):
    if centerY < 170 or centerY > 990 or centerX < 10 or centerX > 1070:
        screenWidth, screenHeight = pyautogui.size()
        centerX = screenWidth / 2
        centerY = screenHeight / 2
    pyautogui.moveTo(centerX, centerY)
    points = PointsInCircum(radius, numSpokes)
    for x, y in points:
        pyautogui.dragRel(x, y)
        if step > 0:
            newStep = step - 1
            newRadius = radius / 2
            newNumSpokes = numSpokes + 2
            newCenterX, newCenterY = pyautogui.position()
            draw_Otra(newStep, newCenterX, newCenterY, newRadius, newNumSpokes)
        pyautogui.moveTo(centerX, centerY)


# Wrapper to call above function with random brush type and set seed values
def drawOtraWrapper():
    pickRandomBrush()
    centerX, centerY = moveToCenter()
    draw_Otra(5, centerX, centerY, 2400, 4)


# Very similar to draw_Otra, doesn't change numSpokes. Again, try messing around with these step, radius, and numSpokes values
# for some interesting effects!
def draw_modified(step, centerX, centerY, radius, numSpokes):
    colorX = [805, 831, 854, 872, 894, 920, 942, 959]
    colorY = [59, 81]
    colXIdx, colYIdx = pickRandomColor()
    oldCenterX = centerX
    oldCenterY = centerY
    if centerY < 170:
        centerY = 990 - (centerY + 170)
        oldCenterY = 988
    if centerY > 990:
        centerY = 170 + (centerY - 990)
        oldCenterY = 172
    if centerX < 10:
        centerX = 1070 - (centerX + 10)
        oldCenterX = 1068
    if centerX > 1070:
        centerX = 10 + (centerX - 1070)
        oldCenterX = 12
    if pyautogui.onScreen(oldCenterX, oldCenterY) and pyautogui.onScreen(centerX, centerY):
        pyautogui.moveTo(oldCenterX, oldCenterY)
        pyautogui.dragTo(centerX, centerY)
    else:
        centerX, centerY = moveToCenter()
    points = PointsInCircum(radius, numSpokes)
    numPoints = len(points)
    flipFlag = random.randrange(0, 100, 1)
    if flipFlag > 50:
        points.reverse()
    startIdx = random.randrange(0, numPoints - 1, 1)
    endIdx = random.randrange(startIdx, numPoints - 1, 1)
    if startIdx >= endIdx:
        startIdx = 0
    for idx in range(startIdx, endIdx):
        x, y = points[idx]
        pyautogui.dragRel(x, y)
        if step > 0:
            newStep = step - 1
            newRadius = radius / 2
            newCenterX, newCenterY = pyautogui.position()
            drawModified(newStep, newCenterX, newCenterY, newRadius, numSpokes)
        pyautogui.click(x=colorX[colXIdx], y=colorY[colYIdx])
        pyautogui.moveTo(centerX, centerY)


# Wrapper to kick off draw_Modified recursive function
def drawWeb():
    # pickRandomBrush()
    centerX, centerY = moveToCenter()
    drawModified(5, centerX, centerY, 2400, 4)


# Call draw_Modified with random parameters
def drawRandWeb():
    centerX, centerY = moveToCenter()
    r = random.randrange(800, 2400)
    spokes = random.randrange(4, 12)
    drawModified(5, centerX, centerY, r, spokes)


# Helper function to determine on-screen location of items. Usage: call loc_helper and nothing else, press Ctrl+F to print the x,y
# coordinates of the mouse
def loc_helper(self):
    print(pyautogui.position())


# Locate and move to the center of the image provided by 'img'. Note that you must provide full filename e.g. 'example.png' or it
# will fail. Also, the image must be in the same directory as this script.
def locate_MoveTo(img):
    imgLocated = False
    try:
        left, top, width, height = pyautogui.locateOnScreen(img)
        imgLocated = True
    except (FileNotFoundError, TypeError) as e:
        print("locate_MoveTo failed:", e)
        print('unable to find: ', img)
        return False
    if imgLocated:
        pyautogui.moveTo(x=left + (width / 2), y=top + (height / 2))
        return True


# Locate and click on the image provided by 'img'. Useful for selecting specific controls.
def locate_Click(img):
    found = locate_MoveTo(img)
    if found:
        pyautogui.click()
    return found


# Currently unused, was toying around with opening and maximizing Paint when this script is run.
def launch_subprocess(path):
    subprocess.Popen([path])


# Draw a spiral by first calculating the PointsInCircum for a number of radii using a list comprehension.
def draw_spiral():
    # moveToCenter()
    screenWidth, screenHeight = pyautogui.size()
    centerX = screenWidth / 2
    centerY = screenHeight / 2
    pyautogui.moveTo(centerX, centerY)
    numPoints = 60
    startRadius = 30
    for i in range(0, 10):
        points = [PointsInCircum(x, numPoints) for x in range(startRadius, startRadius + numPoints)]
        innerIdx = 0
        for idx in range(0, len(points)):
            arr = points[idx]
            x, y = arr[idx]
            pyautogui.moveRel(x, y)
            pyautogui.mouseUp()
            pyautogui.moveTo(centerX, centerY)
            pyautogui.click()
            pyautogui.moveRel(x, y)
            pyautogui.mouseDown()
            pyautogui.moveTo(centerX, centerY)
            # innerIdx += 1
        startRadius += numPoints


# Draw a number of concentric shapes
def draw_Concentric():
    pickRandomShape()
    for r in range(5, 200, 20):
        drawShape(r)


# Clear the canvas: select all -> delete
def clear_Canvas():
    moveToCenter()
    pyautogui.click()
    found = locate_Click('SelectMenu.png')
    if not found:
        locate_Click('SelectMenu2.png')
    pyautogui.press(['down', 'down', 'down'])
    pyautogui.press('enter')
    pyautogui.press('delete')


hk = SystemHotkey()
hk.register(('control', 'x'), callback=abort)
hk.register(('control', 'f'), callback=loc_helper)


# Playing around with looking up a function in a dict
def totalRandomDrawing():
    funcdict = {
        'draw_Concentric': draw_Concentric,
        'drawRandWeb': drawRandWeb,
        'drawCircle': drawCircle,
        'drawShield': drawShield
    }
    random.choice(list(funcdict.values()))()


if __name__ == "__main__":
    totalRandomDrawing()