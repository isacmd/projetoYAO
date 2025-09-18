package patterns.command;

import models.Pedido;
import models.StatusPedido;
import services.IPedidoService;

public class CancelarPedidoCommand implements ICommand {
    private final IPedidoService pedidoService;
    private final String pedidoId;
    private StatusPedido statusAnterior;

    public CancelarPedidoCommand(IPedidoService pedidoService, String pedidoId) {
        this.pedidoService = pedidoService;
        this.pedidoId = pedidoId;
    }

    @Override
    public void execute() {
        Pedido pedido = pedidoService.buscarPorId(pedidoId);
        statusAnterior = pedido.getStatus();
        pedidoService.cancelarPedido(pedidoId);
    }

    @Override
    public void undo() {
        pedidoService.alterarStatusPedido(pedidoId, statusAnterior);
    }

    @Override
    public String getDescription() {
        return "Cancelar pedido: " + pedidoId;
    }
}
