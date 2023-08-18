from auxiliar import NUMEROS, OPERADORES, PONTUACAO


class Token:

    def __init__(self, arquivo, posicao):
        self.posicao = posicao
        with open(arquivo, 'r') as reader:
            self.text = reader.read()
    
    def prox_token(self):
        token = ''
        for i in range(self.posicao, len(self.text)):
            if self.posicao == len(self.text):
                return None
            
            if self.text[i:i+6] in ['public', 'static', 'return','length', 'String']:
                token = self.text[i:i+6]
                print(token)
                self.posicao += 5
                return token, 'Palavra Reservada', self.posicao
            
            if self.text[i:i+4] in ['void', 'main', 'null', 'true', 'else', 'this']:
                token = self.text[i:i+4]
                print(token)
                self.posicao += 3
                return token, 'Palavra Reservada', self.posicao
            
            if self.text[i:i+5] in ['class', 'while', 'false']:
                token = self.text[i:i+5]
                print(token)
                self.posicao += 4
                return token, 'Palavra Reservada', self.posicao
            
            if self.text[i:i+3] in ['new', 'int']:
                token = self.text[i:i+3]
                print(token)
                self.posicao += 2
                return token, 'Palavra Reservada', self.posicao
            
            if self.text[i:i+7] in ['boolean', 'extends']:
                token = self.text[i:i+7]
                print(token)
                self.posicao += 6
                return token, 'Palavra Reservada', self.posicao
            
            if self.text[i:i+2] == 'if':
                token = self.text[i:i+2]
                print(token)
                self.posicao += 1
                return token, 'Palavra Reservada', self.posicao
            
            if self.text[i:i+18] == 'System.out.println':
                token = self.text[i:i+18]
                print(token)
                self.posicao += 17
                return token, 'Palavra Reservada', self.posicao
            
            if self.text[i] in NUMEROS:
                token = self.text[i]
            
            
            self.posicao += 1

            
        

    def main(self):
        posicao = 0
        tokens = []
        while True:
            teste = Token('teste.txt', posicao).prox_token()
            if teste == None:
                print("fim do arquivo")
                break
            print(teste)
            tokens.append(teste[0])
            posicao = teste[2]
        print(tokens)



