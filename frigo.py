from coneBD import mydb
class frigo():
    def menu():
        print('[1] - ver menu 🙂')
        print('[2] - comprar 👫')
      
        cate = input('SELECIONE A OPCAO DESEJADA:')
        if cate == '1':

   
    # --------- ira fazer um select na tabela frigobar --------- 
    
           
            mycursor = mydb.cursor()

            mycursor.execute("select * from hotelmr.frigobar;")

            myresult = mycursor.fetchall()
            print( " |======= TABELA ======|\n | ID PRODUTO  / NOME /   |\n |=====================|")
            for x in myresult:
                print(' |',  x)
            print(" \n QUARTOS DISPONIVEIS \n  ")



        
#----________________________________________________________________________________

            mycursor = mydb.cursor()
            b = input('digite o numero do produto:')
            val = b
            sql = "DELETE FROM frigobar WHERE id_produto = %s;" 
            val = (b,)

            mycursor.execute(sql, val)
            print("COMPRA EFETUADA")

            mydb.commit()
         
        

           
frigo()

