from flask import Flask, render_template, redirect, url_for, request, flash
import requests
import json


app =  Flask (__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.config.from_object('config')
profiles = 12312


url = "https://webservices.vianuvem.com.br/AdminVianuvem/public/token"
data = {"login":"api.integracao", 
            "pass":"rvQo1W$jq2I{",
            "encryptedPass": "false",
            "token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJhcGkuaW50ZWdyYWNhbyIsInVzZXIiOiJhcGkuaW50ZWdyYWNhbyIsInVzZXJJZCI6NTAyMjE1ODcsImV4cCI6MTcxNzQwMTU1MH0._GNtu9Y5QPYOP7rYzq7mwMTbWvpwvOW3EicuKr6mAB0"}

json_data = json.dumps(data)
    
headers = {"Content-type": "application/json"}
response = requests.post(url, data=json_data, headers=headers)

token = (response.text)
print(token)
strip = token[10:263]
print(strip)






@app.route ('/desativar')
def desativar ():
    return render_template ('desativar.html')


@app.route ('/ativar')
def ativar():
    return render_template ('ativar.html')


@app.route ('/desativar_usuario', methods = ["GET", "POST"])
def desativar_usuario():
    usuario = request.form.get ('usuario')

    if request.method == "POST":
        user = str(usuario)
        bearer_token = strip
        headers = {"Authorization": f"Bearer {bearer_token}"}
        response = requests.delete("https://webservices.vianuvem.com.br/AdminVianuvem/api/users/%s/byLogin" % user, headers=headers)
        if response.status_code == 200:
            flash ("Usuário desativado com sucesso!")
            
        else:
            flash ("Erro: Não foi possivel desativar!")

    return render_template ("desativar.html")





@app.route ('/ativar_usuario', methods = ["GET", "POST"]) 
def ativar_usuario():
    usuario = request.form.get ('usuario')

    if request.method == "POST":
        user = str(usuario)
        bearer_token = strip
        
        headers = {"Authorization": f"Bearer {bearer_token}"}
        
        response = requests.put("https://webservices.vianuvem.com.br/AdminVianuvem/api/users/%s/byLogin" % user, headers=headers)
        if response.status_code == 200:
            flash ("Usuário ativo com sucesso!")

        else:
            flash ("Erro: Não foi possivel ativar")
            print(response.status_code)

    return render_template ("ativar.html")




    


@app.route ('/criar', methods = ["GET", "POST"])
def criar ():
    
    if request.method == "POST":
        
        bearer_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJhcGkuaW50ZWdyYWNhbyIsInZuU2VjcmV0IjoiZjc5NWU3NTdjZWIxYzVhOWY4MGU2ZTlkYjc4YmM0NWMiLCJ1c2VyIjoiYXBpLmludGVncmFjYW8iLCJ1c2VySWQiOjUwMjIxNTg3LCJleHAiOjE3MTk4Nzk0NTB9.clVgvDRV4S06ov_GGdzJ3CoFoKNPlD17ud0GUQqSoio"
        headers = {"Authorization": f"Bearer {bearer_token}"}
        response = requests.post("https://webservices.vianuvem.com.br/AdminVianuvem/api/users/create", headers=headers)
        
    return render_template ("criarusuario.html")

@app.route('/criar_usuario', methods = ["GET","POST"])
def criar_usuario ():
    
    if request.method == "POST":
        nome= request.form.get('nome')
        apelido = request.form.get('apelido')
        cpf= request.form.get('cpf')
        telefone = request.form.get('telefone')
        usuario = request.form.get('usuario')
        senha= request.form.get('senha')
        genero = request.form.get('genero')
        cidade=request.form.get('cidade')
        estado = request.form.get('estado')
        nacionalidade= request.form.get('nacionalidade')
        aniversario = request.form.get('aniversario')
        cnpj= request.form.get('cnpj')
        lista = [nome, apelido,cpf,telefone,usuario,senha,genero,cidade,estado,nacionalidade,aniversario,cnpj]
        print(lista)
    return render_template ('criarusuario.html')


    
    
    

        





app.run(host='0.0.0.0' , port=81,debug=True,threaded=True)