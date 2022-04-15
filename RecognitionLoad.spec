# -*- mode: python ; coding: utf-8 -*-


block_cipher = None
excluded_modules = ['torch.distributions']

a = Analysis(['RecognitionLoad.py','RecognitionMain.py','RecognitionRegister.py','RecognitionModel.py',
				'CRNN/dataset.py',
				'CRNN/demo.py',
				'CRNN/utils.py',
				'CRNN/models/crnn.py',
				'CTPN/main/demo.py',
				'CTPN/nets/model_train.py',
				'CTPN/nets/vgg.py',
				'CTPN/utils/bbox/bbox_transform.py',
				'CTPN/utils/bbox/setup.py',
				'CTPN/utils/dataset/data_provider.py',
				'CTPN/utils/dataset/data_util.py',
				'CTPN/utils/prepare/split_label.py',
				'CTPN/utils/prepare/utils.py',
				'CTPN/utils/rpn_msr/anchor_target_layer.py',
				'CTPN/utils/rpn_msr/config.py',
				'CTPN/utils/rpn_msr/generate_anchors.py',
				'CTPN/utils/rpn_msr/proposal_layer.py',
				'CTPN/utils/text_connector/detectors.py',
				'CTPN/utils/text_connector/other.py',
				'CTPN/utils/text_connector/text_connect_cfg.py',
				'CTPN/utils/text_connector/text_proposal_connector.py',
				'CTPN/utils/text_connector/text_proposal_connector_oriented.py',
				'CTPN/utils/text_connector/text_proposal_graph_builder.py',
				'MICR/bank_check_ocr_1.py',
				'MICR/bank_check_ocr_2.py',
				'SQL/Commonutil.py',
				'SQL/sqlite.py'],
             pathex=['E:\\desktop\\check_recognition_v2\\RecognitionLoad.py'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=excluded_modules,
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts, 
          [],
          exclude_binaries=True,
          name='RecognitionLoad',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas, 
               strip=False,
               upx=True,
               upx_exclude=[],
               name='RecognitionLoad')
