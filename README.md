# AB-Testing
MIUUL Data Science and Machine Learning Bootcamp Projesi

## İş Problemi
  Facebook kısa süre önce mevcut "maximum bidding" adı verilen teklif verme türüne alternatif
olarak yeni bir teklif türü olan "average bidding"i tanıttı. Müşterilerimizden biri, 
bu yeni özelliği test etmeye karar verdi ve average bidding'in maximum bidding'den daha fazla dönüşüm
getirip getirmediğini anlamak için bir A/B testi yapmak istiyor. A/B testi 1 aydır devam ediyor ve
müşterimiz şimdi sizden bu A/B testinin sonuçlarını analiz etmenizi bekliyor. Müşterimiz için
nihai başarı ölçütü Purchase'dır. Bu nedenle, istatistiksel testler için Purchase metriğine odaklanılmalıdır.

## Veri Seti Hikâyesi
  Bir firmanın web site bilgilerini içeren bu veri setinde kullanıcıların gördükleri ve tıkladıkları
reklam sayıları gibi bilgilerin yanı sıra buradan gelen kazanç bilgileri yer almaktadır. Kontrol ve Test
grubu olmak üzere iki ayrı veri seti vardır. Bu veri setleri  ab_testing.xlsx excel’inin ayrı sayfalarında yer 
almaktadır. Kontrol grubuna Maximum Bidding, test grubuna Average Bidding uygulanmıştır.

**impression**: Reklam görüntüleme sayısı \
**Click**: Görüntülenen reklama tıklama sayısı \
**Purchase**: Tıklanan reklamlar sonrası satın alınan ürün sayısı \
**Earning**: Satın alınan ürünler sonrası elde edilen kazanç
