@echo off
REM TURLink_Manager icin tek dosya, tasinabilir EXE derleme scripti.
REM Bu dosyayi Windows'ta, proje klasorunun icinde (main.py ile ayni yerde) calistir.

echo === Sanal ortam olusturuluyor ===
python -m venv build_venv
call build_venv\Scripts\activate.bat

echo === Bagimliliklar kuruluyor ===
python -m pip install --upgrade pip
pip install -r requirements.txt
pip install pyinstaller

echo === EXE derleniyor ===
pyinstaller turlink_manager.spec --noconfirm

echo.
echo === Bitti ===
echo Cikti dosyasi: dist\TURLink_Manager.exe
echo Bu tek dosyayi baska bir Windows bilgisayara kopyalayip dogrudan calistirabilirsin.
pause
