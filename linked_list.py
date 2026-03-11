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

    def size(self):
        return print(f"{self._size}")

    def is_empty(self):
        return self.head is None

    def search(self, valor):

        ponteiro = self.head

        while ponteiro:
            if ponteiro.data == valor:
                return True

            ponteiro = ponteiro.next

        return False

    def remove(self, valor):

        if not self.head:
            return

        if self.head.data == valor:
            self.head = self.head.next
            self._size -= 1
            return

        ponteiro = self.head

        while ponteiro.next:

            if ponteiro.next.data == valor:
                ponteiro.next = ponteiro.next.next
                self._size -= 1
                return

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
    lista.size()
    print(lista.is_empty())
    lista.remove(123)
    lista.search(23040)
    lista.print_list()
except Exception as err:
    print(f"deu pra testar não pai, isso daí aconteceu: \n{err}")