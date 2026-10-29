# -*- mode: python ; coding: utf-8 -*-
# TURLink Radio Management & Link Monitor - taşınabilir tek dosya EXE derlemesi
#
# Kullanım (Windows üzerinde, proje klasöründe):
#   pyinstaller turlink_manager.spec
#
# Çıktı: dist/TURLink_Manager.exe  (tek dosya, başka bilgisayara kopyalanıp
# hiçbir kurulum yapılmadan çalıştırılabilir; sadece PySide6'nın Windows'ta
# ihtiyaç duyduğu standart VC++ çalışma zamanı genelde sistemde zaten vardır)

block_cipher = None

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[
        'PySide6.QtCore',
        'PySide6.QtGui',
        'PySide6.QtWidgets',
        'serial',
        'serial.tools.list_ports',
        'pymavlink',
    ],
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
    name='TURLink_Manager',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,      # arka planda konsol penceresi açılmasın istersen False kalsın
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    # icon='app_icon.ico',   # istersen kendi ikon dosyanı ekleyip bu satırı aç
)
