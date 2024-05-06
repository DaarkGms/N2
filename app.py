from flask import Flask, request, jsonify
from flasgger import Swagger
import pandas as pd

app = Flask(__name__)
swagger = Swagger(app)

# Carregar o dataset
dataset = pd.read_csv("Car_Insurance_Claim.csv")

# Definir rota para o endpoint da API
@app.route('/get_credit_score', methods=['POST'])
def get_credit_score():
    """
    Endpoint para calcular o CREDIT_SCORE com base nos dados fornecidos.
    ---
    parameters:
      - name: idade
        in: formData
        type: string
        required: true
      - name: sexo
        in: formData
        type: string
        required: true
      - name: anos_experiencia_habilitado
        in: formData
        type: string
        required: true
      - name: nivel_escolaridade
        in: formData
        type: string
        required: true
      - name: renda
        in: formData
        type: string
        required: true
      - name: ano_veiculo
        in: formData
        type: string
        required: true
      - name: quilometragem_anual
        in: formData
        type: string
        required: true
      - name: tipo_veiculo
        in: formData
        type: string
        required: true
    responses:
      200:
        description: CREDIT_SCORE calculado com sucesso.
        schema:
          id: credit_score
          properties:
            CREDIT_SCORE:
              type: integer
              description: Pontuação de crédito calculada.
    """
    # Receber dados da requisição
    idade = request.form['idade']
    sexo = request.form['sexo']
    anos_experiencia_habilitado = request.form['anos_experiencia_habilitado']
    nivel_escolaridade = request.form['nivel_escolaridade']
    renda = request.form['renda']
    ano_veiculo = request.form['ano_veiculo']
    tipo_veiculo = request.form['tipo_veiculo']
    quilometragem_anual = request.form['quilometragem_anual']

    # Selecionar os dados do dataset correspondentes aos dados fornecidos
    filtered_data = dataset[
        (dataset['AGE'] == idade) &
        (dataset['GENDER'] == sexo) &
        (dataset['DRIVING_EXPERIENCE'] == anos_experiencia_habilitado) &
        (dataset['EDUCATION'] == nivel_escolaridade) &
        (dataset['INCOME'] == renda) &
        (dataset['VEHICLE_YEAR'] == ano_veiculo) &
        (dataset['VEHICLE_TYPE'] == tipo_veiculo) &
        (dataset['ANNUAL_MILEAGE'] == float(quilometragem_anual))
    ]

    # Obter o CREDIT_SCORE
    if len(filtered_data) > 0:
        credit_score = filtered_data['CREDIT_SCORE'].values[0]
        return jsonify({'CREDIT_SCORE': credit_score})
    else:
        return jsonify({'error': 'Não foi possível calcular o CREDIT_SCORE para os dados fornecidos.'}), 400


if __name__ == '__main__':
    app.run(debug=True)