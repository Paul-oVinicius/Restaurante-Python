import os
from turtle import clear


cadastro = []
listapedidos=[]


dictxsalada = {
        "codigo":"1",
        "nome":"X-salada",
        "valor":"10",
}
dictxburguer = {
        "codigo":"2",
        "nome":"X-Burguer",
        "valor":"10",
}
dictcachorroquente = {
        "codigo":"3",
        "nome":"Cachorro Quente",
        "valor":7.50,
}
dictxsalada = {
        "codigo":"4",
        "nome":"Misto Quente",
        "valor":8,
}
dictxsalada = {
        "codigo":"5",
        "nome":"Salada de Fruta",
        "valor":5.50,
}
dictxsalada = {
         "codigo":"6",
        "nome":"Refrigerante",
        "valor":4.50,
}
dictxsalada = {
        "codigo":"7",
        "nome":"Suco Natural",
        "valor":6.25,
}








listaprodutos = [
    {    
        "codigo":"1",
        "nome":"X-salada",
        "valor":10,
    },

      {    
        "codigo":"2",
        "nome":"X-Burguer",
        "valor":10,
    },
      {    
        "codigo":"3",
        "nome":"Cachorro Quente",
        "valor":7.50,
    },
      {    
        "codigo":"4",
        "nome":"Misto Quente",
        "valor":8,
    },
      {    
        "codigo":"5",
        "nome":"Salada de Fruta",
        "valor":5.50,
    },
      {    
        "codigo":"6",
        "nome":"Refrigerante",
        "valor":4.50,
    },
      {    
        "codigo":"7",
        "nome":"Suco Natural",
        "valor":6.25,
    }
]

listacodigo = [1,2,3,4,5,6,7]
listaprodutos2 = ["X-salada","X-Burguer","Cachorro Quente","Misto Quente","Salada de Frutas","Refrigerante","Suco Natural"]
listaprecos = ["10", "10", "7.50", "8", "5.50", "4.50", "6.25"]


def cancelarPedido():
    print()
    print("Para cancelar o pedido, nos informe seu CPF  e sua senha")
    cpf = input("Digite seu CPF: ")
    senha = input("Digite sua Senha: ")
    registro = open("registro.txt","r")
    for linha in registro.readlines():
        conteudo_registro2 = linha.split()
        cadastro.append(conteudo_registro2)
    for elemento in cadastro:
            if(elemento[1] == cpf and elemento[2]==senha):
                cancelarReal = input("Deseja cancelar todo o pedido? Uma vez cancelado, não é possivel recuperar! S (sim) / N (não)")
                cancelarReal = cancelarReal.upper()
                if(cancelarReal.upper() == "S"):
                    os.remove("pedidos.txt")()
                    print("PEDIDO CANCELADO!")
                    main()
                elif(cancelarReal.upper() == "N"):
                    main()
                else:
                    print("Algo de errado aconteceu, verifique se digitou corretamente!")
                    cancelarPedido()   

def inserirProduto():
    print()
    print("Para inserir um produto no seu pedido, nos informe seu CPF  e sua senha")
    cpf = input("Digite seu CPF: ")
    senha = input("Digite sua Senha: ")
    registro = open("registro.txt","r")
    for linha in registro.readlines():
        conteudo_registro2 = linha.split()
        cadastro.append(conteudo_registro2)
    for elemento in cadastro:
            if(elemento[1] == cpf and elemento[2]==senha):
                print()
                print("Codigo \tProduto   \tPreço")
                for produto in listaprodutos:
                    print("%4s \t%4s\t%4.2f" % (produto["codigo"],produto["nome"],produto["valor"]))
                print() 
                
                escolha_do_produto = input("Digite o codigo do produto que deseja! ")
                escolha_da_quantidade = input("Digite a quantidade do produto desejado! ")
                
                pedidos = open("pedidos.txt", "w")
                pedidos.write(" %s %s\n" % (escolha_do_produto,escolha_da_quantidade))
                pedidos.close()
                pedidos = open("pedidos.txt","r")
                for i in pedidos.readlines():
                    pedidos_separados = i.split()                
                    listapedidos.append(pedidos_separados)
                    pedidos.close()
                print(listapedidos)
            else:
                print("Algo de errado aconteceu, verifique se digitou corretamente!")
                main()    


def cancelarProdutodoPedido():
    print()
    print("Para cancelar um produto do seu pedido, nos informe seu CPF  e sua senha")
    cpf = input("Digite seu CPF: ")
    senha = input("Digite sua Senha: ")
    registro = open("registro.txt","r")
    for linha in registro.readlines():
        conteudo_registro2 = linha.split()
        cadastro.append(conteudo_registro2)
    for elemento in cadastro:
            if(elemento[1] == cpf and elemento[2]==senha):
                print("Agora nos informe o codigo do produto que queira cancelar!")
                codigoCancelar = input("Digite o codigo do produto que deseja! ")
                print("Agora nos informe a quantidade do produto que queira cancelar!")
                quantiadeCancelar = int(input("Digite a quantidade do produto desejado! "))
                




                print("Produto cancelado!")
                main()
            else:
                print("Algo de errado aconteceu, verifique se digitou corretamente!")
                main()  



def valor():
    print()
    print("Para valor do pedido, nos informe seu CPF e sua senha")
    cpf = input("Digite seu CPF: ")
    senha = input("Digite sua Senha: ")
    registro = open("registro.txt","r")
    for linha in registro.readlines():
        conteudo_registro2 = linha.split()
        cadastro.append(conteudo_registro2)
    for elemento in cadastro:
            if(elemento[1] == cpf and elemento[2] == senha):
                print("Aqui está o valor do pedido!")
                
                calcularpedidos(listapedidos,listaprodutos)
                
                main()
            else:
                print("Algo de errado aconteceu, verifique se digitou corretamente!")
                    

def extrato():
    print()
    print("Para extrato do pedido, nos informe seu CPF e sua senha")
    cpf = input("Digite seu CPF: ")
    senha = input("Digite sua Senha: ")
    registro = open("registro.txt","r")
    for linha in registro.readlines():
        conteudo_registro2 = linha.split()
        cadastro.append(conteudo_registro2)
    for elemento in cadastro:
        if(elemento[1] == cpf and elemento[2]==senha):
            print("Aqui está seu extrato!")
            calcularpedidos(listapedidos,listaprodutos)


            main()  
        else:
            print("Algo de errado aconteceu, verifique se digitou corretamente!")
            main() 
    
    


def menudopedido():
    print()
    print("Para fazer um pedido, nos informe seu NOME ,CPF e sua SENHA")
    nome = input("Digite seu Nome: ")
    cpf = input("Digite seu CPF: ")
    senha = input("Digite sua Senha: ")
    registro = open("registro.txt","r")
    for linha in registro.readlines():
            conteudo_registro2 = linha.split()
            cadastro.append(conteudo_registro2)
    for elemento in cadastro:
            if(elemento[0]==nome and elemento[1] == cpf and elemento[2]==senha):
                print()
                print("Faça seu pedido")
                print()
                print("Codigo \tProduto   \t\tPreço")
                for produto in listaprodutos:
                    print("%4s \t%4s\t\t%4.2f" % (produto["codigo"],produto["nome"],produto["valor"]))
                print()
                 

                
                escolha_do_produto = input("Digite o codigo do produto que deseja! ")
                escolha_da_quantidade = input("Digite a quantidade do produto desejado! ")
                
               
                
                    
                        
                
                
                pedidos = open("pedidos.txt", "w")
                pedidos.write(" %s %s\n" % (escolha_do_produto,escolha_da_quantidade))
                pedidos.close()
                pedidos = open("pedidos.txt","r")
                for i in pedidos.readlines():
                    pedidos_separados = i.split()                
                    listapedidos.append(pedidos_separados)
                    pedidos.close()
                print(listapedidos)
                
               
                
                segundo_escolha = input("Deseja adicionar outro produto? S(sim) / N(não):")
                segundo_escolha.upper()


                while(segundo_escolha.upper() == "S"):
                    print("Codigo\t Produto   \t\tPreço")
                    for produto in listaprodutos:
                        print("%4s \t%4s\t\t%4.2f" % (produto["codigo"],produto["nome"],produto["valor"]))
                    print()


                    escolha_do_produto = input("Digite o codigo do produto que deseja! ")
                    escolha_da_quantidade = input("Digite a quantidade do produto desejado! ")
                    

                    pedidos = open("pedidos.txt", "a")
                    pedidos.write(" %s %s\n" % (escolha_do_produto,escolha_da_quantidade))
                    pedidos.close()
                    pedidos = open("pedidos.txt","r")
                    for i in pedidos.readlines():
                        pedidos_separados = i.split()                                  
                    listapedidos.append(pedidos_separados)
                    pedidos.close()
                    print(listapedidos)
                    
                    segundo_escolha = input("Deseja adicionar outro produto? S (sim) / N (não):")
                    
                if(segundo_escolha.upper() == "N"):
                    main()
                else:
                    print("Escolha inválida")
                    main()
            else:
                print("Algo de errado aconteceu, verifique se: já possui cadastro/digitou corretamente. Chame um atendente se precisar")
                main()

   
def main():
    print()
    print('1 - Novo Pedido')
    print('2 - Cancela Pedido')
    print('3 - Insere Produto')
    print('4 - Cancela Produto')
    print('5 - Valor do Pedido')
    print('6 - Extrato do pedido')
    print()
    print()
    print('0 - Sair')
    
    escolha = int(input("Escolha uma das opções acima! " ))
    print()

    if(escolha==0):
        exit()
    elif(escolha==1):
        menudopedido()
    elif(escolha==2):
        cancelarPedido()
    elif(escolha==3):
        inserirProduto()
    elif(escolha==4):
        cancelarProdutodoPedido()
    elif(escolha==5):
        valor()
    elif(escolha==6):
        extrato()
    else:
        print("ALGO DE ERRADO ACONTECEU")
        main()  

def cadastroPessoa():       
    verificar_se_tem_cadastro = input("Usuário tem cadastro? S(sim) / N(não): ")
    verificar_se_tem_cadastro = verificar_se_tem_cadastro.upper()
    print(verificar_se_tem_cadastro)
    if(verificar_se_tem_cadastro.upper() == "N"):
        nome = input("Digite o seu NOME: ")
        cpf = input("Digite o seu CPF: ")
        senha = input("Digite uma SENHA: ")
        registro = open("registro.txt", "a")
        registro.write("\n %s %s %s" % (nome,cpf,senha))
        registro.close() 
        registro = open("registro.txt","r")
        conteudo_registro = registro.readlines()
        print(conteudo_registro)
        main()
    
    elif(verificar_se_tem_cadastro.upper() == "S"):
        print("Usuário já possui cadastro. Confirme, por favor.")
        cpf = input("Digite seu CPF: ")
        registro = open("registro.txt","r")
        for linha in registro.readlines():
            conteudo_registro2 = linha.split()
            cadastro.append(conteudo_registro2)
        print(cadastro)
        for elemento in cadastro:
            if(elemento[1]==cpf):
               print("Bem Vindo!")
               menudopedido()
            else:
                print("nada legal")
        print(cadastro)
       
    else:
         print("Escolha inválida")
         cadastroPessoa()







def calcularpedidos(produtos,pedidos):


    for l in pedidos:
        for i in produtos:
            if(l[0]==i["codigo"]):
                print()
                valor = int(l[1])*i["valor"]
                print("Valor:",i["nome"],"-",valor)
            else:
                pass

                   
   

        



cadastroPessoa() 
