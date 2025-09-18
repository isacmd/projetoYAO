package patterns.command;

import models.Pedido;
import models.StatusPedido;
import services.IPedidoService;

public class ConfirmarPedidoCommand implements ICommand {
    private final IPedidoService pedidoService;
    private final String pedidoId;
    private StatusPedido statusAnterior;

    public ConfirmarPedidoCommand(IPedidoService pedidoService, String pedidoId) {
        this.pedidoService = pedidoService;
        this.pedidoId = pedidoId;
    }

    @Override
    public void execute() {
        Pedido pedido = pedidoService.buscarPorId(pedidoId);
        statusAnterior = pedido.getStatus();
        pedidoService.confirmarPedido(pedidoId);
    }

    @Override
    public void undo() {
        pedidoService.alterarStatusPedido(pedidoId, statusAnterior);
    }

    @Override
    public String getDescription() {
        return "Confirmar pedido: " + pedidoId;
    }
}
