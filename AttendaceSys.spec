# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['F:/Python3.8/Project/AttendaceSys.py'],
    pathex=[],
    binaries=[],
    datas=[('F:/Python3.8/Project/attendance.csv', '.'), ('F:/Python3.8/Project/TrainingImage', 'TrainingImage/')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='AttendaceSys',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='AttendaceSys',
)
