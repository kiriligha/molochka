
import vk_api
import random
vvod=False
token = "19b0bedcf792b06f6786134da5c4fc6df747ded528cb0694db2f0b468e0a35bb5d050b08b4e48e1179274"

vk = vk_api.VkApi(token=token)
vk._auth_token()
while True:
    messages = vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unanswered"})
    if messages["count"] >= 1:
        id = messages["items"][0]["last_message"]["from_id"]
        body = messages["items"][0]["last_message"]["text"]
        if vvod:
            polis = body.lower()
            print(polis)
            vvod=False
            vk.method("messages.send", {"peer_id": id, "message": "https://barcode.tec-it.com/barcode.ashx?data="+polis+"&code=&multiplebarcodes=false&translate-esc=false&unit=Fit&dpi=96&imagetype=Png&rotation=0&color=%23000000&bgcolor=%23ffffff&codepage=&qunit=Mm&quiet=0", "random_id": random.randint(1, 2147483647)})
        elif body.lower() == "где получать":
            vk.method("messages.send", {"peer_id": id, "message": "Получить молочное питание можно:\n1.Боровая 19.", "random_id": random.randint(1, 2147483647)})
        elif body.lower() == "инфо":
            vk.method("messages.send", {"peer_id": id, "message": "Детям от 8 месяцев до года полагается молочное питание, полачиваемое государством. Из-за того, что нужно выполнить очень много указаний, чтобы получить питание. Большинство молодых мам не получает его, хотя государство тратит на них деньги!\nНаш бот позволяет Вам отправлять полис Вашего ребенка, а мы кидаем Вам штрих-код!", "random_id": random.randint(1, 2147483647)})
        elif body.lower() == "полис":
            vk.method("messages.send", {"peer_id": id, "message": "Отлично, введите полис вашего ребенка состаящий из 12 цифр!", "random_id": random.randint(1, 2147483647)})
            vvod=True
        else:
            vk.method("messages.send", {"peer_id": id, "message": "Не понял Вас!\nВарианты ответов:\n1.'Где получать' - Выводит список магазинов для получения питания\n2.'Инфо' - Выводит информацию про бота\n3.'Полис' - Ввод полиса ребенка для получения штрих-кода", "random_id": random.randint(1, 2147483647)})

