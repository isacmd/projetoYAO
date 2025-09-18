package patterns.command;

import java.util.Stack;

public class GerenciadorComandos {
    private final Stack<ICommand> historicoComandos;
    private final int maxHistorico;

    public GerenciadorComandos(int maxHistorico) {
        this.historicoComandos = new Stack<>();
        this.maxHistorico = maxHistorico;
    }

    public void executarComando(ICommand comando) {
        comando.execute();
        historicoComandos.push(comando);

        if (historicoComandos.size() > maxHistorico) {
            historicoComandos.removeElementAt(0);
        }
    }

    public void desfazerUltimoComando() {
        if (!historicoComandos.isEmpty()) {
            ICommand ultimoComando = historicoComandos.pop();
            ultimoComando.undo();
        }
    }

    public boolean podeDesfazer() {
        return !historicoComandos.isEmpty();
    }

    public String obterDescricaoUltimoComando() {
        if (!historicoComandos.isEmpty()) {
            return historicoComandos.peek().getDescription();
        }
        return "Nenhum comando para desfazer";
    }
}
