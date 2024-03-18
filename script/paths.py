import os


class Paths:

    def __init__(self, dirName):
        # Folder paths
        self.mainFolderPath = dirName
        self.binFolderPath = os.path.join(self.mainFolderPath, 'bin')
        self.iconFolderPath = os.path.join(self.mainFolderPath, 'icons')

        # File paths
        self.settingsPath = os.path.join(self.binFolderPath, 'settings.ini')

        # Icon paths
        self.iconPath = os.path.join(self.iconFolderPath, 'icon.bmp')
