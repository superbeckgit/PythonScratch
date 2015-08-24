# -*- coding: utf-8 -*-
"""
Created on Tue Jan  6 16:14:56 2015

@author: mjbeck

Draw a series of squares to explore basic turtle usage
"""

import turtle

def draw_square(pen):
    """ draws a 100px X 100px square using the incoming turtle object """
    for i in range(4):
        pen.forward(100)
        pen.right(90)

def draw_art():
    """ creates a turtle object, draws 36 squares each rotated 10 degrees from the last """
    window = turtle.Screen();
    window.bgcolor('blue')

    pen = turtle.Turtle()
    pen.color('red')
    pen.speed(0)
    for i in range(36):
        draw_square(pen)
        pen.right(10)
    window.exitonclick()

if __name__ == '__main__':
    draw_art()
