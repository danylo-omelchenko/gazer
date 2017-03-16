# -*- mode: python -*-

block_cipher = None


a = Analysis(
    ['../main.py'],
    pathex=['/Users/work/projects/swf_client'],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher)

pyz = PYZ(
    a.pure,
    a.zipped_data,
    cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    name='main',
    debug=True,
    strip=False,
    upx=True,
    console=False)

app = BUNDLE(
    exe,
    name='main.app',
    icon='../resources/icon.icns',
    bundle_identifier=None,
    info_plist={
        'NSHighResolutionCapable': 'True'})
