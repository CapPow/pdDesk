# -*- mode: python -*-

block_cipher = None


a = Analysis(['collBook.py'],
             pathex=['C:\\Users\\Shawlab\\Documents\\collBook'],
             binaries=[],
             datas=[],
             hiddenimports=["reportlab.graphics.barcode.code39","reportlab.graphics.barcode.code93","reportlab.graphics.barcode.code128","reportlab.graphics.barcode.usps","reportlab.graphics.barcode.usps4s","reportlab.graphics.barcode.ecc200datamatrix"],
             hookspath=[],
             runtime_hooks=[],
             excludes=['PyQt4','matplotlib','scipy','wx','IPython','tkinter','tk'],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='collBook',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False, 
	  icon="collBookIcon.ico")
