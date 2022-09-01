from coneBD import mydb
class dispon:
    
        def valor_simples():
             print('1 -  simple 😃')
             print('2 - casal 👫 ')
             print("3 - luxo😎 ")
             ca = input('SELECIONE O SERVIÇO DESEJADO:')
        #serviço quarto simples - ---- - ---------- - - - - - - - -
             if ca == '1':

                mycursor = mydb.cursor()
                print("1 = 200")
                print('2 = 340.00')
                print("3 = 500.00")
               
                v = input("ESCOLHA O:")
                nu = input("DIGITE O NUMERO DO QUARTO:")
                R  = v
                sql = "insert into servico values (%s,'simples',%s);"
                val = (nu,R)
                mycursor.execute(sql,val)

                mydb.commit()
            
            

                print(f"DESCRIÇÃO DO SERVIÇO {ca} simples")

        #---------- serviço quarto casal --------
             if ca == '2':


                mycursor = mydb.cursor()
                print("1 = 200")
                print('2 = 340.00')
                print("3 = 500.00")
               
                v = input("ESCOLHA O:")
                nu = input("DIGITE O NUMERO DO QUARTO:")
                R  = v
                sql = "insert into servico values (%s,'casal',%s);"
                val = (nu,R)
                mycursor.execute(sql,val)

                mydb.commit()
            
            

                print(f"DESCRIÇÃO DO SERVIÇO {ca} casal")
    #________ serviço quarto luxo -----------------------------
             if ca == '3':


                mycursor = mydb.cursor()
                print("1 = 200")
                print('2 = 340.00')
                print("3 = 500.00")
               
                v = input("ESCOLHA O:")
                nu = input("DIGITE O NUMERO DO QUARTO:")
                R  = v
                sql = "insert into servico values (%s,'luxo',%s);"
                val = (nu,R)
                mycursor.execute(sql,val)

                mydb.commit()
            
            

                print(f"DESCRIÇÃO DO SERVIÇO {ca} luxo")


        


                
dispon()
