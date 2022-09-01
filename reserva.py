from coneBD import mydb

class Cadastro():
    def __initi__(self,nome,cpf):
        self.nome = nome
        self.cpf = cpf
    def cadstro_cliente():
        mycursor = mydb.cursor()
        nome = input('digite seu nome:')
        cpf = input('digite o nome de seu cpf :')
        tele = input('digite seu telefone:')
        val = cpf,nome,tele

        sql = "INSERT INTO reserva (nome, cpf, telefone) VALUES (%s, %s, %s)"
        val = (nome,cpf, tele)
        mycursor.execute(sql, val)

        mydb.commit()

        print("dados inserido",val)
        print("======================\n CADASTRADO COM SUCESSO \n ")
        mycursor == True
        mycursor = mydb.cursor()
     
        conferir = ("select * from hotelmr.reserva where cpf  = %s;")
        sele = (cpf,)


        mycursor.execute(conferir, sele)


        myresult = mycursor.fetchall()
        print( "======================\n   NOME    /     CPF / FONE ")
        for x in myresult:

            print(' -----------------------\n',x)
        print("======================\n CADASTRADO COM SUCESSO \n ")
Cadastro()
