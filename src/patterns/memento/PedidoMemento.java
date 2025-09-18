package patterns.memento;

import java.time.LocalDateTime;
import java.util.List;
import models.ItemPedido;
import models.StatusPedido;

public class PedidoMemento implements IMemento {
    private final String idPedido;
    private final List<ItemPedido> itens;
    private final String observacoes;
    private final StatusPedido status;
    private final LocalDateTime date;

    public PedidoMemento(String idPedido, List<ItemPedido> itens,
                         String observacoes, StatusPedido status) {
        this.idPedido = idPedido;
        this.itens = List.copyOf(itens);
        this.observacoes = observacoes;
        this.status = status;
        this.date = LocalDateTime.now();
    }

    public String getIdPedido() {
        return idPedido;
    }

    public List<ItemPedido> getItens() {
        return itens;
    }

    public String getObservacoes() {
        return observacoes;
    }

    public StatusPedido getStatus() {
        return status;
    }

    @Override
    public String getName() {
        return idPedido + " - " + date.toString();
    }

    @Override
    public String getDate() {
        return date.toString();
    }
}
