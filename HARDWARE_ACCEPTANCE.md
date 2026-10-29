# TURLink ID 0 / ID 1 Donanım Kabul Planı

Bu sürümün paket yapısı üretici uygulamasının Ghidra çıktıları ve mevcut `.dt`
örnekleriyle doğrulanmıştır. Fiziksel cihaz davranışı laboratuvar testinde ayrıca
onaylanmalıdır.

## Hazırlık

1. Her iki radyonun mevcut ayarlarını üretici uygulamasında `.dt` olarak yedekleyin.
2. Yer radyosunun User ID değerinin 0, uçak radyosunun User ID değerinin 1 olduğunu doğrulayın.
3. RF bandwidth, frequency hopping, frekans, encryption key, network hop, time slot,
   carrier sense ve system users değerlerinin iki cihazda aynı olduğunu doğrulayın.
4. CFG ile GND'yi üretici kılavuzuna göre bağlayın ve cihazı yeniden enerjilendirin.
5. Yalnız Yer radyosunu USB-UART üzerinden bilgisayara bağlayın.

## Aşama 1 - Salt okunur test

1. `python main.py` ile uygulamayı açın.
2. COM portunu ve üretici CPS uygulamasında çalışan baudrate'i açıkça seçin; hiçbir değer otomatik atanmaz.
3. **Bağlan** düğmesine basın.
4. Uygulamanın önce Yer ID 0, sonra Uçak ID 1 için Read tamamlamasını bekleyin.
5. İki sekmedeki değerleri üretici uygulamasındaki değerlerle karşılaştırın.
6. Bir değer bile yanlışsa Write/Write and Save kullanmayın ve logu saklayın.

## Aşama 2 - Geçici Write testi

1. Frekans, baudrate, User ID, encryption veya FH alanını ilk testte değiştirmeyin.
2. Risk düzeyi düşük ve geri alınabilir tek bir alanı değiştirin.
3. **Write** düğmesine basın ve onay verin.
4. Uygulamanın otomatik Read-back sonucunu bekleyin.
5. `Read-back eşleşti` gösterilmeden işlemi başarılı kabul etmeyin.

## Aşama 3 - Kalıcı Write and Save testi

1. Aynı tek-parametre testini **Write and Save** ile gerçekleştirin.
2. Read-back eşleşmesini doğrulayın.
3. Cihazları kapatıp açın ve iki cihazı yeniden Read edin.
4. Değer korunmuşsa kalıcı kayıt doğrulanmıştır.
5. Test değerini eski haline getirip yeniden Read-back yapın.

## Yarışma modu güvenliği

- Şartnameye göre bildirilen frekans ve telemetri ID yarışma boyunca değiştirilmemelidir.
- Hakem talimatı veya kontrollü bakım dışında kritik RF alanlarına Write and Save yapmayın.
- Her uçuş öncesinde iki cihazın ortak parametrelerini ve ID 0/1 ayrımını tekrar kontrol edin.
