# Now, shall we begin?

# OH YEAHHHHHHHHHHHHHHHHHHHHH

"""

Implemente uma Lista Encadeada Simples em Python, conforme discutido em aula.

A implementação deve utilizar classes próprias para representar:

Node → representa cada nó da lista

LinkedList → representa a lista encadeada

Cada nó deve armazenar:

um valor (data)

uma referência para o próximo nó (next)

Métodos obrigatórios

Sua implementação deve conter, no mínimo, os seguintes métodos:

insert_beginning(value) — inserir elemento no início da lista *
insert_end(value) — inserir elemento no final da lista *
remove(value) — remover um elemento da lista 
search(value) — buscar um elemento na lista *
print_list() — imprimir os elementos da lista *
size() — retornar o tamanho da lista *
is_empty() — verificar se a lista está vazia *

Entrega da atividade

extra: adicionar no meio da lista (kenzo)

A entrega será realizada enviando o link do repositório GitHub no Moodle.

Cada aluno deverá criar um repositório público contendo a implementação da atividade.

Nome do repositório

Utilize o seguinte padrão:

ed-lista-encadeada-nome-sobrenome
Exemplo:
ed-lista-encadeada-joao-silva

"""

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self):
        self.initial = None
        self.size = 0

    def insert_end(self, element):
        if self.head:
            ponteiro = self.head
            while(ponteiro.next): ponteiro = ponteiro.next
            ponteiro.next = Node(element)

        else:
            self.head = Node(element)
        self.size += 1

    def insert_beginning(self, element):
        if self.head:
            ponteiro = self.head
            ponteiro.next = Node(element)
        else: 
            self.head = Node(element)
            self.size += 1
    
    def __len__(self):
        return self.size
    
    def search(self, valor):
        if self.head:
            pointer = self.head
            if pointer.head == valor:
                return True
            while pointer.next: 
                ponteiro = ponteiro.next
                if pointer.head == valor:
                    return True
            return False
    
    def print_list(self):
        numeros = []
        if self.head:
            pointer = self.head
            while pointer.next:
                numeros.append(pointer)
            return print(' --> '.join(numeros))
                        
    def is_empty(self):
        if self.head: return False
        else: return True
            
    
        
    # def insert_beginning(self, element):
    #     if self.head:
    #         ponteiro = self.head
    #         while(ponteiro.next != None):

    #             ponteiro = ponteiro.next
                


    