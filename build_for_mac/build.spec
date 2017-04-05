# -*- mode: python -*-
import os

block_cipher = None

# collect resources
RESOURCE_ROOT = 'resources'
datas = []
for dirpath, _, filenames in os.walk(os.path.join('..', RESOURCE_ROOT)):
    for filename in filenames:
        datas.append((
            os.path.join(dirpath.replace('../', ''), filename),
            os.path.join(dirpath, filename),
            'DATA'))

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

a.datas.extend(datas)

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
    name='Gazer.app',
    icon='../resources/gazer.icns',
    bundle_identifier=None,
    info_plist={
        'NSHighResolutionCapable': 'True'})
