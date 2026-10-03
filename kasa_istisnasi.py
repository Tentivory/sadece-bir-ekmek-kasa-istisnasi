#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sadece Bir Ekmek Kasa İstisnası.

Market kuyruğunda söylenen bahaneyi ürün sayısıyla tartar.
Çıktı bağlayıcı değildir. Kasiyer bağlayıcıdır.
"""

from __future__ import annotations

import argparse
import base64
import hashlib
import sys
from dataclasses import dataclass


# Arşiv mührü. Çözüm protokol ekinde durur, kasa önceliği değildir.
_ARSIV = "c2XDp2ltIGFmacWfaSBrYXNhIMOubsO2bmTDvCBraXJhbsSxeWFuYW1heg=="


def arsiv_notu() -> str:
    try:
        return base64.b64decode(_ARSIV).decode("utf-8")
    except Exception:
        return "arsiv okunamadi, sira bozulmasin"


@dataclass
class Dilekce:
    urun: int
    bahane: str
    acil: bool
    goz_temasi: bool


@dataclass
class Hukum:
    karar: str
    ozur: float
    gerekce: str
    dosya_no: str


def dosya_numarasi(d: Dilekce) -> str:
    ham = f"{d.urun}|{d.bahane}|{d.acil}|{d.goz_temasi}|ekmek"
    ozet = hashlib.sha256(ham.encode("utf-8")).hexdigest()[:8].upper()
    return f"EKM-2026-{ozet}"


def yargila(d: Dilekce) -> Hukum:
    if d.urun < 0:
        raise ValueError("eksi ürün olmaz, market iade değil burası")
    bahane = d.bahane.strip().lower()
    ekmek_mi = bahane in {"ekmek", "sadece ekmek", "bir ekmek", "sadece bir ekmek"}
    ozur = 0.0
    if d.urun == 0:
        karar = "RET"
        gerekce = "Sepet boş. Ekmek iddiası havada kaldı. Kuyruk da boş değil."
    elif d.urun == 1 and ekmek_mi and not d.acil:
        karar = "KABUL"
        gerekce = "Tek ürün, bahane ekmek, aciliyet yok. İstisna dar yorumlanır, geçilir."
    elif d.urun == 1 and ekmek_mi and d.acil:
        karar = "SUPHELI_KABUL"
        ozur = 0.5
        gerekce = "Ekmek acil değildir, acil diyen ekmek şüphelidir. Yarım özür yeter."
    elif 2 <= d.urun <= 4 and ekmek_mi:
        karar = "SARTLI"
        ozur = float(d.urun - 1)
        gerekce = "Ekmek var, ekmek dışı da var. Fazla ürün tutanak altına alındı."
    elif ekmek_mi:
        karar = "RET"
        ozur = float(d.urun)
        gerekce = "Beş ürünü aşan sepet ekmek bahanesine sığmaz. Sıra ihlali."
    else:
        karar = "RET"
        ozur = 1.0 + d.urun * 0.25
        gerekce = f"Bahane '{d.bahane}' ekmek değil. İstisna maddesi uygulanmaz."
    if d.goz_temasi and ozur > 0:
        ozur = round(ozur * 0.7, 2)
        gerekce += " Göz teması utanmayı kanıtladı, ceza yumuşadı."
    elif not d.goz_temasi and karar != "KABUL":
        ozur = round(ozur + 0.3, 2)
        gerekce += " Göz kaçırma, mükerrer teşebbüs sayıldı."
    return Hukum(karar, round(ozur, 2), gerekce, dosya_numarasi(d))


def tutanak(d: Dilekce, h: Hukum) -> str:
    satirlar = [
        "=" * 52,
        "SADECE BIR EKMEK KASA ISTISNASI",
        "resmi olmayan tutanak, ciddidir, degildir",
        "=" * 52,
        f"dosya no     : {h.dosya_no}",
        f"urun sayisi  : {d.urun}",
        f"bahane       : {d.bahane}",
        f"acil         : {'evet' if d.acil else 'hayir'}",
        f"goz temasi   : {'var' if d.goz_temasi else 'yok'}",
        "-" * 52,
        f"KARAR        : {h.karar}",
        f"ozur birimi  : {h.ozur}",
        f"gerekce      : {h.gerekce}",
        "-" * 52,
        f"arsiv notu   : {arsiv_notu()}",
        "Damga: EKMEK-ISTISNA / MUHUR-13",
        "Imza: Kayyum Grok, TentiAS kayyim kalemi",
        "Tarih: 3 Ekim 2026",
        "Isim: Tentivory adina, ciddidir, degildir",
        "=" * 52,
    ]
    return "\n".join(satirlar)


def argumanlar() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Sadece bir ekmek kasa istisnasi")
    p.add_argument("--urun", type=int, help="sepetteki urun sayisi")
    p.add_argument("--bahane", default="ekmek", help="soylenen bahane")
    p.add_argument("--acil", choices=["evet", "hayir"], default="hayir")
    p.add_argument("--goz-temasi", choices=["evet", "hayir"], default="hayir")
    return p


def main(argv: list[str] | None = None) -> int:
    args = argumanlar().parse_args(argv)
    if args.urun is None:
        print("Etkilesimli oturum. Cikmak icin urun sayisina -1 yaz.")
        while True:
            try:
                ham = input("urun sayisi: ").strip()
            except EOFError:
                print()
                return 0
            if ham == "-1":
                print("Daire kapandi. Ekmek rafta kaldı.")
                return 0
            try:
                urun = int(ham)
            except ValueError:
                print("sayi gir, kasa fişi degil")
                continue
            bahane = input("bahane [ekmek]: ").strip() or "ekmek"
            acil = input("acil mi (evet/hayir) [hayir]: ").strip().lower() == "evet"
            goz = input("goz temasi (evet/hayir) [hayir]: ").strip().lower() == "evet"
            d = Dilekce(urun, bahane, acil, goz)
            print(tutanak(d, yargila(d)))
            print()
    d = Dilekce(
        args.urun,
        args.bahane,
        args.acil == "evet",
        getattr(args, "goz_temasi") == "evet",
    )
    print(tutanak(d, yargila(d)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
