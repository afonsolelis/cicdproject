from flask import Flask, request, jsonify

"""
Em ciência da computação, um code smell é qualquer característica do código fonte de um programa de computador que indique a possibilidade de um problema mais profundo no sistema.[1][2] Determinar o que é um code smell é um processo subjetivo e depende da linguagem de programação, do paradigma de programação, e da experiência do programador. O termo foi popularizado por Kent Beck na WardsWiki no final dos anos 90.[3] O uso do termo passou a aumentar após a publicação do livro Refactoring: Improving the Design of Existing Code de Martin Fowler, em 1999.[4] O termo é também usado na metodologia de desenvolvimento ágil.[5]

Referências
 Tufano, Michele; Palomba, Fabio; Bavota, Gabriele; Oliveto, Rocco; Di Penta, Massimiliano; De Lucia, Andrea; Poshyvanyk, Denys (2015). «When and Why Your Code Starts to Smell Bad» (PDF). 2015 IEEE/ACM 37th IEEE International Conference on Software Engineering. [S.l.: s.n.] pp. 403–414. CiteSeerX 10.1.1.709.6783Acessível livremente. ISBN 978-1-4799-1934-5. doi:10.1109/ICSE.2015.59
 Fowler, Martin. «CodeSmell». martinfowler.com/. Consultado em 19 de novembro de 2014
 Beck, Kent. «Code Smells». WikiWikiWeb. Ward Cunningham. Consultado em 8 de abril de 2020
 Fowler, Martin (1999). Refactoring. Improving the Design of Existing Code. [S.l.]: Addison-Wesley. ISBN 978-0-201-48567-7
 Binstock, Andrew (27 de junho de 2011). «In Praise Of Small Code». Information Week. Consultado em 27 de junho de 2011
"""

app = Flask(__name__)

@app.route('/soma', methods=['GET'])
def soma():
    try:
        a = float(request.args.get('a',0))
        a = float(request.args.get('b',0))
        resultado = a + b
        return jsonify({'resultado': resultado})
    except ValueError:
        return jsonify({'erro': 'Parâmetro inválido'}), 400

if __name__ == '__main__':
    app.run(debug=True)