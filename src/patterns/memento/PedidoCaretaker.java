package patterns.memento;

import java.util.Stack;

public class PedidoCaretaker {
    private final Stack<PedidoMemento> historico = new Stack<>();

    public void salvarEstado(PedidoMemento memento) {
        historico.push(memento);
    }

    public PedidoMemento restaurarEstado() {
        if (!historico.isEmpty()) {
            return historico.pop();
        }
        return null;
    }

    public boolean temHistorico() {
        return !historico.isEmpty();
    }
}