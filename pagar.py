from coneBD import mydb


class check_aut(): 
    def __init__(self,cpf,b):
      self.cpf = cpf
      self.b = b
    def boleto(self):
          self.cpf = input("DIGITE SEU CPF:")
          self.b = input('digite o numero quarto:')
          mycursor = mydb.cursor()
         
          sql = ("select * from check_aut where numero_quarto = (%s) ;")
          va = (self.cpf,)
          mycursor.execute(sql,va )
          myresult = mycursor.fetchall()
          print( " |======= TABELA ======|\n | quarto/cpf /consumo /diaria/     |\n |=====================|")
          for x in myresult:
                print(' |',  x)
          print(" \n DADOS  de consumo e diarias  ")
          mycursor == True
#----________________________________________________________________________________
      
          mycursor = mydb.cursor()
          val = self.cpf
          sql = " delete  from check_aut where cpf = %s;"  
          val = (self.cpf,)

          mycursor.execute(sql, val,)

          mydb.commit()
          print('\nOBRIGADO VOLTE SEMPRE ')
          mycursor == True

          

#----________________________________________________________________________________
  
          mycursor = mydb.cursor()
          val = self.b
          sql = " UPDATE simples SET situacao = 0 WHERE numero_quarto  = %s;" 
          val = (self.b,)

          mycursor.execute(sql, val)

          mydb.commit()
          print(" OPERAÇÃO FINALIZADA")
         

sai = check_aut(cpf=None,b=None)


       

       
