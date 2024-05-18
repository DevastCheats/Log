import requests
from flask import Flask, request, jsonify
from flask_cors import CORS
from threading import Thread

app = Flask('')

CORS(app)


@app.route('/list', methods=['GET'])
def ServersList():
  url_ = 'https://api.eg.rivet.gg/matchmaker/lobbies/list'
  headers_ = {
      "Content-Type": "application/json",
      "Accept": "application/json",
      "Origin": "https://devast.io"
  }
  servers_list = requests.get(url_, headers=headers_)

  if servers_list.status_code == 200:
    response_text = servers_list.text
    return response_text
  else:
    return "Error fetching server list!", 500


@app.route('/find', methods=['POST'])
def FindServer():
  data_ = request.get_json()
  print(data_)
  game_mode = data_.get("game_modes")
  if game_mode:
    url_ = 'https://api.eg.rivet.gg/matchmaker/lobbies/find'
    headers_ = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Origin": "https://devast.io"
    }
    payload_ = {"game_modes": game_mode}
    response_ = requests.post(url_, headers=headers_, json=payload_)
    if response_.status_code == 200:
      response_data = response_.json()
      return jsonify(response_data)


@app.route('/join', methods=['POST'])
def JoinServer():
  data_ = request.get_json()
  print(data_)
  lobby_id = data_.get("lobby_id")
  if lobby_id:
    url_ = 'https://api.eg.rivet.gg/matchmaker/lobbies/join'
    headers_ = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Origin": "https://devast.io"
    }
    payload_ = {"lobby_id": lobby_id}
    response_ = requests.post(url_, headers=headers_, json=payload_)

    if response_.status_code == 200:
      response_data = response_.json()
      return jsonify(response_data)


def run():
  app.run(host="0.0.0.0", port=8080)


def keep_alive():
  server = Thread(target=run)
  server.start()


keep_alive()
