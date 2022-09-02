from coneBD import mydb
class dispon:
        def __init__(self,ca,mycursor,sql):
          self.ca = ca
          self.mycursor = mycursor
          self.sql = sql
    
        def valor_simples(self):
             print('1 -  simple 😃')
             print('2 - casal 👫 ')
             print("3 - luxo😎 ")
             self.ca = input('SELECIONE O SERVIÇO DESEJADO:')
        #serviço quarto simples - ---- - ---------- - - - - - - - -
             if self.ca == '1':

                self.mycursor = mydb.cursor()
                print("1 = 200")
                print('2 = 340.00')
                print("3 = 500.00")
               
                v = input("ESCOLHA O:")
                nu = input("DIGITE O NUMERO DO QUARTO:")
                R  = v
                self.sql = "insert into servico values (%s,'simples',%s);"
                val = (nu,R)
                self.mycursor.execute(self.sql,val)

                mydb.commit()
            
            

                print(f"DESCRIÇÃO DO SERVIÇO {self.ca} simples")

        #---------- serviço quarto casal --------
             if self.ca == '2':


                self.mycursor = mydb.cursor()
                print("1 = 200")
                print('2 = 340.00')
                print("3 = 500.00")
               
                v = input("ESCOLHA O:")
                nu = input("DIGITE O NUMERO DO QUARTO:")
                R  = v
                self.sql = "insert into servico values (%s,'casal',%s);"
                val = (nu,R)
                self.mycursor.execute(self.sql,val)

                mydb.commit()
            
            

                print(f"DESCRIÇÃO DO SERVIÇO {self.ca} casal")
    #________ serviço quarto luxo -----------------------------
             if self.ca == '3':


                self.mycursor = mydb.cursor()
                print("1 = 200")
                print('2 = 340.00')
                print("3 = 500.00")
               
                v = input("ESCOLHA O:")
                nu = input("DIGITE O NUMERO DO QUARTO:")
                R  = v
                self.sql = "insert into servico values (%s,'luxo',%s);"
                val = (nu,R)
                self.mycursor.execute(self.sql,val)

                mydb.commit()
            
            

                print(f"DESCRIÇÃO DO SERVIÇO {self.ca} luxo")


        


ser = dispon(ca=None,mycursor=None,sql=None)              

