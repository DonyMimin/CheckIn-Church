# -*- mode: python ; coding: utf-8 -*-

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('ultralytics/cfg/default.yaml', 'ultralytics/cfg')
    ],
    hiddenimports=[
        'scipy.special._cdflib',
        'cv2',  # Menambahkan OpenCV
        'PyQt5',  # Menambahkan PyQt5
        'PyQt5.QtCore',  # Menambahkan PyQt5 core
        'PyQt5.QtGui',   # Menambahkan PyQt5 GUI
        'PyQt5.QtWidgets',  # Menambahkan PyQt5 widgets
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=['my_hook.py'],
    excludes=['tkinter'],
    noarchive=False,
    optimize=0,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='CheckIn-Church',
    debug=True,  # Mengaktifkan mode debug
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    console=True,  # Mengaktifkan console untuk melihat output
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    onefile=False,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='main',
)
