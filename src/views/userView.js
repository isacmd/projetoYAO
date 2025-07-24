const User = require('./User');

class UserView {
  constructor(userManager) {
    this.userManager = userManager;
  }

  mostrarTelaCadastro(inputStr) {
    const dados = inputStr.split(',');
    if (dados.length === 6) {
      const user = new User(
        dados[0].trim(), // nome
        parseInt(dados[1].trim()), // telefone
        parseInt(dados[2].trim()), // dataNasc
        dados[3].trim(), // cpf
        dados[4].trim(), // email
        dados[5].trim()  // senha
      );
      this.userManager.cadastrarUsuario(user);
      return "Usuário cadastrado com sucesso.";
    } else {
      return "Erro: entrada inválida (esperado: nome,telefone,dataNasc,cpf,email,senha)";
    }
  }

  mostrarTelaLogin(inputStr) {
    const dados = inputStr.split(',');
    if (dados.length === 2) {
      const sucesso = this.userManager.fazerLogin(dados[0].trim(), dados[1].trim());
      return sucesso ? "Login realizado com sucesso." : "Credenciais inválidas.";
    } else {
      return "Erro: entrada inválida (esperado: email,senha)";
    }
  }

  mostrarTelaRecuperarSenha(inputStr) {
    const senha = this.userManager.recuperarSenha(inputStr.trim());
    return senha ? `Senha: ${senha}` : "Email não encontrado.";
  }

  mostrarListaUsuarios() {
    const lista = this.userManager.listarUsuarios();
    return lista.length > 0
      ? lista.map(u => u.toString()).join('\n')
      : "Nenhum usuário cadastrado.";
  }
}

module.exports = UserView;
