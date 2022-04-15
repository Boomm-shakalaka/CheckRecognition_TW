# CheckRecognition_TW
### 使用CTPN和CRNN神经网络，通过深度学习来识别台湾支票的项目。
------ 
## 文件说明  
1. CRNN: 包含CRNN架构模型  
2. CRNN_model: 包含已训练的针对汉字日期以及数字识别模型  
   模型链接：[阿里云盘](https://www.aliyundrive.com/s/YySToVjVPoe)  
3. CTPN：包含CTPN构架模型
4. CTPN_model：包含已训练的针对目标检测模型  
   模型链接：[阿里云盘](https://www.aliyundrive.com/s/Nby8cpdgadz)    
5. icon 文件夹：系统内的图标和图案  
6. MICR 文件夹：包含 MICR 架构模型  
7. MICR_model：包含 MICR 模型  
8. SQL 文件夹：包含数据库处理相关 Python 档案以及数据库文件  
9. Check_demo：包含可以用于快速测试系统功能的支票图片  
10. RecognitionLoad.py：登录界面  
11. RecognitionMain.py：识别主界面  
12. RecognitionModel.py：支票识别模型  
13. RecognitionRegister.py：注册界面  
14. RecognitionLoad.spec: pyinstaller 生成 exe(小黑 pyinstaller RecognitionLoad.spec) 
------ 
## demo
1. 安装完系统后，点击 RecognitionLoad.py 进入登录界面。输入邮箱、密码以及可以进入本系统。默认账户密码和授权码都为admin。  
   ![alt 文字](https://raw.githubusercontent.com/adam-p/markdown-here/master/src/common/images/icon48.png)  



  




