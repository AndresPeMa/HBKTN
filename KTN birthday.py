# -*- coding: utf-8 -*-
"""
Created on Wed May 17 22:38:18 2023

@author: andy_
"""
# Import turtle package
import turtle


# Creating a turtle object(pen)
pen = turtle.Turtle()
  

#Settings
turtle.bgcolor("black")
pen.color("red")
pen.pensize(0)
pen.speed(50)


# Defining a method to draw curve
def curve():
    for i in range(200):
  
        # Defining step by step curve motion
        pen.right(1)
        pen.forward(1)
  
# Defining method to draw a full heart
def heart():
  
    # Set the fill color to red
    pen.fillcolor('red')
  
    # Start filling the color
    pen.begin_fill()
  
    # Draw the left line
    pen.left(140)
    pen.forward(113)
  
    # Draw the left curve
    curve()
    pen.left(120)
  
    # Draw the right curve
    curve()
  
    # Draw the right line
    pen.forward(112)
  
    # Ending the filling of the color
    pen.end_fill()
  
    
    
# Defining method to write text
def txt():
  
    # Move turtle to air
    pen.up()
  
    # Move turtle to a given position
    pen.setpos(-105, 195)
  
    # Move the turtle to the ground
    pen.down()
  
    # Set the text color to lightgreen
    pen.color('PaleGreen1')
  
    # Write the specified text in 
    # specified font style and size
    pen.write("Happy Birthday Katelyn!", font=(
      "Verdana", 12, "bold"))
  
  
# Defining method to write text
def txt2():
  
    # Move turtle to air
    pen.up()
  
    # Move turtle to a given position
    pen.setpos(-20, -45)
  
    # Move the turtle to the ground
    pen.down()
  
    # Set the text color to lightgreen
    pen.color('PaleGreen1')
  
    # Write the specified text in 
    # specified font style and size
    pen.write("TQM!", font=(
      "Verdana", 12, "bold"))
    
    
    
# Draw a heart
heart()


# Write text1
txt()
  
# Write text2
txt2()

# To hide turtle
pen.ht()
