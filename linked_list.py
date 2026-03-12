class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList: 
    def __init__(self):
        self.head = None
        self._size = 0   

    def insert_end(self, element):

        if self.head:
            ponteiro = self.head

            while ponteiro.next:
                ponteiro = ponteiro.next

            ponteiro.next = Node(element)

        else:
            self.head = Node(element)

        self._size += 1

    def insert_beginning(self, element):

        novo = Node(element)

        novo.next = self.head   
        self.head = novo        

        self._size += 1

    def insert_middle(self, index, element):
        if index > self.size():
            print(f"O escopo da função é inserir entre o começo e o fim da lista encadeada.\n O index inserido foi de {index}, ultrapassando o size de {self.size()}")
        if index == 0:
            self.insert_beginning(element)
            return

        ponteiro = self.head
        counter = 0

        while ponteiro and counter < index - 1:
            ponteiro = ponteiro.next
            counter += 1

        if ponteiro:
            novo = Node(element)
            novo.next = ponteiro.next
            ponteiro.next = novo
            self._size += 1

    def size(self):
        return self._size

    def is_empty(self):
        return self.head is None

    def search(self, valor):
        
        ponteiro = self.head

        while ponteiro:
            if ponteiro.data == valor:
                return True

            ponteiro = ponteiro.next
        print("O valor passado não foi encontrado dentro da lista encadeada.")
        return False

    def remove(self, valor_index):
        if self.size() < valor_index + 1:
            return print(f"Impossível remover o {valor_index + 1}° valor de uma lista com somente {self.size()} elemento(s).")
        contador = 0
        if not self.head:
            return
        if contador == valor_index:
            print(f"Valor do index {valor_index} = {self.head.data} removido com sucesso!")
            self.head = self.head.next
            self._size -= 1
            return

        ponteiro = self.head

        while ponteiro.next:

            if contador == valor_index - 1:
                print(f"Valor do index {valor_index} = {ponteiro.next.data} removido com sucesso!")
                ponteiro.next = ponteiro.next.next
                self._size -= 1
                return
            contador += 1
            ponteiro = ponteiro.next

    def print_list(self):

        ponteiro = self.head
        valores = []

        while ponteiro:
            valores.append(str(ponteiro.data))
            ponteiro = ponteiro.next

        print(" --> ".join(valores))

try:
    lista = LinkedList()
    lista.insert_beginning(10)
    lista.insert_beginning(5)
    lista.insert_end(20)
    lista.insert_end(30)
    lista.insert_middle(34, 12)
    lista.size()
    
    print(lista.is_empty())
    lista.remove(123)
    lista.search(23040)
    lista.print_list()
    lista.remove(0)
    lista.remove(2)
    lista.remove(1)
    lista.remove(1)
    lista.print_list()
    
except Exception as err:
    print(f"deu pra testar não pai, isso daí aconteceu: \n{err}")