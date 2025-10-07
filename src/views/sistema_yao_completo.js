// ====== PADRÃO 1: COMMAND ======

class AtualizarPedidoCommand {
    constructor(pedido, novosItens) {
        this.pedido = pedido;
        this.novosItens = novosItens;
        this.mementoAnterior = null;
    }

    execute() {
        this.mementoAnterior = this.pedido.criarMemento();
        this.pedido.itens = this.novosItens;
    }

    undo() {
        if (this.mementoAnterior) {
            this.pedido.restaurarMemento(this.mementoAnterior);
        }
    }
}

class GerenciadorComandos {
    constructor() {
        this.historico = [];
    }

    executar(comando) {
        comando.execute();
        this.historico.push(comando);
    }

    desfazer() {
        if (this.historico.length > 0) {
            const comando = this.historico.pop();
            comando.undo();
        }
    }
}

// ====== PADRÃO 2: MEMENTO ======

class PedidoMemento {
    constructor(itens, status) {
        this.itens = [...itens];
        this.status = status;
    }
}

// ====== PADRÃO 3: OBSERVER ======

class Pedido {
    constructor(id) {
        this.id = id;
        this.itens = [];
        this.status = 'PENDENTE';
        this.observers = [];
    }

    // Observer
    addObserver(observer) {
        this.observers.push(observer);
    }

    notifyObservers() {
        this.observers.forEach(obs => obs.update(this));
    }

    // Memento
    criarMemento() {
        return new PedidoMemento(this.itens, this.status);
    }

    restaurarMemento(memento) {
        this.itens = memento.itens;
        this.status = memento.status;
    }

    // Muda status e notifica
    setStatus(novoStatus) {
        this.status = novoStatus;
        this.notifyObservers();
    }
}

class NotificacaoObserver {
    constructor(tipo) {
        this.tipo = tipo;
    }

    update(pedido) {
        console.log(`[${this.tipo}] Pedido ${pedido.id}: ${pedido.status}`);
    }
}

// ====== PADRÃO 4: STRATEGY ======

class PrecificacaoNormal {
    calcular(pedido) {
        return pedido.itens.reduce((total, item) => total + item.preco, 0);
    }
}

class PrecificacaoDesconto {
    constructor(percentual) {
        this.percentual = percentual;
    }

    calcular(pedido) {
        const total = pedido.itens.reduce((total, item) => total + item.preco, 0);
        return total * (1 - this.percentual);
    }
}

class CalculadoraPreco {
    constructor(strategy) {
        this.strategy = strategy;
    }

    calcular(pedido) {
        return this.strategy.calcular(pedido);
    }
}

// ====== PADRÃO 5: COMPOSITE ======

class ElementoCardapio {
    constructor(nome) {
        this.nome = nome;
        this.filhos = [];
    }

    adicionar(elemento) {
        this.filhos.push(elemento);
    }

    exibir(nivel = 0) {
        console.log('  '.repeat(nivel) + this.nome);
        this.filhos.forEach(filho => filho.exibir(nivel + 1));
    }
}

class ItemCardapio {
    constructor(nome, preco) {
        this.nome = nome;
        this.preco = preco;
    }

    exibir(nivel = 0) {
        console.log('  '.repeat(nivel) + `${this.nome} - R$ ${this.preco}`);
    }
}

// ====== DEMONSTRAÇÃO ======

// Command + Memento
const pedido = new Pedido('PED001');
pedido.itens = [{nome: 'Hambúrguer', preco: 15}];

const gerenciador = new GerenciadorComandos();
const comando = new AtualizarPedidoCommand(pedido, [
    {nome: 'Hambúrguer', preco: 15},
    {nome: 'Batata', preco: 8}
]);

gerenciador.executar(comando);
console.log('Após atualizar:', pedido.itens.length); // 2 itens

gerenciador.desfazer();
console.log('Após desfazer:', pedido.itens.length); // 1 item

// Observer
pedido.addObserver(new NotificacaoObserver('Cliente'));
pedido.addObserver(new NotificacaoObserver('Vendedor'));
pedido.setStatus('CONFIRMADO'); // Notifica todos

// Strategy
const calc1 = new CalculadoraPreco(new PrecificacaoNormal());
console.log('Preço normal:', calc1.calcular(pedido));

const calc2 = new CalculadoraPreco(new PrecificacaoDesconto(0.10));
console.log('Preço com desconto:', calc2.calcular(pedido));

// Composite
const cardapio = new ElementoCardapio('Cardápio');
const lanches = new ElementoCardapio('Lanches');
lanches.adicionar(new ItemCardapio('X-Burger', 18));
lanches.adicionar(new ItemCardapio('X-Salada', 20));
cardapio.adicionar(lanches);
cardapio.exibir();