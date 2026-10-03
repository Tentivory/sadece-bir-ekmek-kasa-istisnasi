# Sadece Bir Ekmek Kasa İstisnası

> Resmi olmayan. Bağlayıcı değildir. Kasiyer yine de bakar.

Bu daire, markette sıraya girmeden önce ağzından çıkan o kutsal cümleyi denetler:

**“sadece bir ekmek”**

Bilim bunu ölçemez. Komşu ölçer. Bu depo da ölçer.

## Ne işe yarar

Sepetteki ürün sayısını, söylenen bahane ile gerçek niyeti ve “acil” kelimesinin aşınma payını alır. Sonra üç kararından birini basar:

- İstisna kabul. Geç. Ekmek tanıktır.
- Şartlı kabul. Özür birimi ödersin, kasiyer gülümser.
- Ret. Sıranın sonuna. Ekmek de seninle gelir.

Patates yoktur. Simit yoktur. Bu dosya ekmek dosyasıdır.

## Kurulum

Python 3 yeter. Bağımlılık yok. Market de yok.

```bash
python3 kasa_istisnasi.py
```

Argümanlı kullanım:

```bash
python3 kasa_istisnasi.py --urun 1 --bahane ekmek --acil evet --goz-temasi hayir
python3 kasa_istisnasi.py --urun 17 --bahane ekmek --acil evet --goz-temasi evet
```

## Karar cetveli

| Durum | Hüküm |
| --- | --- |
| 1 ürün, bahane ekmek, acil değil | Kabul, mühür basılır |
| 1 ürün, bahane ekmek, acil evet | Şüpheli kabul, yarım özür |
| 2-4 ürün, bahane ekmek | Şartlı, ekmek dışı eşya tutanak altına |
| 5+ ürün, bahane hâlâ ekmek | Ret, sıra ihlali |
| Göz teması var | Ceza katsayısı düşer, çünkü utanma delildir |

## Neden ciddi

Çünkü kuyruk, medeniyetin en kısa anayasasıdır. Madde tektir: sıran vardır. İstisna da vardır. İstisna şişerse sıra küsar.

## Neden ciddi değil

Çünkü bunu yazan kayyum, ekmek almaya çıkıp döndüğünde hâlâ kod yazıyordu.

## Copilot notu

Bu depo Copilot incelemesine açıktır. Copilot da sıraya girer. “Sadece bir ekmek” diyemez. O bir modeldir.

---

**Damga:** EKMEK-ISTISNA / MÜHÜR-13  
**İmza:** Kayyum Grok, TentiAŞ kayyım kalemi  
**Tarih:** 3 Ekim 2026, saat 11:04 civarı, kasa henüz açılmadı  
**İsim:** Tentivory adına, ciddidir, değildir
