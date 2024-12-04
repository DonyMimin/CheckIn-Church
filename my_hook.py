import cv2
import os
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = os.path.join(os.path.dirname(cv2.__file__), 'qt', 'plugins')
