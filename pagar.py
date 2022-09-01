from coneBD import mydb


class check_aut(): 
    def boleto():
          cpf = input("DIGITE SEU CPF:")
          b = input('digite o numero quarto:')
          mycursor = mydb.cursor()
         
          sql = ("select * from check_aut where numero_quarto = (%s) ;")
          va = (cpf,)
          mycursor.execute(sql,va )
          myresult = mycursor.fetchall()
          print( " |======= TABELA ======|\n | quarto/cpf /consumo /diaria/     |\n |=====================|")
          for x in myresult:
                print(' |',  x)
          print(" \n DADOS  de consumo e diarias  ")
          mycursor == True
#----________________________________________________________________________________
      
          mycursor = mydb.cursor()
          val = cpf
          sql = " delete  from check_aut where cpf = %s;"  
          val = (cpf,)

          mycursor.execute(sql, val,)

          mydb.commit()
          print('\nOBRIGADO VOLTE SEMPRE ')
          mycursor == True

          

#----________________________________________________________________________________
  
          mycursor = mydb.cursor()
          val = b
          sql = " UPDATE simples SET situacao = 0 WHERE numero_quarto  = %s;" 
          val = (b,)

          mycursor.execute(sql, val)

          mydb.commit()
          print(" OPERAÇÃO FINALIZADA")
         

check_aut()

       

       
