from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)


quarks=[{'name':'Джамиля Шамгунова', 'email': 'shamgunova1999@gmail.com', 'telegram':'@jamdaring', 'mentor':'Гаухар Рахимбекова', 'mentor_telegram':'@gohin_rm' },
        {'name':'Елена Ковалева', 'email': 'kovalyovayelena@gmail.com', 'telegram':'@YelenaKovalyova', 'mentor':'Гаухар Рахимбекова', 'mentor_telegram':'@gohin_rm' },
        {'name':'Амина Асильбекова', 'email': 'amina-asilbekova@mail.ru', 'telegram':'@darcys_lu', 'mentor':'Дина Мукашева', 'mentor_telegram':'@dinapina' },
        {'name':'Олег Рофман', 'email': 'o.rofman@mail.ru', 'telegram':'@oleg_rofman', 'mentor':'Ануар Уахитов', 'mentor_telegram':'@Wooyeee' },
        {'name':'Жансая Усембаева', 'email': 'z.ussembayeva@gmail.com', 'telegram':'@zhansayusha', 'mentor':'Самат Купаров', 'mentor_telegram':'@QSamat' },
        {'name':'Султан Кенжеханов', 'email': 'sultankenzhekhanov@gmail.com', 'telegram':'@dembeldore', 'mentor':'Сулеймен Даукишов', 'mentor_telegram':'@slmndkshv' },
        {'name':'Акмарал Бисекенова', 'email': 'akmaralbisekenova@gmail.com', 'telegram':'@aqma_ral', 'mentor':'Асылжан Акынова', 'mentor_telegram':'@novaaky' },
        {'name':'Айгерим Ибраева', 'email': 'mdttns@gmail.com', 'telegram':'@vigerim', 'mentor':'Айжан Имангалиева', 'mentor_telegram':'@a_imangaliyeva' },
        {'name':'Андрей Ким', 'email': 'decepmail@gmail.com', 'telegram':'@depeas', 'mentor':'Исламбек Темирбек', 'mentor_telegram':'@ITemirbek' },
        {'name':'Камила Бишенова', 'email': 'kamilabishenova@gmail.com', 'telegram':'@BKamila_K', 'mentor':'Малика Кунсеитова / Рустем Тукабеков', 'mentor_telegram':'@malication' },
        {'name':'Наталья Козулина', 'email': 'ko7ulina@gmail.com', 'telegram':'@Biscuitty', 'mentor':'Максим Коллесников', 'mentor_telegram':'@maxxxony' },
        {'name':'Максим Коллесников', 'email': 'kolesnikov@gmail.com', 'telegram':'@maxxxony', 'mentor':'Дмитрий Казаков', 'mentor_telegram':'@dkazakov' },
        {'name':'Камилла Тен', 'email': 'dixcome@gmail.com', 'telegram':'@dixcome', 'mentor':'Максим Коллесников', 'mentor_telegram':'@maxxxony' }]

@app.route('/', methods=['GET'])
def hello_world():
    return jsonify({'message' : 'Hello, World!'})

@app.route('/quarks', methods=['GET'])
def returnAll():
    return jsonify({'quarks' : quarks})

@app.route('/quarks/<string:name>', methods=['GET'])
def returnOne(name):
    theOne = quarks[0]
    for i,q in enumerate(quarks):
      if q['telegram'] == name:
        theOne = quarks[i]
    return jsonify({'quarks' : theOne})

@app.route('/quarks', methods=['POST'])
def addOne():
    new_quark = request.get_json()
    print(new_quark)
    quarks.append(new_quark)
    return jsonify({'quarks' : quarks})



if __name__ == "__main__":
    app.run(debug=True)