import mysql.connector
from coneBD import mydb

class quartos():
    def seleciona():
        print("====== CATEGORIAS DISPONIVEIS ===========")
        print('[1] - simples 🙂')
        print('[2] - casal 👫')
        print("[3] - luxo  😎 ")
        cate = input('SELECIONE A CATEGORIA DESEJADA:')
    # --------- ira fazer um select na tabela de categoria simples --------- 
        if cate == '1':
           
            mycursor = mydb.cursor()

            mycursor.execute("select * from hotelmr.simples where situacao  = 1;")

            myresult = mycursor.fetchall()
            print( " |======= TABELA ======|\n | funcionario  / numero quarto /   |\n |=====================|")
            for x in myresult:
                print(' |',  x)
            print(" \n QUARTOS DISPONIVEIS \n  ")
            mycursor == True
#----________________________________________________________________________________
        #ira fazer um update do numero de quarto disponivel -----------
            mycursor = mydb.cursor()
            b = input('digite o numero quarto:')
            val = b
            sql = " UPDATE simples SET situacao = 0 WHERE numero_quarto  = %s;" 
            val = (b,)

            mycursor.execute(sql, val)

            mydb.commit()
         
        

            print(f"DESCRIÇÃO DA RESERVA QUARTO de categoria {cate}",val)
            mycursor == True
            cpf = input('DIGITE SEU CPF NOVAMENTE:')

            
            sql = "insert into check_aut(cpf ,numero_quarto,consumo, total_diaria) values (%s,%s, 200.00, 800.00);" 
            val = (cpf,b)

            mycursor.execute(sql, val)

            mydb.commit()
            print("======================\n CADASTRADO COM SUCESSO \n ")


#____________________ faz um select na tabela casal ____________________________________________________________
        if cate == '2':
          
     
           
            mycursor = mydb.cursor()

            mycursor.execute("select * from hotelmr.casal where situacao  = 1;")

            myresult = mycursor.fetchall()
            print( " |======= TABELA ======|\n | funcionario  / numero quarto /   |\n |=====================|")
            for x in myresult:
                print(' |',  x)
            print(" \n QUARTOS DISPONIVEIS \n  ")
            mycursor == True
#----________________________________________________________________________________
        #ira fazer um update do numero de quarto disponivel -----------
            mycursor = mydb.cursor()
            b = input('digite o numero quarto:')
            val = b
            sql = " UPDATE casal SET situacao = 0 WHERE numero_quarto  = %s;" 
            val = (b,)

            mycursor.execute(sql, val)

            mydb.commit()
         
        

            print(f"DESCRIÇÃO DA RESERVA QUARTO de categoria {cate}",val)
            mycursor == True
            cpf = input('DIGITE SEU CPF NOVAMENTE:')
            
            
            sql = "insert into check_aut(cpf ,numero_quarto,consumo, total_diaria) values (%s,%s, 200.00, 800.00);" 
            val = (b,cpf)

            mycursor.execute(sql, val)

            mydb.commit()

            


#_______________________________________________________________________________________________
              # -------ira fazer um select na tabela de categoria luxo--------#
       
        if cate == '3':
          
           
            mycursor = mydb.cursor()

            mycursor.execute("select * from hotelmr.luxo where situacao  = 1;")

            myresult = mycursor.fetchall()
            print( " |======= TABELA ======|\n | funcionario  / numero quarto /   |\n |=====================|")
            for x in myresult:
                print(' |',  x)
            print(" \n QUARTOS DISPONIVEIS \n  ")
            mycursor == True
#----________________________________________________________________________________
        #ira fazer um update do numero de quarto disponivel -----------
            mycursor = mydb.cursor()
            b = input('digite o numero quarto:')
            val = b
            sql = " UPDATE simples SET situacao = 1 WHERE numero_quarto  = %s;" 
            val = (b,)

            mycursor.execute(sql, val)

            mydb.commit()
         
        

            print(f"DESCRIÇÃO DA RESERVA QUARTO de categoria {cate}",val)
            mycursor == True
            
            sql = "insert into check_aut(cpf ,numero_quarto,consumo, total_diaria) values (1456, %s, 450.0, 800.00);" 
            val = (b,)

            mycursor.execute(sql, val)

            mydb.commit()



#_______________________________________________________________________________________________
        


quartos()

