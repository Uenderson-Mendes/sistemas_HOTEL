from coneBD import mydb

class Cadastro():
    def __init__(self,nome,cpf,tele):
        self.nome = nome
        self.cpf = cpf
        self.tele = tele
    def cadstro_cliente(self):
        mycursor = mydb.cursor()
        print('\n CADASTRAR CLIENTE \n')
        self. nome = input('digite seu nome:')
        self. cpf = input('digite o nome de seu cpf :')
        self.tele = input('digite seu telefone:')
        
        val = self.cpf,self.nome,self.tele

        sql = "INSERT INTO reserva (nome, cpf, telefone) VALUES (%s, %s, %s)"
        val = (self.nome,self.cpf, self.tele)
        mycursor.execute(sql, val)

        mydb.commit()

        print("dados inserido",val)
        print("======================\n CADASTRADO COM SUCESSO \n ")
        mycursor == True
        mycursor = mydb.cursor()
     
        conferir = ("select * from hotelmr.reserva where cpf  = %s;")
        sele = (self.cpf,)


        mycursor.execute(conferir, sele)


        myresult = mycursor.fetchall()
        print( "======================\n   NOME    /     CPF / FONE ")
        for x in myresult:

            print(' -----------------------\n',x)
        print("======================\n CADASTRADO COM SUCESSO \n ")

ca = Cadastro(nome=None,cpf=None,tele=None)

