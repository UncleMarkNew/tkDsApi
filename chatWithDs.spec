# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['d:\\chatwithAPIkeep\\tkChatDsApi\\chatWithDs.py'],
    pathex=[],
    binaries=[],
    datas=[('config.txt', '.'), ('.env', '.')],  # Include data files
    hiddenimports=['docx', 'PyPDF2', 'openai', 'pywin32', 'pywin32_ctypes'],  # Add hidden imports
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
    a.binaries,
    a.datas,
    [],
    name='chatWithDs',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
