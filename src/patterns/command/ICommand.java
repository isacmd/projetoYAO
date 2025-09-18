package patterns.command;

public interface ICommand {
    void execute();
    void undo();
    String getDescription();
}
