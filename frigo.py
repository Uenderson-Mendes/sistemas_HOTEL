from coneBD import mydb
class frigo():
    def __init__(self,cate,mycursor,val):
        self.cote = cate
        self.mycursor = mycursor
        self.val = val
    
    def menu(self):
        print('[1] - ver menu 🙂')
        print('[2] - comprar 👫')
      
        self.cate = input('SELECIONE A OPCAO DESEJADA:')
        if self.cate == '1':

   
    # --------- ira fazer um select na tabela frigobar --------- 
    
           
            self.mycursor = mydb.cursor()

            self.mycursor.execute("select * from hotelmr.frigobar;")

            myresult = self.mycursor.fetchall()
            print( " |======= TABELA ======|\n | ID PRODUTO  / NOME /   |\n |=====================|")
            for x in myresult:
                print(' |',  x)
            print(" \n PRODUTOS DISPONIVEIS \n  ")



        
#----________________________________________________________________________________

            self.mycursor = mydb.cursor()
            b = input('digite o numero do produto:')
            self.val = b
            sql = "DELETE FROM frigobar WHERE id_produto = %s;" 
            self.val = (b,)

            self.mycursor.execute(sql, self.val)
            print("COMPRA EFETUADA")

            mydb.commit()
         
        

fri = frigo(cate=None,mycursor=None,val=None)         


