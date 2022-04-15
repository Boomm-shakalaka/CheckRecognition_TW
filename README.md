# CheckRecognition_TW
### 使用CTPN和CRNN神经网络，通过深度学习来识别台湾支票的项目。
------ 
## 文件说明  
1. CRNN: 包含CRNN架构模型  
2. CRNN_model: 包含已训练的针对汉字日期以及数字识别模型  
   模型链接：[阿里云盘](https://www.aliyundrive.com/s/YySToVjVPoe)  [Google Drive](https://drive.google.com/drive/folders/1CFXPSx7HKxrQfYx4MEQR4wN4NhnJPp78?usp=sharing)  
3. CTPN：包含CTPN构架模型
4. CTPN_model：包含已训练的针对目标检测模型  
   模型链接：[阿里云盘](https://www.aliyundrive.com/s/Nby8cpdgadz)  [Google Drive](https://drive.google.com/drive/folders/1WtgV501g2j6PjNdsa37zTPJz-LHUk7_q?usp=sharing)
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
  
   ![alt 文字](https://github.com/Boomm-shakalaka/CheckRecognition_TW/blob/master/demo_pic/load.png)  
   
2. 第一次使用的用户可以点击注册按钮进入注册窗口。通过自己的邮箱验证码进行绑定，所有用户数据都将会保存在数据库中(SQL 文件夹)。  
3. 进入本系统，是整个支票识别的主视窗，左边部分是输出结果和控制台部分。中间由信息交互窗口以及可视化路径组成。最右边是支票图像展示区域以及相应的图像路径。 
  
   ![alt 文字](https://github.com/Boomm-shakalaka/CheckRecognition_TW/blob/master/demo_pic/main.png)
   
4. 本系统分为单张识别和批量识别模式，点击开始识别将调用。点击单张识别，通过可视化路径选择所要辨识的支票图片，再点击开始识别，系统会对支票自动进行辨识，并将文本结果输出到    左边显示框，并且在支票图像展示区域也会框选识别目标。使用者可以点击保存信息，将这次的识别结果先保存于后台。当遇到大量支票需要辨识时，可以选择批量识别模式，选择所要辨识    的支票文件夹，所有支票文件名会先显示在信息交互窗口。再点击开始识别，系统开始自动辨识，每张支票大概只消耗 2-3 秒的时间。等待辨识结束，可以点击保存信息将结果存于后台。  
   
   ![alt 文字](https://github.com/Boomm-shakalaka/CheckRecognition_TW/blob/master/demo_pic/recog.png)
   
5. 当所有辨识结果已经保存，可以点击上方导出按钮，系统会自动将已保存的支票信息生成一份 Excel 档案，以提供给用户进行后期使用。
