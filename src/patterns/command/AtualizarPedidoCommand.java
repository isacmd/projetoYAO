package patterns.command;

import java.util.List;

import models.ItemPedido;
import models.Pedido;
import models.PedidoMemento;
import services.IPedidoService;

public class AtualizarPedidoCommand implements ICommand {
    private final IPedidoService pedidoService;
    private final String pedidoId;
    private final List<ItemPedido> novosItens;
    private final String novasObservacoes;
    private PedidoMemento mementoAnterior;

    public AtualizarPedidoCommand(IPedidoService pedidoService, String pedidoId,
                                  List<ItemPedido> novosItens, String novasObservacoes) {
        this.pedidoService = pedidoService;
        this.pedidoId = pedidoId;
        this.novosItens = novosItens;
        this.novasObservacoes = novasObservacoes;
    }

    @Override
    public void execute() {
        Pedido pedido = pedidoService.buscarPorId(pedidoId);
        mementoAnterior = pedido.criarMemento();
        pedidoService.atualizarPedido(pedidoId, novosItens, novasObservacoes);
    }

    @Override
    public void undo() {
        if (mementoAnterior != null) {
            pedidoService.restaurarPedido(pedidoId, mementoAnterior);
        }
    }

    @Override
    public String getDescription() {
        return "Atualizar pedido: " + pedidoId;
    }
}