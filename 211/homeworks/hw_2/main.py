"""Homework 2
Quinn Smiley, 2026-04-13, CS 211"""

from controller import Controller
from model import Model
from view import View


def main():
    model = Model()
    view = View()
    controller = Controller(model, view)
    controller.main_loop()


if __name__ == "__main__":
    main()

