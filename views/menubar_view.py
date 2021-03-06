from auri.vendor.Qt import QtWidgets
from functools import partial


class MenuBarView(QtWidgets.QMenuBar):
    def __init__(self, common_ctrl, main_ctrl):
        """

        Args:
            common_ctrl (auri.controllers.common_controller.CommonController):
            main_ctrl (auri.controllers.main_controller.MainController):
        """
        self.common_ctrl = common_ctrl
        self.main_ctrl = main_ctrl
        super(MenuBarView, self).__init__()

        file_menu = self.addMenu("&File")
        file_menu.addAction(self.new_project_action())
        file_menu.addAction(self.open_project_action())
        file_menu.addAction(self.save_project_action())
        file_menu.addAction(self.save_project_as_action())
        file_menu.addAction(self.import_project_action())

        edit_menu = self.addMenu("&Edit")
        edit_menu.addAction(self.refresh_action())
        edit_menu.addAction(self.prebuild_all_action())
        edit_menu.addAction(self.execute_all_action())

        about_menu = self.addMenu("&Help")
        about_menu.addAction(self.about_action())

        # about_menu = self.addMenu("&About")

    def new_project_action(self):
        action = QtWidgets.QAction("&New Project", self)
        action.triggered.connect(self.common_ctrl.new_project)
        action.setShortcut("Ctrl+N")
        action.setStatusTip("Clear current project")
        return action

    def open_project_action(self):
        action = QtWidgets.QAction("&Open Project", self)
        action.triggered.connect(self.common_ctrl.open_project)
        action.setShortcut("Ctrl+O")
        action.setStatusTip("Open a project")
        return action

    def save_project_action(self):
        action = QtWidgets.QAction("&Save Project", self)
        action.triggered.connect(self.common_ctrl.save_project)
        action.setShortcut("Ctrl+S")
        action.setStatusTip("Save current project")
        return action

    def save_project_as_action(self):
        action = QtWidgets.QAction("Save Project &As", self)
        action.triggered.connect(self.common_ctrl.save_project_as)
        action.setShortcut("Ctrl+Shift+S")
        action.setStatusTip("Save current project as")
        return action

    def import_project_action(self):
        action = QtWidgets.QAction("Import Project", self)
        action.triggered.connect(partial(self.common_ctrl.open_project, True))
        action.setShortcut("Ctrl+I")
        action.setStatusTip("Import & append a project to the currect project")
        return action

    def refresh_action(self):
        action = QtWidgets.QAction("&Refresh", self)
        action.triggered.connect(self.common_ctrl.refresh)
        action.setShortcut("Ctrl+R")
        action.setStatusTip("Refresh categories & scripts")
        return action

    def prebuild_all_action(self):
        action = QtWidgets.QAction("Pre&build All", self)
        action.triggered.connect(self.main_ctrl.prebuild_all)
        action.setShortcut("Ctrl+B")
        action.setStatusTip("Launch the Prebuild function of every scripts")
        return action

    def execute_all_action(self):
        action = QtWidgets.QAction("&Execute All", self)
        action.triggered.connect(self.main_ctrl.execute_all)
        action.setShortcut("Ctrl+E")
        action.setStatusTip("Launch the Execute function of every scripts")
        return action

    def about_action(self):
        action = QtWidgets.QAction("&About", self)
        action.triggered.connect(self.main_ctrl.show_about)
        action.setShortcut("Ctrl+Alt+A")
        action.setStatusTip("Show the About window")
        return action
