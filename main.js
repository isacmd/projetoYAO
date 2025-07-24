const prompt = require('prompt-sync')();
const UserManager = require('./UserManager');
const UserView = require('./UserView');

const manager = new UserManager();
const view = new UserView(manager);

while (true) {
  console.log("\n1 - Cadastrar usuário");
  console.log("2 - Login");
  console.log("3 - Recuperar senha");
  console.log("4 - Listar usuários");
  console.log("5 - Sair");

  const opcao = prompt("Escolha uma opção: ");

  switch (opcao) {
    case "1":
      console.log("Informe: nome,telefone,dataNasc,cpf,email,senha");
      const cadastro = prompt("Entrada: ");
      console.log(view.mostrarTelaCadastro(cadastro));
      break;
    case "2":
      console.log("Informe: email,senha");
      const login = prompt("Entrada: ");
      console.log(view.mostrarTelaLogin(login));
      break;
    case "3":
      const email = prompt("Digite o email: ");
      console.log(view.mostrarTelaRecuperarSenha(email));
      break;
    case "4":
      console.log(view.mostrarListaUsuarios());
      break;
    case "5":
      console.log("Saindo...");
      process.exit(0);
    default:
      console.log("Opção inválida.");
  }
}
