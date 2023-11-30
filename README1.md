### Reference Web

- https://max-everyday.com/2018/03/tixcraft-bot/


### Step

1. install python 3.10.X ( 我是使用 3.10.6)
2. 更新 pip
> ```
> python -m pip install --upgrade pip
> ```
3. 安裝 pip-req.txt 裡面的套件
> ```
> python -m pip install -r pip-req.txt
> ```
4. 安裝 chromedriver_autoinstaller
> ```
> python -m pip install chromedriver_autoinstaller 
>
> or 
>
> python -m pip install git+https://github.com/max32002/> python-chromedriver-autoinstaller@master
> ```

5. download webdriver (我是使用 edge)

> 在 chrome_tixcraft.py 的檔案裏面的 get_driver_by_config 方法，有每個 webdriver 載點

6. 在此專案的目錄下創建 webdriver 資料夾，把剛剛下載的 .exe 檔放進去。